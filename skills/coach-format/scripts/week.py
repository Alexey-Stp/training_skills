#!/usr/bin/env python3
"""Show the current week's plan from the plan files. No model involved.

Reads plan/weeks/<Monday>.md and plan/days/<date>.md in the data folder and
prints one compact line per planned session, with a mark for what was done.

    python week.py                      # this week, data folder found automatically
    python week.py --date 2027-02-03    # the week holding that date
    python week.py --data path/to/training --out current_week.md

Standard library only.
"""
import argparse
import datetime as dt
import pathlib
import re
import sys

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
MARK = {"done": "✅", "partly": "🟡", "not": "❌", "missed": "❌", "waiting": "⏳",
        "ahead": "·", "none": "❔"}


def find_data_folder(start: pathlib.Path) -> pathlib.Path:
    """The folder holding COACH.md: named in AGENTS.md, or ./training, or here."""
    agents = start / "AGENTS.md"
    if agents.exists():
        m = re.search(r"Coach data index:\s*`?([^`\n]+COACH\.md)`?", agents.read_text(encoding="utf-8"))
        if m:
            p = pathlib.Path(m.group(1).strip()).expanduser()
            p = p if p.is_absolute() else start / p
            if p.exists():
                return p.parent
    for cand in (start, start / "training"):
        if (cand / "plan" / "weeks").is_dir():
            return cand
    return start


def sections(text: str, level: str) -> dict:
    """Split markdown into {heading: body} for headings of the given level."""
    out, name, buf = {}, None, []
    for line in text.splitlines():
        if line.startswith(level + " ") and not line.startswith(level + "#"):
            if name is not None:
                out[name] = "\n".join(buf)
            name, buf = line[len(level) + 1:].strip(), []
        elif name is not None:
            buf.append(line)
    if name is not None:
        out[name] = "\n".join(buf)
    return out


def field(body: str, name: str) -> str:
    m = re.search(rf"^- {re.escape(name)}:\s*(.+)$", body, re.M)
    return m.group(1).strip() if m else ""


def short_target(t: str) -> str:
    """'65-75% Pace' -> '65-75%', '180w' -> '180', 'Z2 HR' -> 'Z2'."""
    t = t.strip()
    t = re.sub(r"\s+(pace|hr|lthr|power|ftp)$", "", t, flags=re.I)
    t = re.sub(r"(?<=\d)\s*w(atts)?$", "", t, flags=re.I)
    return t.replace(" ", "")


def short_step(line: str) -> str:
    """'- 10m 180w' -> '10@180'; '- 20s Rest' -> '20s@Rest'."""
    m = re.match(r"^-\s*(\d+(?:\.\d+)?)\s*([a-zA-Z]*)\s*(.*)$", line.strip())
    if not m:
        return line.strip("- ").strip()
    amount, unit, target = m.groups()
    unit = "" if unit.lower() in ("m", "min", "") else unit.lower()
    target = short_target(target)
    return f"{amount}{unit}@{target}" if target else f"{amount}{unit}"


def short_steps(code: str) -> str:
    """Workout text -> '10@180+10x2@300+15@180' or '15@65-75%+4x(8@100%+2@65%)+10@65-75%'."""
    parts, block, reps = [], [], 1

    def flush():
        nonlocal block, reps
        if not block:
            return
        if reps > 1:
            parts.append(f"{reps}x{block[0]}" if len(block) == 1 else f"{reps}x({'+'.join(block)})")
        else:
            parts.extend(block)
        block, reps = [], 1

    for raw in code.splitlines():
        line = raw.strip()
        if not line:
            flush()
            continue
        if line.startswith("-"):
            block.append(short_step(line))
            continue
        flush()  # a header line starts a new block
        m = re.search(r"(\d+)\s*x\s*$", line, re.I)
        reps = int(m.group(1)) if m else 1
    flush()
    return "+".join(parts)


def short_duration(d: str) -> str:
    m = re.match(r"(\d+)\s*min", d)
    if m:
        return f"{m.group(1)}min"
    m = re.match(r"(\d+):(\d+)", d)
    if m:
        return f"{int(m.group(1)) * 60 + int(m.group(2))}min"
    return d


def planned_sessions(day_text: str) -> list:
    body = sections(day_text, "##").get("Planned sessions", "")
    out = []
    for heading, sbody in sections(body, "###").items():
        title = re.sub(r"^\d+\.\s*", "", heading).strip()
        code = re.search(r"```[^\n]*\n(.*?)```", sbody, re.S)
        steps = short_steps(code.group(1)) if code else ""
        out.append({"title": title, "duration": short_duration(field(sbody, "Duration")),
                    "steps": steps, "targets": field(sbody, "Targets")})
    return out


def review_states(day_text: str) -> tuple:
    """({session title lower: state}, [unplanned headings])."""
    body = sections(day_text, "##").get("Session reviews", "")
    states, unplanned = {}, []
    for heading, rbody in sections(body, "###").items():
        h = re.sub(r"^[^\w]+", "", heading).strip()
        name = h.split(":")[0].strip().lower()
        up = h.upper()
        if "UNPLANNED" in up:
            unplanned.append(h.split(":")[0].strip())
        elif "NOT DONE" in up:
            states[name] = "not"
        elif "PARTLY" in up:
            states[name] = "partly"
        elif "DONE AS PLANNED" in up:
            states[name] = "done"
        elif "NO ACTIVITY" in up:
            states[name] = "missed" if re.search(r"skipped|missed", rbody, re.I) else "waiting"
        elif "WAITING" in up or "waiting on real figures" in rbody:
            states[name] = "waiting"
    return states, unplanned


def verdict(day_text: str) -> str:
    body = sections(day_text, "##").get("Readiness verdict", "")
    m = re.search(r"\*\*([A-Z ]+(?:\(provisional\))?)\*\*", body)
    return m.group(1).strip() if m else ""


def week_header(week_text: str) -> list:
    lines = []
    m = re.search(r"^# (.+)$", week_text, re.M)
    title = m.group(1).replace("Week plan: ", "Week ") if m else "Week"
    status = field(week_text, "Status").split(" (")[0]
    lines.append(f"{title} · {status}" if status else title)
    sync = field(week_text, "Calendar sync")
    if sync and not sync.startswith("last successful"):
        lines.append(f"⚠️ Calendar: {sync}")
    total = re.search(r"^\|\s*Total\s*\|\s*([^|]+)\|\s*([^|]+)\|", week_text, re.M)
    if total:
        lines.append(f"Planned: {total.group(1).strip()} h · load {total.group(2).strip()}")
    return lines


def render(data: pathlib.Path, today: dt.date) -> str:
    monday = today - dt.timedelta(days=today.weekday())
    week_file = data / "plan" / "weeks" / f"{monday.isoformat()}.md"
    if not week_file.exists():
        return f"No week plan for the week of {monday.isoformat()} ({week_file})."
    out = week_header(week_file.read_text(encoding="utf-8"))
    out.append("")
    for i in range(7):
        day = monday + dt.timedelta(days=i)
        label = f"{DAYS[i]} {day.day:>2}"
        day_file = data / "plan" / "days" / f"{day.isoformat()}.md"
        if not day_file.exists():
            out.append(f"{label}  ❔ no day plan")
            continue
        text = day_file.read_text(encoding="utf-8")
        sessions = planned_sessions(text)
        states, unplanned = review_states(text)
        if day == today:
            v = verdict(text)
            label += f" ◀ today{': ' + v if v else ''}"
        if not sessions:
            out.append(f"{label}  Rest")
        for n, s in enumerate(sessions):
            state = states.get(s["title"].lower())
            if state is None:
                state = "ahead" if day >= today else "none"
            steps = s["steps"]
            one = re.fullmatch(r"(\d+)@(.+)", steps)
            if one and s["duration"] == f"{one.group(1)}min":
                steps = "@" + one.group(2)  # one steady step: do not repeat the duration
            detail = " ".join(x for x in (s["duration"], steps or s["targets"]) if x)
            head = label if n == 0 else " " * len(f"{DAYS[i]} {day.day:>2}")
            out.append(f"{head}  {MARK[state]} {s['title']}: {detail}".rstrip(": "))
        for u in unplanned:
            out.append(f"{' ' * 6}  ➕ {u} (unplanned)")
    out += ["", "✅ done  🟡 partly  ❌ not done or missed  ⏳ waiting  · ahead  ❔ no review"]
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description="Show the current week's plan from the plan files.")
    ap.add_argument("--data", help="data folder (the one holding COACH.md and plan/)")
    ap.add_argument("--date", help="any date in the week to show, YYYY-MM-DD (default: today)")
    ap.add_argument("--out", help="also write the view to this file, relative to the data folder")
    a = ap.parse_args()
    data = pathlib.Path(a.data).expanduser() if a.data else find_data_folder(pathlib.Path.cwd())
    today = dt.date.fromisoformat(a.date) if a.date else dt.date.today()
    view = render(data, today)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print(view)
    if a.out:
        target = pathlib.Path(a.out)
        target = target if target.is_absolute() else data / target
        target.write_text(view + "\n", encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# Training skills

Agent skills that coach one endurance athlete: they review completed training and plan what comes next. Built for swim, bike and run, with strength as ordinary sessions.

They run in OpenClaw first and Claude Code second, from the same files. Plans live as markdown in a private folder on the athlete's machine; intervals.icu receives a copy of approved sessions and forwards them to the watch.

## Status

Early. All twelve skills exist and each was checked by dry run on invented data: an agent worked through the same situations with and without the skill. None has been through a full week on real data yet, and several API details are still untested. [`spec/unverified.md`](spec/unverified.md) lists what is not yet proven.

## The skills

Nine the athlete calls, by name or in plain words:

| Skill | Ask it | What it does |
|---|---|---|
| [`coach-setup`](skills/coach-setup/SKILL.md) | "set up my profile", "my FTP changed" | Creates and updates the data index, the athlete profile and the athlete's own rules |
| [`coach-today`](skills/coach-today/SKILL.md) | "what's today", "am I ready" | The daily check: today's session and a readiness verdict of go, modify or skip, from sleep, HRV, resting heart rate, form and yesterday's training |
| [`coach-review-session`](skills/coach-review-session/SKILL.md) | "review my run" | Assesses one activity against its planned session |
| [`coach-review-week`](skills/coach-review-week/SKILL.md) | "how was my week" | Reviews a finished week and says whether the athlete is on track |
| [`coach-plan-week`](skills/coach-plan-week/SKILL.md) | "plan next week" | Drafts the coming week; publishes it after approval |
| [`coach-adjust`](skills/coach-adjust/SKILL.md) | "I missed it", "I'm tired", "move Thursday" | Changes an approved plan, shown as before and after |
| [`coach-plan-month`](skills/coach-plan-month/SKILL.md) | "plan the next block" | Drafts the next block of weeks from the season plan |
| [`coach-plan-season`](skills/coach-plan-season/SKILL.md) | "plan my season", "I added a race" | Drafts the season: phases, and every week as load, easy, taper, race or recovery, counted back from the target races |
| [`coach-nutrition`](skills/coach-nutrition/SKILL.md) | "what's my calorie target", "how much should I eat today" | Gives the day's nutrition target in kcal, carbohydrate, protein and fat: an estimate while a session is still ahead, final once the training is recorded |

Three shared ones the others call:

| Skill | Holds |
|---|---|
| [`coach-rules`](skills/coach-rules/SKILL.md) | Coaching limits and defaults; the athlete's own rules override them |
| [`coach-data`](skills/coach-data/SKILL.md) | Finding the data folder and getting training figures |
| [`coach-format`](skills/coach-format/SKILL.md) | Plan file layouts, calendar sync and the shared vocabulary |

## How it behaves

- **Markdown is the truth.** Plans are files; the calendar is a copy.
- **Approval before publishing.** A plan or plan update is shown first. Nothing reaches the calendar until the athlete approves it.
- **Limits and defaults.** A limit is not planned past without the athlete's explicit say-so. A default can be departed from, with the reason written into the plan.
- **No invented numbers.** A figure that is missing is said to be missing.
- **The verdict advises.** The daily check does not change the plan. A change goes through `coach-adjust` and needs approval.
- **Races are planned sessions.** Each has a priority of A, B or C, which sets the taper before it and the easy days after. A readiness verdict does not ease or move a race.
- **Few questions.** A skill looks for a value, works it out from history, or assumes a marked default before it asks.

## Your data stays out of this repo

The skills are public; the athlete's data is not. Everything personal lives in a data folder on the athlete's machine: profile, rules, plans, reviews. Keys live in files in the home directory.

`coach-setup` writes a small index, `COACH.md`, into that folder. It tells the other skills where each file is and which private command answers each data question. The skills find the index through one line in the runtime's standing instructions:

```
Coach data index: <path to COACH.md>
```

The files a skill writes follow the templates in [`skills/coach-format/templates/`](skills/coach-format/templates/). All values in them are invented.

## Install

**OpenClaw.** Copy the twelve folders under `skills/` into your workspace's `skills/` folder. They are picked up without a restart. In Telegram the commands appear with underscores, for example `/coach_setup`.

**Claude Code.** Copy the twelve folders into `~/.claude/skills/`.

Then run `coach-setup`. It proposes which of your existing documents to import from and shows the profile and rules for approval before writing them.

The repo also carries a Claude Code plugin manifest in `.claude-plugin/`. Installing it as a plugin, or as a linked bundle in OpenClaw, is untested.

## See the week without asking

A small script prints the current week straight from the plan files, with no model involved:

```
python skills/coach-format/scripts/week.py --data <your data folder>
```

```
Week 1 to 7 Feb 2027 · APPROVED
Planned: 9:45 h · load 528

Mon  1  ✅ Easy swim: 50min @70-80%
Tue  2  🟡 Threshold run: 65min 15@65-75%+4x(8@100%+2@65%)+10@65-75%
        ❌ Strength: 20min core and hips
Wed  3 ◀ today: GO  · Bike intervals: 75min 10@180+10x2@300+15@180
Thu  4  · Easy run: 55min @65-75%
Fri  5  Rest
```

Steps read as minutes@target, joined by `+`; `10x2@300` is ten times two minutes at 300. Add `--out current_week.md` to store the view in the data folder, and `--date` for another week. The skills refresh that file after every change to a plan.

## What you need

- An [intervals.icu](https://intervals.icu) account with a personal API key. It is the primary source of activities and the calendar the plans are published to.
- A watch that receives planned sessions from intervals.icu, if you want them on your wrist.
- Optional: your own scripts that turn raw activity data into figures (a readiness score, per-rep analysis). The skills call them through the index and expect JSON in the shape listed in [`coach-data`](skills/coach-data/SKILL.md). Without them the skills work from basic intervals.icu figures.

## Repo layout

| Path | What |
|---|---|
| `skills/` | The twelve skills |
| `spec/` | The decisions the skills were built from, and what is still untested |
| `GLOSSARY.md` | The terms the project uses |
| `AGENTS.md` | Rules for agents working on this repo |

## Not in scope

More than one athlete, sports beyond swim, bike and run, food logging, and meal plans. Nutrition goes as far as a fuelling line on sessions over 90 minutes and the day's nutrition target.

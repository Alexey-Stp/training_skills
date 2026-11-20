# The data folder

Where private training data lives and what each file looks like.

## Location and access

From [private training data][t8]:

- One shared local folder: the `training/` folder inside the athlete's OpenClaw workspace. Claude Code reads and writes the same files. No second copy, no remote.
- A skill finds it through a one-line pointer: in OpenClaw the workspace `AGENTS.md` points at the data index; in Claude Code the user-level `CLAUDE.md` names the folder.
- Keys sit in per-service files in the home directory, outside the data folder. The index records each file's path, never a key.
- The workspace is already a local git repository with no remote. Skills commit there after each write.

## Layout

From [plan files][t10]; examples accepted in [file templates][t24].

| What | Path | Written by | Example |
|---|---|---|---|
| Data index | `COACH.md` | `coach-setup` | [COACH.md](examples/COACH.md) |
| Athlete profile | `ATHLETE.md` | `coach-setup` only | [ATHLETE.md](examples/ATHLETE.md) |
| Athlete rules | `ATHLETE-RULES.md` | `coach-setup` | [ATHLETE-RULES.md](examples/ATHLETE-RULES.md) |
| Season plan | existing file | the athlete; `coach-setup` replaces its goals and anchors sections with a pointer, once | none |
| Month plan | `plan/months/<first Monday of the block>.md` | `coach-plan-month` | [2027-01-18.md](examples/plan/months/2027-01-18.md) |
| Week plan | `plan/weeks/<Monday>.md` | `coach-plan-week`, `coach-adjust`, `coach-review-week` | [2027-02-01.md](examples/plan/weeks/2027-02-01.md) |
| Day plan | `plan/days/<date>.md` | `coach-plan-week`, `coach-adjust`, `coach-today`, `coach-review-session`; any `coach-*` skill, for a score it hears | [2027-02-02.md](examples/plan/days/2027-02-02.md) |

## Data index

Sections: files; key file paths; the command for each training data question; settings, as in the accepted example. ([training data contract][t21], [file templates][t24])

## Athlete profile

From [athlete profile contents][t9] and [athlete setup flow][t25]:

- Eight sections: basics (birth year, height, timezone); sport mode; goals and target races; anchors (bike FTP, CP and W′; run threshold pace and LTHR; swim CSS; max HR); zones; availability; limitations; equipment. Then a change log.
- intervals.icu is authoritative for every threshold and zone it holds. The profile keeps a dated copy of each threshold, as an anchor; zones are read from intervals.icu when needed and not copied (see Amendments in the [README](README.md)). The profile is authoritative for CP and W′, goals, availability, limitations and equipment. When the two differ, the skill shows both and asks; it never overwrites either silently.
- Weight, HRV baseline and resting-heart-rate baseline are computed from wellness data, not typed in. The profile records only how each is computed.
- Every anchor carries value, date, method (tested, derived, estimated) and source (intervals.icu, a named imported document, or stated by the athlete). Skills prescribe only from the latest tested anchor. An anchor older than 8 weeks, or only estimated, is flagged whenever it is used.
- Goals, target races and anchors live here. The season plan keeps phases, the macro calendar and its change log, and points here for numbers.
- Limitations: what, since when, which athlete rule it triggers. Day-to-day scores are not profile data; the profile says where they are logged, which is the day plan's "How I felt".
- Availability: a weekly template (time available, fixed commitments, facility access) plus dated exceptions.
- Holds the default sport mode. ([sport mode][t12])

## Athlete rules

Seven fixed headings, any of which may be empty ([file templates][t24]): limits; targets; readiness bands; weekly shape; departures from the coaching rules; routines; kept from the earlier setup.

- They override the public coaching rules where the two differ. ([replace, absorb or coexist][t18])
- Which bike anchor targets derive from is stated here. ([coaching method][t11])
- Readiness band cut-offs are stated here. ([today skill][t20])
- A routine named here, for example mobility, appears in the week plan as a one-line reminder, with no load and no review. ([map][map])

## Month plan

One block of whole weeks, normally four, Monday to Sunday. ([plan files][t10])

- Header: status; phase, taken from the season plan; sport mode and focus for the block. ([sport mode][t12])
- Reasoning for the block.
- One row per week: role (load or easy), hours, planned load, per-sport volumes, key sessions.
- Checks for the block; any test.
- Block review. Who writes it is an open point in the [README](README.md).

## Week plan

One file per week from the moment it is drafted. No separate archive; the current week is found by date. ([plan files][t10])

- Header: status; calendar sync state (time of last successful publish, or not synced); link to the month plan; sport mode and focus, inherited. ([calendar sync][t13])
- "Why this week looks like this", including any departure from a default and its reason. ([coaching method][t11])
- Targets: hours and planned load per sport, run load visible on its own.
- Checks.
- Days: one line per day linking to the day plan.
- Changes: one entry per plan update: when, what changed from what to what, why.
- Actual vs plan: written by week review.

## Day plan

The only place a day's planned sessions are written in full. It accumulates through the day. ([plan files][t10])

1. Planned sessions. Fixed fields: sport, title, duration, planned load, purpose, targets, caps, calendar state. Then the steps, in intervals.icu workout text, so calendar sync can publish them without retyping.
2. Readiness verdict, with the inputs behind it. ([today skill][t20], [file templates][t24])
3. "How I felt": the subjective log. ([subjective log][t23])
4. Session reviews, including a planned session with no activity. ([session review][t14], [map][map])

Day plans have no status of their own; they follow their week.

## Status

Week and month plans carry DRAFT, then APPROVED, then CLOSED. Closed means reviewed. `coach-review-week` closes a week; who closes a month plan is an open point in the [README](README.md). ([plan files][t10])

## How far ahead

- Month plan: the current block, plus the next one drafted during the current block's last week.
- Week plan: the current week, plus next week's draft from Sunday.
- Day plans: created for all seven days when the week is drafted.

## Subjective log

From [subjective log][t23]. All scores are optional.

| Score | Scale | When |
|---|---|---|
| Effort | 0 to 10 | per activity |
| Overall feel | 1 to 5 | per day |
| Soreness | 1 to 5 | per day |
| Pain | 0 to 10 | per standing limitation in the profile |
| Illness | flag | per day |
| Note | free text | any time |

- Only the effort score is also written to the matching activity in intervals.icu.
- No dedicated skill: whichever skill hears a score writes it, whether or not its own Writes section lists the subjective log. A plain remark in chat is logged too.
- Asked at most once each morning and once per activity. Missing scores never block anything.

## What the suite does not touch

From [replace, absorb or coexist][t18] and the [map][map]:

- Nutrition files and jobs. A nutrition job may read the day plan for the day's planned load; the suite reads nothing from nutrition.
- The runtime's daily memory notes. The day plan replaces them for coaching; coach skills neither read nor write them.
- The private analysis scripts, except to run the commands the index lists.
- Calendar entries the suite did not create.

[t8]: https://github.com/Alexey-Stp/training_skills/issues/8
[t9]: https://github.com/Alexey-Stp/training_skills/issues/9
[t10]: https://github.com/Alexey-Stp/training_skills/issues/10
[t11]: https://github.com/Alexey-Stp/training_skills/issues/11
[t12]: https://github.com/Alexey-Stp/training_skills/issues/12
[t13]: https://github.com/Alexey-Stp/training_skills/issues/13
[t14]: https://github.com/Alexey-Stp/training_skills/issues/14
[t18]: https://github.com/Alexey-Stp/training_skills/issues/18
[t20]: https://github.com/Alexey-Stp/training_skills/issues/20
[t21]: https://github.com/Alexey-Stp/training_skills/issues/21
[t23]: https://github.com/Alexey-Stp/training_skills/issues/23
[t24]: https://github.com/Alexey-Stp/training_skills/issues/24
[t25]: https://github.com/Alexey-Stp/training_skills/issues/25
[map]: https://github.com/Alexey-Stp/training_skills/issues/1

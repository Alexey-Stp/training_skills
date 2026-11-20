---
name: coach-data
description: Use at the start of any coach skill, and whenever training figures are needed (readiness, activities, activity analysis, week summary, load state). Finds the athlete's data folder and answers from the analysis layer or intervals.icu.
user-invocable: false
---

# Training data

How a coach skill finds the athlete's private files and gets its figures. This skill names questions; the athlete's data index maps each to a private command.

## Steps

1. **Find the data index.** The runtime's standing instructions carry one line, `Coach data index: <path to COACH.md>`: the workspace `AGENTS.md` in OpenClaw, the user-level `CLAUDE.md` in Claude Code. Read that `COACH.md`. If there is no line or no file, say so and point to `coach-setup`; stop there.
2. **Refresh** before reading any figure: run the index's Refresh command.
3. **Ask the question** by running the index's command for it, with the arguments filled in. Run it exactly as listed.
4. **Fall back** when the index has no command for the question, or the command fails: read the basics from intervals.icu (see [intervals-icu.md](intervals-icu.md)), tell the athlete the figures are basic, and report which command is missing or broken.
5. **Check each activity** before passing it on. A Garmin-recorded activity with no streams and no detail is an empty stub: follow [garmin-fallback.md](garmin-fallback.md).

Done when the calling skill has every figure it asked for, each one either real or named as missing.

## The questions

Each command prints one JSON object. A value that is not known is `null`, never `0` and never omitted.

| Question | Arguments | Answer |
|---|---|---|
| Refresh | none | `{ok, new_activities, wellness_days, errors[]}` |
| Readiness for a date | date | `{date, score, inputs: {sleep_hours, sleep_score, hrv, hrv_baseline, resting_hr, resting_hr_baseline, form, device_readiness}}` |
| Activities in a date range | from, to | `{activities: [{id, start, sport, name, duration_s, load, source, paired_event_id, stub}]}` |
| Analysis of one activity | activity id | `{id, sport, duration_s, load, intervals: [{label, duration_s, distance_m, pace_s_per_km, pace_s_per_100m, power_w, hr_avg}], drift_pct, time_in_zones_s[], time_in_target_s, stub}` |
| Week summary | Monday's date | `{monday, sports: {<sport>: {sessions, hours, load, distance_km}}, total: {hours, load}, easy_sessions, hard_sessions, monotony}` |
| Load state | none | `{date, fitness, fatigue, form, ramp}` |
| Name an activity (optional) | activity id | `{id, name}`; renames the activity in intervals.icu |

`device_readiness` is optional and often `null`. A scheduled sync on the athlete's machine is a head start; still refresh.

## Keys

Key files live in the home directory, at the paths the index lists. Pass a key file's path to a command or read it only to make a call. In files, messages and logs, refer to a key by its file path. Asked for a key's value, give the path.

## Boundaries

- Run only commands the data index lists, and leave the analysis layer's scripts as they are. A broken command is reported, then step 4 applies.
- A number comes from a command or from intervals.icu. When neither has it, say it is missing.
- Garmin is read-only. Planned sessions reach the watch through intervals.icu.
- Writes to an activity in intervals.icu (effort, the short review, the fallback upload) are listed in [intervals-icu.md](intervals-icu.md); calendar events belong to `coach-format`.

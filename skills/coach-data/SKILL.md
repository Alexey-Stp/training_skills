---
name: coach-data
description: Use at the start of any coach skill, read in one turn with the data index and `coach-rules`, and whenever training figures are needed (readiness, activities, activity analysis, week summary, load state). Finds the athlete's data folder and answers from the analysis layer or intervals.icu.
user-invocable: false
---

# Training data

How a coach skill finds the athlete's private files and gets its figures. This skill names questions; the athlete's data index maps each to a private command.

## Steps

1. **Find the data index.** The runtime's standing instructions carry one line, `Coach data index: <path to COACH.md>`: the workspace `AGENTS.md` in OpenClaw, the user-level `CLAUDE.md` in Claude Code. Read that `COACH.md`. If there is no line or no file, say so and point to `coach-setup`; stop there.
2. **Refresh** before reading any figure: run the index's Refresh command.
3. **Ask the question** by running the index's command for it, with the arguments filled in. Run it exactly as listed.

   Ask in one call: the refresh first, then every question the calling skill needs, chained one after another in that order where the runtime can chain commands. Never run the refresh and a question side by side.
4. **Fall back** when the index has no command for the question, or the command fails: read the basics from intervals.icu (see [intervals-icu.md](intervals-icu.md)), tell the athlete the figures are basic, and report which command is missing or broken.
5. **Check each activity** before passing it on. A Garmin-recorded activity with no streams and no detail is an empty stub: follow [garmin-fallback.md](garmin-fallback.md).

Done when the calling skill has every figure it asked for, each one either real or named as missing.

## Loading in two rounds

Each round of tool calls sends the whole conversation to the model again, so a coach skill loads in two:

1. In parallel in one turn: this skill, the data index and `coach-rules`.
2. In parallel in the next turn:
   - the one call of step 3: the refresh, then every question the skill asks in its "Load" and "Get the figures" steps, with the activities list among them whenever an activity's id is needed later;
   - every file those steps list, the athlete profile and `ATHLETE-RULES.md`, and the files in `coach-rules` that the skill itself names (such as `race-prep.md`);
   - the files its later steps need for writing, such as `coach-format` and [intervals-icu.md](intervals-icu.md).

   The refresh does not change plan files, so they are read beside it. A day plan for a date the athlete named or the request implies ("review my run" with no day is today's) is read in this turn, with the week plan; it does not wait for the activity.

One more turn only for what needs an answer first: an activity's analysis, which needs the activity's id, and a file whose name only an answer gives, such as the month plan named in the week plan header. A file already read in this conversation is not read again.

## The questions

Each command prints one JSON object. A value that is not known is `null`, never `0` and never omitted.

| Question | Arguments | Answer |
|---|---|---|
| Refresh | none | `{ok, new_activities, wellness_days, errors[]}` |
| Readiness for a date | date | `{date, score, inputs: {sleep_hours, sleep_score, hrv, hrv_7d, hrv_baseline, resting_hr, resting_hr_baseline, form, device_readiness}}` |
| Activities in a date range | from, to | `{activities: [{id, start, sport, name, duration_s, distance_m, load, work_kj, device_kcal, source, paired_event_id, stub}]}` |
| Analysis of one activity | activity id | `{id, sport, duration_s, distance_m, load, hr_avg, hr_max, cadence_avg, climb_m, power_avg_w, power_norm_w, intervals: [{label, duration_s, distance_m, pace_s_per_km, pace_s_per_100m, power_w, hr_avg, hr_max, cadence}], splits_km: [{km, pace_s_per_km, hr_avg, hr_max, cadence}], drift_pct, time_in_zones_s[], hr_time_in_zones_s[], time_in_target_s, stub}` |
| Week summary | Monday's date | `{monday, sports: {<sport>: {sessions, hours, load, distance_km}}, total: {hours, load}, easy_sessions, hard_sessions, monotony}` |
| Load state | date (optional; today when left out) | `{date, fitness, fatigue, form, ramp}` |
| Best efforts in a date range (optional) | sport, from, to | `{efforts: [{activity_id, date, distance_m, time_s}]}`: the fastest time for each standard distance |
| Food intake for a date (optional) | date | `{date, kcal, carbs_g, protein_g, fat_g, items}` |
| Name an activity (optional) | activity id | `{id, name}`; renames the activity in intervals.icu |

`device_readiness` is optional and often `null`. `time_in_zones_s` is in the sport's own zones (power for a ride with power, pace for a run or a swim, heart rate otherwise) and `hr_time_in_zones_s` in heart-rate zones; when a command gives neither, read the activity's zone times from intervals.icu. `work_kj` is the work a power meter measured and `device_kcal` the recording device's own energy figure; when a command gives neither, read them from the activity in intervals.icu. There is no command for weight: work it out from the wellness records in intervals.icu, as the athlete profile says. `hrv_7d` is the average of the last seven nights; when a command does not give it, work it out from the wellness records in intervals.icu. A scheduled sync on the athlete's machine is a head start; still refresh.

## Keys

Key files live in the home directory, at the paths the index lists. Pass a key file's path to a command or read it only to make a call. In files, messages and logs, refer to a key by its file path. Asked for a key's value, give the path.

## Boundaries

- Run only commands the data index lists, and leave the analysis layer's scripts as they are. A broken command is reported, then step 4 applies.
- A number comes from a command or from intervals.icu. When neither has it, say it is missing.
- Garmin is read-only. Planned sessions reach the watch through intervals.icu.
- Writes to an activity in intervals.icu (effort, the review, the name, the fallback upload) are listed in [intervals-icu.md](intervals-icu.md); calendar events belong to `coach-format`.

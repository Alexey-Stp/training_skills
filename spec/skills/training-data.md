# Training data (shared skill)

The skill's name is not decided; see the open points in the [README](../README.md).

## Purpose

Tell every other skill how to find the data folder, read the activity sources, and get figures from the athlete's private analysis layer, without this repo ever naming a private script.

## Triggers

Called by other skills only, at the start of each of them.

## Reads

- The data index, found through the runtime's pointer: the workspace `AGENTS.md` in OpenClaw, the user-level `CLAUDE.md` in Claude Code. ([private training data][t8])
- Key files, by the paths the index gives.
- The analysis layer, by running the commands the index lists.
- intervals.icu, the primary activity source. Garmin, the secondary one, for data intervals.icu lacks.

## Writes

Nothing in the data folder. Through intervals.icu it performs the writes other skills ask for: the effort score and the short review on an activity, and the fallback upload described below.

## Steps

1. Find and read the data index. If there is none, say so and point to `coach-setup`.
2. Before a skill reads, refresh.
3. Answer the calling skill's question from the analysis layer.
4. If the question has no command in the index, or the command fails, read intervals.icu directly for the basics, state that the figures are basic, and report the broken command.

### The questions

From [training data contract][t21]. Answers are JSON with fixed field names; the fields are an open point.

| Question | Answer |
|---|---|
| Refresh | pulls the latest activities and wellness |
| Readiness for a date | one score plus its inputs |
| Activities in a date range | list with sport, duration, load |
| Analysis of one activity | reps or intervals with pace, power and heart rate; drift; time in zones |
| Week summary | hours and load per sport, easy/hard share, monotony |
| Load state | fitness, fatigue, form, ramp |
| Name an activity (optional) | renames the activity in the activity source |

Any scheduled sync is a head start, not a dependency.

### Without an analysis layer

The normal path in a runtime that has none, such as Claude Code on another machine. From intervals.icu directly: activity summary, wellness, fitness figures. From [intervals.icu API][t2]:

- Auth: HTTP Basic, username `API_KEY`, password the personal key. Athlete id `0` means the owner of the key.
- Limits: 5000 requests a day, 2500 per rolling 15 minutes, 10 a second per address; a 429 carries `Retry-After`.
- Activities carry `source` and `paired_event_id`, the link to the planned workout.
- Wellness per day: resting heart rate, HRV, sleep, readiness, weight, subjective fields, fitness and fatigue. Form is computed, not a field.
- Thresholds and zones per sport come from sport settings.

### If intervals.icu stops serving Garmin data

From [activity source resilience][t15]. intervals.icu stays primary and nothing switches early.

1. Check each activity read. A Garmin-recorded activity that comes back as an empty stub is reported as such.
2. First fallback: fetch the original activity file from Garmin and upload it to intervals.icu as the athlete's own file, so load, fitness figures and pairing with planned sessions keep working.
3. Second fallback: the analysis layer answers "analysis of one activity" directly from the Garmin file.
4. Sleep, HRV and resting heart rate are read from Garmin directly if intervals.icu stops serving them.

The Garmin route named by this spec is the official Personal API key, which is read-only. It has no Training Readiness figure, so that readiness input is optional. ([Garmin as secondary source][t3])

## Reply

None to the athlete, except to say plainly when figures are basic, when a command is broken, or when an activity is an empty stub.

## Must never

- Print, log or copy a key, token or password. Refer to key files by path only.
- Run a command the data index does not list.
- Edit a script in the analysis layer.
- Invent a number, or pass on empty data as if it were real.
- Write to Garmin.

## Source tickets

[Training data contract][t21], [private training data][t8], [intervals.icu API][t2], [Garmin as secondary source][t3], [activity source resilience][t15], [replace, absorb or coexist][t18].

[t2]: https://github.com/Alexey-Stp/training_skills/issues/2
[t3]: https://github.com/Alexey-Stp/training_skills/issues/3
[t8]: https://github.com/Alexey-Stp/training_skills/issues/8
[t15]: https://github.com/Alexey-Stp/training_skills/issues/15
[t18]: https://github.com/Alexey-Stp/training_skills/issues/18
[t21]: https://github.com/Alexey-Stp/training_skills/issues/21

# intervals.icu directly

For when the data index has no command for a question, or the command fails. These are the basic figures: activity summary, wellness, fitness. Say "basic figures" to the athlete whenever an answer comes from here.

## Access

- Base: `https://intervals.icu/api/v1`.
- Auth: HTTP Basic, username `API_KEY`, password the personal key from the key file the index lists.
- Athlete id `0` means the owner of the key.
- Limits: 5000 requests a day, 2500 per rolling 15 minutes, 10 a second per address. A 429 carries `Retry-After`; wait that long.

## What is there

| Need | Where | Notes |
|---|---|---|
| Activities | the athlete's activities, by date range | each carries `source` and `paired_event_id`, the link to its planned session's calendar event |
| Wellness per day | the athlete's wellness records | resting heart rate, HRV, sleep, readiness, weight, subjective fields, fitness and fatigue |
| Form | computed: fitness minus fatigue | it is not a stored field |
| Thresholds and zones | sport settings, per sport | intervals.icu is authoritative for these; the unit of the zone arrays is untested, so compare one against the web app before relying on it |

## Mapping to the questions

- **Readiness**: there is no combined score here. Give the inputs (sleep, HRV, resting heart rate, form) and say that no score is available.
- **Activities in a date range**: sport, duration, load from the activity list.
- **Analysis of one activity**: the summary, plus the activity's own laps or intervals for per-km and per-rep figures (pace or power, heart rate, cadence). Time in the target range is worked out from those; when it cannot be, name it as missing.
- **Week summary**: sum hours and load per sport from the activity list. Leave monotony and the easy/hard share as missing.
- **Load state**: fitness and fatigue from the latest wellness record; form computed.

## Writes

A session review writes up to three things to its activity. All are untested against the live API: after writing, read the activity back and check that the value is there. If it is not, tell the athlete and leave the day plan as the record.

- **Effort**: the athlete's score out of 10, on the activity.
- **Review**: the whole review, appended to the activity's description under a line reading `Coach review`. Keep whatever the description already holds and put the block last: it runs from that line to the end. On a second write, replace the earlier block instead of adding another.
- **Name**: the activity's name, when the session review's "Naming" calls for it.

If the data index lists a command for any of these, run that instead.

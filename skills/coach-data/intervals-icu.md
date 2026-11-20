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
- **Analysis of one activity**: summary only. Per-rep figures need the analysis layer.
- **Week summary**: sum hours and load per sport from the activity list. Leave monotony and the easy/hard share as missing.
- **Load state**: fitness and fatigue from the latest wellness record; form computed.

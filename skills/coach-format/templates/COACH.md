# Coach data index

Every coach skill reads this file first. Written by `coach-setup`. All values in this example are invented.

## Files

| What | Path |
|---|---|
| Athlete profile | `ATHLETE.md` |
| Athlete rules | `ATHLETE-RULES.md` |
| Season plan | `SEASON-PLAN.md` |
| Month plans | `plan/months/<first Monday of the block>.md` |
| Week plans | `plan/weeks/<Monday>.md` |
| Day plans | `plan/days/<date>.md` |

## Key files (paths only, never the values)

| Service | Path |
|---|---|
| intervals.icu | `~/.intervals-icu/credentials.json` |
| Garmin | `~/.garmin/credentials.json` |

## Analysis layer commands

Each command prints JSON. A question with no command is answered from intervals.icu directly, with basic figures only.

| Question | Command |
|---|---|
| Refresh | `python tools/refresh.py --days 3 --json` |
| Readiness for a date | `python tools/readiness.py --date <date> --json` |
| Activities in a date range | `python tools/activities.py --from <date> --to <date> --json` |
| Analysis of one activity | `python tools/analyse.py --id <activity id> --json` |
| Week summary | `python tools/week.py --monday <date> --json` |
| Load state | `python tools/load.py --json` |
| Best efforts in a date range (optional) | `python tools/efforts.py --sport <sport> --from <date> --to <date> --json` |
| Food intake for a date (optional) | `python tools/food.py --date <date> --json` |
| Name an activity (optional) | `python tools/name.py --id <activity id> --json` |

## Settings

- Chat channel for approvals: Telegram
- Last setup run: 2027-01-10

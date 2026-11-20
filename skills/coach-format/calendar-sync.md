# Calendar sync

Publishing approved planned sessions to the intervals.icu calendar. intervals.icu forwards them to the watch itself, for the next seven days.

## Who does what

| Skill | Publishes | Looks for calendar differences |
|---|---|---|
| `coach-plan-week` | the whole week, Monday to Sunday, in one go, after approval | before it publishes |
| `coach-adjust` | only the sessions a plan update affects: updated, added or removed | before it changes a session |
| `coach-review-week` | nothing | once a week, for published sessions still ahead |
| `coach-today` | nothing | no; it does not read the calendar, and only warns when the week plan says "not synced" |

## Publishing

1. **Check approval.** The week plan's status is `APPROVED`, or the plan update was approved in this conversation. A `DRAFT` is never published.
2. **Build one event per planned session**: title, sport, date, duration, planned load, and the steps as workout text in `description`. Rest days, weekly targets and reasoning stay in markdown.
3. **Give each event a stable `external_id`**: `coach-<date>-<n>`, where `<n>` is the session's number in its day plan. Example: `coach-2027-02-02-1`.
4. **Send** all the events in one call: `POST /api/v1/athlete/0/events/bulk?upsert=true`. With `upsert=true` an event whose `external_id` already exists is updated in place. A plain `POST .../events` with the same `external_id` creates a second event, so every send goes through the bulk call.
5. **Read back** each event and compare it with the day plan: duration and number of steps. A mismatch means the workout text was parsed wrongly: tell the athlete which session and what intervals.icu made of it, and treat the publish as failed.
6. **Record the result** in the day plans ("Calendar: published (event <id>)") and in the week plan header: `Calendar sync: last successful publish <date time>`, or `Calendar sync: not synced` on failure. A failed publish leaves the week `APPROVED`; sending again is safe.

Done when every planned session of the scope has an event that reads back as planned, or the week plan says "not synced" and the athlete has been told why.

## Whose events

- An event is the suite's own when its `external_id` starts with `coach-`. `external_id` is returned when an event is read.
- Change and remove only the suite's own events.
- Everything else on the calendar (races, notes, sessions added by hand) is planning context: read it, leave it.
- An event on a past day, or one already paired with an activity, stays as it is.

## Calendar differences

A calendar difference is a published session that differs in intervals.icu from the markdown plan.

1. Show the athlete both versions.
2. Ask which stands: take the calendar's version into the plan, or restore the plan's version.
3. Hand the answer to `coach-adjust`, which carries out either one: the first as a plan update logged in "Changes", the second as a re-publish.

Until the athlete answers, both sides stay as they are.

## Pool swims

Publish them like any other session. Their export to the watch has open bugs, and distance steps are where workout text is least certain, so the read-back in step 5 matters most here.

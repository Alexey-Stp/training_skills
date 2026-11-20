# Plan format (shared skill)

The skill's name is not decided; see the open points in the [README](../README.md).

## Purpose

Tell every skill that writes a plan file how the file is laid out, how a planned session is written, how calendar sync is carried out, and what the suite's terms mean.

## Triggers

Called by other skills only: any skill that reads or writes a month, week or day plan, and any skill that publishes to the calendar.

## Reads

- The templates, kept as sibling files of the skill. They are the six files in [examples/](../examples/), with the layouts described in [data-folder.md](../data-folder.md).
- The existing plan file being changed.

## Writes

Nothing itself. It governs what the calling skills write.

## Steps

### Files

- Paths, sections, status and how far ahead each plan is written are set out once, in [data-folder.md](../data-folder.md). The skill follows that page and the templates. ([plan files][t10])
- Tables are fine in files. Messages to the chat channel are separate, short and table-free. ([file templates][t24])
- Commit to the workspace's local repository after each write. ([private training data][t8])

### A planned session

The fixed fields and the workout steps are listed under "Day plan" in [data-folder.md](../data-folder.md).

Pace targets need the sport's threshold pace to be set in intervals.icu. ([intervals.icu API][t2])

### A plan update

Rewrite the affected day plans so they show the current plan cleanly, and append one entry to the week plan's Changes, in the form given under "Week plan" in [data-folder.md](../data-folder.md).

### Calendar sync

From [calendar sync][t13] and [intervals.icu API][t2].

- Publish only after approval.
- One workout event per planned session: title, sport, duration, planned load, and the workout text in the event's `description`. Events are sent through `POST /athlete/{id}/events` and `/events/bulk`. Sending `workout_doc` JSON is not the supported path. Rest days, weekly targets and reasoning are not published.
- A new week: the whole week, Monday to Sunday, in one go. A plan update: only the affected sessions.
- Mark every event the suite creates as its own, and edit only those. How they are marked is untested; see [unverified.md](../unverified.md).
- Never change an event on a past day, or one already paired with an activity.
- The markdown plan is the truth, but nothing is overwritten silently. When a published session differs in intervals.icu, that is a calendar difference: the skill that finds it shows it and asks the athlete to either take the change into the plan, logged in the week plan's Changes, or restore the plan's version. Either is carried out by `coach-adjust`.
- Three skills look for calendar differences: `coach-plan-week` before it publishes, `coach-adjust` before it changes a session, and `coach-review-week` once a week. `coach-today` does not, so the morning message stays short. ([map][map])
- Entries the suite did not create (races, notes, sessions added by hand) are read as planning context only.
- Record the sync state in the week plan: the time of the last successful publish, or not synced. Publishing again must create no duplicates.
- intervals.icu forwards planned sessions to the watch itself, for the next seven days. The suite never writes to Garmin.
- Pool swims are published like any other session. Their export to the watch has open bugs.

### Vocabulary

From the [map][map]. The skill carries, with their definitions, the terms that appear in files and messages. They are taken from [`GLOSSARY.md`](../../GLOSSARY.md), which stays in this repo as the editors' reference and is not loaded at runtime:

athlete, sport mode, focus, planned session, activity, session review, day plan, week plan, month plan, plan update, athlete profile, athlete rules, coaching rules, daily check, readiness verdict, week review, subjective log, calendar sync, approval.

## Reply shape

None. It answers the calling skill, not the athlete.

## Must never

- Let a skill publish a DRAFT.
- Let a skill edit a calendar entry the suite did not create.
- Put a key anywhere but its key file, or private training data into this public repo.

## Source tickets

[Plan files][t10], [calendar sync][t13], [file templates][t24], [intervals.icu API][t2], [private training data][t8], [subjective log][t23].

[t2]: https://github.com/Alexey-Stp/training_skills/issues/2
[t8]: https://github.com/Alexey-Stp/training_skills/issues/8
[t10]: https://github.com/Alexey-Stp/training_skills/issues/10
[t13]: https://github.com/Alexey-Stp/training_skills/issues/13
[t23]: https://github.com/Alexey-Stp/training_skills/issues/23
[t24]: https://github.com/Alexey-Stp/training_skills/issues/24
[map]: https://github.com/Alexey-Stp/training_skills/issues/1

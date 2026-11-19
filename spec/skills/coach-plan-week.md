# coach-plan-week

## Purpose

Draft the coming week's plan, and after the athlete approves it, publish the week to intervals.icu.

## Triggers

- "plan next week", "get me a plan for the week".
- The scheduled Sunday run, after `coach-review-week`.

## Reads

- The month plan's row for the week: role, hours, planned load, per-sport volumes, key sessions, sport mode and focus.
- The previous week's "Actual vs plan" (and through it the subjective scores).
- The athlete profile: anchors and their flags, availability template and dated exceptions, limitations.
- Zones from intervals.icu.
- The coaching rules and athlete rules.
- The intervals.icu calendar for the week: races, notes and sessions added by hand, as context only.

## Writes

- A DRAFT week plan and its seven day plans. ([plan files][t10])
- After approval: status APPROVED, then calendar sync, then the sync state in the week plan. Commits after each write.

## Steps

1. Read the inputs.
2. Build the week within the limits and defaults of the coaching rules, with the athlete rules overriding. ([coaching method][t11])
3. Where judgement is used (sport split, which sport carries the hard sessions) or a default is departed from, write which and why under "Why this week looks like this".
4. Prescribe only from the latest tested anchor. Flag any anchor that is estimated or more than eight weeks old where it is used. ([athlete profile contents][t9])
5. Write each planned session into its day plan with the fixed fields and the workout steps in intervals.icu workout text.
6. Add any routine from the athlete rules as a one-line reminder.
7. Show the draft and wait for approval. A scheduled run leaves the draft and asks for approval in the chat channel.
8. On approval, publish the whole week, Monday to Sunday, in one go: one workout event per planned session. Rest days, targets and reasoning stay in markdown. ([calendar sync][t13])
9. Record the sync state. If publishing fails, the week stays APPROVED and is marked not synced; running the publish again is safe.

Next week's draft exists from Sunday. ([plan files][t10])

## Reply shape

Not prototyped; see the open points in the [README](../README.md). The decided constraints: the week day by day, the reasoning, then a request for approval. The file it produces is shown in [the example week plan](../examples/plan/weeks/2027-02-01.md).

## Must never

- Publish anything before approval.
- Plan past a limit without the athlete's explicit say-so.
- Make up load missed in an earlier week.
- Edit a calendar entry the suite did not create.
- Write to Garmin directly.
- Change the athlete profile.

## Source tickets

[Skill list][t7], [plan files][t10], [coaching method][t11], [sport mode][t12], [calendar sync][t13], [athlete profile contents][t9], [file templates][t24].

[t7]: https://github.com/Alexey-Stp/training_skills/issues/7
[t9]: https://github.com/Alexey-Stp/training_skills/issues/9
[t10]: https://github.com/Alexey-Stp/training_skills/issues/10
[t11]: https://github.com/Alexey-Stp/training_skills/issues/11
[t12]: https://github.com/Alexey-Stp/training_skills/issues/12
[t13]: https://github.com/Alexey-Stp/training_skills/issues/13
[t24]: https://github.com/Alexey-Stp/training_skills/issues/24

# coach-adjust

## Purpose

Make a plan update: change an existing plan in response to what actually happened or a change in the athlete's circumstances.

## Triggers

- "I missed it", "I'm tired", "I'm sick", "move Thursday", "I'm travelling next week".
- An offer accepted from `coach-today` (modify or skip), `coach-review-session` (its Next line) or `coach-setup` (an anchor changed).

## Reads

- The current week plan and the affected day plans.
- The reason the athlete gives, and the recent subjective log.
- Load state and recent activities, through the training data skill.
- The coaching rules and athlete rules.
- The current state of the affected events in intervals.icu.

## Writes

After approval only, then commits:

- The affected day plans, rewritten to show the current plan cleanly.
- One entry in the week plan's Changes section: when, what changed from what to what, and why. ([plan files][t10])
- Calendar sync for the affected sessions only: updated, removed or added. ([calendar sync][t13])
- Any score the athlete mentions ("tired", "sore"), in the day plan's subjective log. ([subjective log][t23])

## Steps

1. Establish the reason and which days are affected.
2. Apply the coaching rules ([coaching method][t11], [best-practice coaching][t5]):
   - Missed sessions are never made up.
   - After a gap of 1 to 3 days, continue; 4 to 7, treat it as the recovery week; 8 to 14, repeat the last loading week; 15 or more, step back a phase. This is a coaching convention.
   - Fever or systemic symptoms: no training. Return with easy sessions only. The skill does not diagnose.
   - No hard days back to back; the long-run cap and weekly run volume rule still hold.
3. Show the change as before and after for each affected day, and wait for approval. A scheduled run leaves a draft and asks in the chat channel.
4. On approval, rewrite the day plans, add the Changes entry, and sync only the affected sessions.
5. Never change a session on a past day, or one already paired with an activity.

Calendar differences. When a published session differs in intervals.icu from the markdown plan, the next skill that runs shows the difference and asks the athlete to either take the change into the plan, logged in Changes, or restore the plan's version. Nothing is overwritten silently. ([calendar sync][t13])

Sport mode and focus can change inside a block only through this skill, as an approved plan update with the reason logged, for example an injury that stops running. ([sport mode][t12])

## Reply

Not prototyped; see the open points in the [README](../README.md). The decided constraints: before and after of the changed days, then a request for approval. The logged result is shown under "Changes" in [the example week plan](../examples/plan/weeks/2027-02-01.md).

## Must never

- Write a change before approval.
- Add load to make up for a missed session.
- Touch a past day, a session already paired with an activity, or a calendar entry the suite did not create.
- Overwrite a difference in intervals.icu silently, in either direction.
- Edit the athlete profile.

## Source tickets

[Skill list][t7], [plan files][t10], [calendar sync][t13], [coaching method][t11], [best-practice coaching][t5], [sport mode][t12], [subjective log][t23], [today skill][t20], [everyday athlete usage][t4].

[t4]: https://github.com/Alexey-Stp/training_skills/issues/4
[t5]: https://github.com/Alexey-Stp/training_skills/issues/5
[t7]: https://github.com/Alexey-Stp/training_skills/issues/7
[t10]: https://github.com/Alexey-Stp/training_skills/issues/10
[t11]: https://github.com/Alexey-Stp/training_skills/issues/11
[t12]: https://github.com/Alexey-Stp/training_skills/issues/12
[t13]: https://github.com/Alexey-Stp/training_skills/issues/13
[t20]: https://github.com/Alexey-Stp/training_skills/issues/20
[t23]: https://github.com/Alexey-Stp/training_skills/issues/23

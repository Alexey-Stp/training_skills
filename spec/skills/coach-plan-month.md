# coach-plan-month

## Purpose

Draft the next block of whole weeks, normally four, between the athlete's season plan and the week plans.

## Triggers

- "plan the next block".

## Reads

- The season plan: the phase, key dates and tests for the period. The season plan is athlete-maintained; this skill only reads it.
- The athlete profile: goals and target races, default sport mode, availability exceptions, limitations.
- The previous block's weeks and their "Actual vs plan".
- Load state, through the training data skill.
- The coaching rules and athlete rules.

## Writes

- A DRAFT month plan at `plan/months/<first Monday of the block>.md`.
- After approval: status APPROVED. Commits after each write.

It publishes nothing to the calendar. Weeks are published by `coach-plan-week`.

## Steps

1. Take the phase from the season plan. ([coaching method][t11])
2. State the sport mode and the focus for the block. They can change at a block boundary. ([sport mode][t12])
3. Decide the block shape. With nothing else to go on, use the block-shape default in the [coaching rules](coaching-rules.md) and label it as convention. An athlete rule on the topic wins.
4. Set each week's role, hours, planned load, per-sport volumes and key sessions, and any test.
5. Apply what the phase shifts, as listed under "Phase" in the [coaching rules](coaching-rules.md).
6. Write the reasoning and the block's checks.
7. Show the draft and wait for approval.

The next block is drafted during the current block's last week. ([plan files][t10])

## Reply shape

Not prototyped; see the open points in the [README](../README.md). The decided constraints: the block's structure week by week, the reasoning, then a request for approval. The file it produces is shown in [the example month plan](../examples/plan/months/2027-01-18.md).

## Must never

- Edit the season plan or the athlete profile.
- Publish to the calendar.
- Present a convention (three-to-one weeks, the easy-week percentage) as evidence.
- Use a fitness, fatigue or form figure as a target.

## Source tickets

[Skill list][t7], [plan files][t10], [coaching method][t11], [sport mode][t12], [best-practice coaching][t5], [file templates][t24].

[t5]: https://github.com/Alexey-Stp/training_skills/issues/5
[t7]: https://github.com/Alexey-Stp/training_skills/issues/7
[t10]: https://github.com/Alexey-Stp/training_skills/issues/10
[t11]: https://github.com/Alexey-Stp/training_skills/issues/11
[t12]: https://github.com/Alexey-Stp/training_skills/issues/12
[t24]: https://github.com/Alexey-Stp/training_skills/issues/24

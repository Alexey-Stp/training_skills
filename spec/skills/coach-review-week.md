# coach-review-week

## Purpose

Assess a finished week: what was done against what the week plan prescribed. It also carries the status check, the answer to "am I on track", which has no skill of its own.

## Triggers

- "how was my week".
- The scheduled Sunday job, which calls this skill and then `coach-plan-week`.

## Reads

- The week plan, including its Changes section, and the week's seven day plans: planned sessions, readiness verdicts, subjective logs and session reviews.
- Week summary and load state, through the training data skill.
- The month plan's row for this week.
- The athlete profile's anchors, and the same thresholds in intervals.icu.
- The season plan's test dates.
- The intervals.icu calendar: published sessions still ahead, to check for calendar differences.
- The coaching rules and athlete rules.

## Writes

Without asking, then commits:

- "Actual vs plan" in the week plan.
- The week plan's status, set to CLOSED.

## Steps

1. Ask the training data skill to refresh, then for the week summary and load state.
2. Compare what was done against both the original plan and the final plan after its Changes. ([plan files][t10])
3. Count each planned session with no activity as missed and show it. Never suggest making it up. ([map][map])
4. Report hours and load per sport, with run load on its own, and the easy/hard share. In single-sport mode, activities in other sports count in total load and are shown as unplanned. ([coaching method][t11], [sport mode][t12])
5. Show fitness, fatigue and form as context only.
6. Summarise the week's subjective scores and flag trends, for example pain rising three days running. ([subjective log][t23])
7. Give the status check: whether the athlete is on track for the goal, with dated evidence from recent weeks of load and wellness. ([everyday athlete usage][t4], [skill list][t7])
8. Check published sessions that are still ahead for calendar differences, as set out under "Calendar sync" in [plan format](plan-format.md). Show any, and offer `coach-adjust` to settle them. ([map][map])
9. Suggest running `coach-setup`, without running it, when ([athlete setup flow][t25]):
   - a threshold in intervals.icu differs from the athlete profile;
   - an anchor is more than eight weeks old;
   - a test date in the season plan has passed.
10. Write "Actual vs plan" and close the week.

`coach-plan-week` reads the subjective scores through this review, not directly.

## Reply shape

Not prototyped; see the open points in the [README](../README.md). The decided constraints: totals, compliance, flags, no tables in chat. ([everyday athlete usage][t4], [file templates][t24])

## Must never

- Change a plan or the calendar.
- Run `coach-setup` or edit the athlete profile.
- Treat fitness, fatigue or form figures as a target or a prediction.
- Suggest making up missed load.

## Source tickets

[Skill list][t7], [plan files][t10], [coaching method][t11], [subjective log][t23], [athlete setup flow][t25], [training data contract][t21], [sport mode][t12], [everyday athlete usage][t4].

[t4]: https://github.com/Alexey-Stp/training_skills/issues/4
[t7]: https://github.com/Alexey-Stp/training_skills/issues/7
[t10]: https://github.com/Alexey-Stp/training_skills/issues/10
[t11]: https://github.com/Alexey-Stp/training_skills/issues/11
[t12]: https://github.com/Alexey-Stp/training_skills/issues/12
[t21]: https://github.com/Alexey-Stp/training_skills/issues/21
[t23]: https://github.com/Alexey-Stp/training_skills/issues/23
[t24]: https://github.com/Alexey-Stp/training_skills/issues/24
[t25]: https://github.com/Alexey-Stp/training_skills/issues/25
[map]: https://github.com/Alexey-Stp/training_skills/issues/1

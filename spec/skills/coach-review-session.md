# coach-review-session

## Purpose

Assess one activity against its planned session, where one exists, and say what it means for the days ahead.

## Triggers

- "review my run", "review today's training".
- The scheduled midday and evening jobs.

## Reads

- The day plan for the activity's date: the planned session and the subjective log.
- Analysis of the activity, through the training data skill.
- The coaching rules and athlete rules.

## Writes

Without asking, then commits:

- The session review, in the day plan under "Session reviews".
- The effort score, in the day plan's subjective log and on the matching activity in intervals.icu.
- The coach's note, a form of the review in plain sentences with the time in zones, to the activity's description in intervals.icu.
- The activity's name, only if the data index lists the optional naming question.

## Steps

1. Ask the training data skill to refresh, then find the activity and its planned session.
2. If the athlete has not given an effort score, ask once for effort out of 10. With no answer, continue without it.
3. Judge the activity against the planned session's purpose and give one of three verdicts: done as planned, partly, not as planned.
4. An activity with no planned session gets no verdict: say what it was and what it cost. In single-sport mode an activity in another sport is treated this way and shown as unplanned. ([sport mode][t12])
5. Give two to four findings, each with the figure behind it.
6. Add one "Next" line. It advises only. If a coming planned session should change, say so and point to `coach-adjust`.
7. Write the review and post the short version.

A planned session with no activity ([map][map]):

1. Refresh.
2. If there is still nothing, ask once whether it was skipped or has not synced.
3. Record the answer in the day plan. A skipped session is counted as missed and is not to be made up.

If the activity comes back as an empty stub, the training data skill's fallback applies. Never review from empty data. ([activity source resilience][t15])

Figures ([session review][t14]):

| Always | Run adds | Bike adds | Swim adds |
|---|---|---|---|
| duration, load, time in the target range, effort | pace and heart rate per rep | power per interval, heart-rate drift | pace per 100 m per set |

Anything else appears only when it explains a finding.

## Reply shape

In this order: verdict line with the session name; planned versus actual for the main set; how much of the purpose was achieved; the findings; the Next line. Phone-sized, no tables. Sample with invented numbers; the same review as stored is in [the example day plan](../examples/plan/days/2027-02-02.md):

```
Threshold run: PARTLY DONE AS PLANNED

Planned 4 x 8 min at 4:10/km. Did 4 x 8 min at 4:09, 4:10, 4:12, 4:21.
Purpose (time at threshold): 24 of 32 min in the target range.

- Reps 1 to 3 on target, heart rate steady.
- Rep 4 slowed 11 s/km while heart rate rose 6 bpm: past threshold, not at it.
- Load 78 planned, 74 done. Effort reported: 8/10.

Next: Thursday's easy run stands. If rep 4 fades again next week,
shorten to 3 x 8 before adding volume.
```

## Must never

- Change a plan or the calendar.
- Give a verdict to an unplanned activity.
- Suggest making up a missed session.
- Ask for effort more than once per activity.
- Review an activity from empty or missing data.

## Source tickets

[Session review][t14], [training data contract][t21], [subjective log][t23], [sport mode][t12], [activity source resilience][t15], [everyday athlete usage][t4].

[t4]: https://github.com/Alexey-Stp/training_skills/issues/4
[t12]: https://github.com/Alexey-Stp/training_skills/issues/12
[t14]: https://github.com/Alexey-Stp/training_skills/issues/14
[t15]: https://github.com/Alexey-Stp/training_skills/issues/15
[t21]: https://github.com/Alexey-Stp/training_skills/issues/21
[t23]: https://github.com/Alexey-Stp/training_skills/issues/23
[map]: https://github.com/Alexey-Stp/training_skills/issues/1

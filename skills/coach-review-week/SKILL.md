---
name: coach-review-week
description: Use when the athlete asks how their week was or is going, or whether they are on track ("how was my week", "am I on track"), and for the scheduled Sunday job before the next week is planned. Gives the week review.
---

# Week review

Assesses a finished week: what was done against what the week plan prescribed. It also gives the status check, the answer to "am I on track".

The review reports. Plans change through `coach-adjust`, the athlete profile through `coach-setup`.

## Which review is this

- The week is over (Sunday evening or later): **full review**. It writes "Actual vs plan" and closes the week.
- The week is still running: **progress so far**. Same steps with figures up to today against whole-week targets; sessions not yet due are listed as still ahead, never as missed. The message says "so far", and nothing is written or closed.
- The week is already `CLOSED`: give the stored "Actual vs plan" as the message and write nothing. The scheduled job stays silent and goes on to `coach-plan-week`.

## Steps

1. **Load.** Use `coach-data` to find the data folder and refresh. Read the week plan with its "Changes", the week's seven day plans (planned sessions, readiness verdicts, "How I felt", session reviews), this week's row in the month plan, and the season plan's test dates. Load the rules through `coach-rules`.
2. **Get the figures** from `coach-data`: the week summary and the load state.
3. **Compare** what was done against two plans: the week as first approved, and the week as it stood after its "Changes". Say both where they differ.
4. **Count the sessions.** Each planned session is done, partly done, or missed. A planned session with no activity is missed, and is shown as missed. Missed load stays missed: the review proposes no make-up, this week or next. The one exception, while the week is still running, is the single move the "Missed session" limit in `coach-rules` allows for a key session or a test. If the athlete asks for one, say that it stays missed and that next week is planned on its own terms.
5. **Totals.** Hours and load per sport against target, run load on its own line, and the share of easy and hard sessions among swim, bike and run, with strength left out of the count and hard swims shown on their own. Count by the rule in `coach-rules` from what was done; where the week summary's counts differ, give the rule's count and name the difference. In single-sport mode, activities in other sports count in total load and are shown as unplanned.
6. **Subjective log.** Summarise the week's scores and flag a trend, for example a pain score rising three days running, or effort high on easy days.
   **Limits.** Check every session that was done against the limits in `coach-rules` and in `ATHLETE-RULES.md`, using that day's scores. Report each limit that was passed, plainly, with the day and the figure, and the hard-session cap or the hard-swim count when the week went over it, unplanned activities included. Do the same for the block's checks in the month plan.
7. **Load state.** Give fitness, fatigue and form in one line, as context. They explain; they are not goals.
8. **Status check.** Say whether the athlete is on track for the goal the current block serves (with several goals in the profile, the one matching the block's focus; name it): on track, behind, ahead, or not settled. Start from the goal: what it needs (the pace or power the goal time implies against the current anchor, the race's distance against the longest run and ride done) and the weeks left to the race. Recent weeks of load and the subjective log support the answer; they do not make it. Give two or three dated facts. If the goal has no time, or the anchor is estimated or more than 8 weeks old, say that the evidence does not settle it and name the test for that anchor.
9. **Calendar differences.** Check published sessions still ahead, as [calendar sync](../coach-format/calendar-sync.md) in `coach-format` describes. Show any difference and offer `coach-adjust`.
10. **Suggest `coach-setup`**, without running it, when any of these holds:
    - a threshold in intervals.icu differs from the athlete profile;
    - an anchor is more than 8 weeks old;
    - a test date in the season plan has passed;
    - the week's MODIFY verdicts from the band alone reach the count under "Readiness" in `coach-rules`: the readiness bands may be set too high for this athlete.
11. **Write** (full review only), without asking, then commit: "Actual vs plan" in the week plan, and the week's status to `CLOSED`. The status line reads `Status: CLOSED (<date time>)`. If this was the last week of its block, also write the month plan's "Block review" and set the month plan to `CLOSED`: per week, planned against done hours, load and volume; key sessions done or not; each block check met or passed; missed sessions; any test result. A week of the block with no "Actual vs plan" is named as not reviewed.
12. **Send** the message in the shape below.

Done when the week plan holds "Actual vs plan" and is closed, and the athlete has the message; for progress so far, when the athlete has the message.

`coach-plan-week` reads the week's subjective scores through this review.

## Actual vs plan

In the file, a table is right. One row per sport and a total: planned hours and load (as first approved, and after changes when different), done hours and load. Below it: sessions done, partly done and missed, by name; the flags and any limit passed; monotony and ramp; the status check; any suggestion made.

## Message shape

Short enough for a phone screen, plain lines, no tables. In this order: one line for the week as a whole; totals; sessions; flags, limits passed first; load state; status check; what is suggested. When the block has ended, add one last line saying so with its headline.

```
Week 1 to 7 Feb: 9:10 of 9:45 h, load 505 of 528.

As first approved: 10:00 h, load 540.

Run 4:55 of 5:10, load 318 of 330. Bike 2:15 of 2:15, load 117 of 118. Swim 1:40 of 1:40. Strength 0:20 of 0:40.
10 sessions: 8 done, 1 partly, 1 missed. Partly: Tue threshold run. Missed: Tue strength.
Easy/hard: 5 easy, 2 hard, 1 hard swim; strength not counted.

Flags
- Limit passed: Sat long run, 26 km with knee at 2. Your rule at 2 or 3 is easy, flat, 45 min at most.
- Knee pain rose Tue to Thu, 1 to 3, and stayed at 3 on Fri.
- Wed bike was cut from 75 to 60 min after a MODIFY verdict.

Fitness 62, fatigue 71, form -9: context, the week was a load week.

On track for the half marathon, 35 weeks out: goal pace 4:30/km against threshold 4:10/km (tested 20 Dec), long run 26 km done on 6 Feb. Run load up three weeks running; threshold reps still fade on rep 4.

Suggest: run setup. Run threshold in intervals.icu (4:05) differs from your profile (4:10).
```

## Boundaries

- Every figure comes from the week summary, the load state, the plans or the day plans. One that is missing is named as missing.
- Fitness, fatigue and form are reported, never offered as a target or a forecast of performance.
- This skill writes two things to the week plan and, at a block's end, two to the month plan. Planned sessions, the calendar and the athlete profile are left as they are.

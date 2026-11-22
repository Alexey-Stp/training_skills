---
name: coach-race
description: Use when the athlete asks to be prepared for a race or what to do before one ("prepare me for my 10k", "I entered a race", "it's race week", "what do I do the day before"), asks which of several races should be A, B or C, or when illness or a gap falls in the three weeks before a race.
---

# Race preparation

One race, from today to its start line: which plan carries the work at this distance in time, what the plan that exists must change, and what the taper and race week hold by day.

Every figure is in `race-prep.md` in `coach-rules`, with "Races" in `coach-rules` and its `season.md`. Read them in this run before proposing anything.

This skill writes no plan file. It shows the preparation, and on approval the skill that owns each file makes the change.

## Steps

1. **Load.** Use `coach-data` to find the data folder and refresh. Read the athlete profile (target races with priority, date and goal; anchors; availability; limitations), the athlete rules and "Races" through `coach-rules`, `season.md` and `race-prep.md` in `coach-rules`, the season plan, the month plans and week plans from today to the race, and from `coach-data` the load state and the activities of the last 8 weeks.
2. **Settle the race.** The one the athlete named, or the next A or B race. A race the profile does not hold: run steps 3 and 4 for it, recommend a priority from "Choosing priorities" with the reason, and stop there until the athlete has named the priority and setup has added the race. Asked only which race should be A, B or C: answer from "Choosing priorities" for every race in the profile and every race the athlete named, and stop.
3. **Count.** Days to race day, whole weeks to race week, and the row of "How far out" this race is in.
4. **Check the distance** as "Ready for the distance" says, for a race of 90 minutes or more.
5. **Check illness and gaps** as "Illness or a gap before a race" says, when the race is three weeks away or less.
6. **Compare** the plans that exist with what the race asks, as "The plan that already exists" says. Take from `race-prep.md` only what the row of step 3 calls for:
   - season plan: week roles and phases;
   - month plan: the load weeks left, their key sessions, the last long session, the taper weeks;
   - week and day plans: the taper by week with "Form in the taper", the last long and hard sessions, and race week by day.
7. **Show the preparation** in the shape below: what stands, what changes, and which change needs approval. Ask once for approval of the changes as a whole. Stop here.
8. **On approval, hand over**, one change at a time, in this order: the profile to `coach-setup`; the season plan to `coach-plan-season`; a block not yet drafted to `coach-plan-month`; a week not yet drafted to `coach-plan-week`; an approved month plan, and an approved or drafted week, to `coach-adjust`. Each of them shows its own before and after and takes its own approval. Say which changes are done and which are still waiting.

Done when the athlete has the preparation with every difference listed and each one either changed by its skill or named as waiting; or, with no difference, has been told that the plans already fit the race, with the days that matter.

## Message shape

The race first: name, date, days to go (whole weeks to race week when it is more than 21 days), priority, goal. Then what the plans already hold, what changes, and the days that matter. Plain lines, no tables, short enough for a phone screen.

Samples with invented numbers. Race week, for an A race:

```
Olympic-distance triathlon, Sun 18 Jul: 6 days to go, A race, goal under 2:40.

This week is planned as a load week: 9:30 h with two hard sessions. For race week it should be about 3:50 h before the race, 60% under your last two load weeks.
Form is -18 today (fitness 68). By convention the short hard session is cut to 8 min of work; the openers stay.

Mon easy swim 30 min
Tue easy ride 50 min
Wed run 40 min with 2 x 4 min at race pace
Thu easy swim 30 min, easy ride 20 min
Fri rest (your rule)
Sat openers: 15 min swim, 30 min ride with 5 pickups of 20 s that also checks the bike, optional 10 min run
Sun race

Your rule makes Saturday the long run day. I recommend the openers; keeping the rule would be a 35 min run in their place. Which?
Food from Friday: ask for the nutrition target. What to expect on the day: ask for a prediction.

Approve, and I change this week through a plan update.
```

A race further out:

```
10 km road race, Sun 6 Jun: 16 weeks to race week, B race, goal under 43:00.

The season plan already holds it: race week 31 May after three load weeks, at about 70% of the week before.
Nothing changes now. The load weeks before it hold threshold reps, with reps at 10 km pace from 19 Apr.
```

## Boundaries

- A limit of `coach-rules` or of the athlete is not stretched for a race: the long-run limit, the fever limit and its return, every athlete limit.
- Whether to start a race is the athlete's decision.
- Pacing on the day comes from the race's planned session, and the expected time from `coach-predict`.
- Nothing is published to the calendar by this skill.

---
name: coach-race
description: Use when the athlete asks to be prepared for a race or what to do before one ("prepare me for my 10k", "I entered a race, prepare me", "it's race week", "what do I do the day before the race"), asks which of several races should be A, B or C, or when illness or a gap falls in the three weeks before an A or B race.
---

# Race preparation

One race, from today to its start line. The athlete asks once and gets the prepared plan for the stretch that matters now: the season's weeks when the race is far, the block when it is weeks away, the days when it is inside its taper.

Every figure is in `race-prep.md` in `coach-rules`, with "Races" in `coach-rules` and its `season.md`. Read them in this run before proposing anything.

## Steps

1. **Load.** Use `coach-data` to find the data folder and refresh. Read the athlete profile (target races with priority, date and goal; anchors; availability; limitations), the athlete rules and "Races" through `coach-rules`, `season.md` and `race-prep.md` in `coach-rules`, the season plan, the month plans and week plans from today to the race, and from `coach-data` the load state and the activities of the last 8 weeks.
2. **Settle the race and its priority.** The race the athlete named, or the next A or B race. Recommend priorities as "Choosing priorities" says: for a race the profile does not hold, and for every race when the athlete asks which should be A, B or C. Asked only that, show the recommendation, record it through setup on the athlete's "ok", and stop.
3. **Count** as "How far out" says, and take the row this race is in.
4. **Check** "Ready for the distance", and "Illness or a gap before a race" where it applies.
5. **Compare** the plans that exist with what the race asks, as "The plan that already exists" says.
6. **Prepare the plan** for the row of step 3, taking from `race-prep.md` only what that row settles:
   - **Season plan row.** Where the season plan does not hold the race's weeks, run `coach-plan-season` now, from the races as they will stand once setup has recorded them; its draft is the preparation.
   - **Month plan row.** Lay out the weeks to the race: each load week with its key sessions, the week of the last long sessions, the taper weeks with their cuts. A block not yet drafted: run `coach-plan-month` now, and its draft is the preparation. An approved block: show its rows as they will be, with what a row was where it changes.
   - **Week and day row.** Lay out every day from today to race day: the taper weeks with "Form in the taper" and "Rest in the taper", the last long sessions, race week by day. A week not yet drafted: run `coach-plan-week` for it now and show its draft with the rest. An approved or drafted week: show its days as they will be, with what a day was where it changes.
7. **Show it** in the shape below and ask once for approval. The athlete sees the whole plan for that stretch, not a list of differences. Stop here.
8. **On approval, have it written**, with no second ask for what was shown:
   - a new race, a priority or a goal, first: `coach-setup`;
   - approved month, week and day plans: `coach-adjust`, by its row "A race's preparation";
   - a draft from step 6: the planning skill that drafted it takes this approval as its own.

   If a calendar check or a limit changes what was shown, show that part again and ask.

Done when the plans hold what was shown and the athlete has been told so in one line; or the athlete has the prepared plan and has been asked; or, with no difference, has been told that the plans already fit the race, with the next date that matters.

## Message shape

The race first: name, date, days to go (whole weeks to race week when it is more than 21 days), priority, goal. Then the plan for the stretch, by week or by day. Then what changes against the plan that exists, any clash with an athlete rule, and the ask. Plain lines, no tables, short enough for a phone screen.

Samples with invented numbers. An A race in race week:

```
Olympic-distance triathlon, Sun 18 Jul: 6 days to go, A race, goal under 2:40.

Race week should be about 3:50 h before the race, 60% under your last two load weeks. It is planned at 9:30 h with two hard sessions.
Last week was trained at 9:00 h, not as a taper week. Nothing more is cut for that.
Form is -18 today (fitness 68). By convention the short hard session is cut to 8 min of work.

Mon easy swim 40 min
Tue easy ride 65 min
Wed run 40 min with 2 x 4 min at race pace (was a hard run, 70 min)
Thu easy swim 25 min, easy ride 20 min (was a hard ride, 75 min)
Fri rest (your rule)
Sat long run 40 min (your rule: Saturday is the long run day; was 100 min)
Sun race

Saturday clashes with the day before a race, which would hold openers: 15 min swim, 30 min ride with 5 pickups of 20 s, optional 10 min run. Say "openers" and Saturday becomes that.
Sleep is part of the taper: your usual hours or more, every night this week.

Approve, and this week is changed as shown.
```

An A race in the block:

```
Half-distance triathlon, Sun 5 Sep: 4 weeks to race week, A race, goal under 5:30.

Ready for the distance: longest ride 2:15, the race asks 2:10; longest run 15 km, the race asks 14.8.

2 Aug load: long ride with blocks at race power and race fuelling; brick off it
9 Aug load: long ride with blocks at race power and race fuelling
16 Aug load: the longest ride and run, by Sun 22 Aug; brick
23 Aug taper: 41% under your last two load weeks
30 Aug race week: 60% under; race Sun 5 Sep

The month plan has 16 Aug as an easy week and 23 Aug as a load week. Those two change; the rest stands.

Approve, and the month plan is changed as shown.
```

A race far out:

```
10 km road race, Sun 6 Jun: 16 weeks to race week, B race, goal under 43:00.

The season plan already holds it: race week 31 May after three load weeks.
Nothing changes now. Its block is drafted in May.
```

## Boundaries

- A limit of `coach-rules` or of the athlete is not stretched for a race.
- An athlete rule stands until the athlete says otherwise in this conversation.
- Whether to start a race is the athlete's decision.
- Pacing on the day comes from the race's planned session, and the expected time from `coach-predict`.

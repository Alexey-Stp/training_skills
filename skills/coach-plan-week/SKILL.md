---
name: coach-plan-week
description: Use when the athlete asks for next week's training plan ("plan next week"), and for the scheduled Sunday job after the week review. Drafts the coming week, and publishes it to the calendar once the athlete approves.
---

# Week planning

Drafts the coming week's plan and, after the athlete approves it, publishes the week to intervals.icu.

Two states, kept apart: a **draft** is written to the files at once; the **calendar** is touched only after approval.

## Steps

1. **Load.** Use `coach-data` to find the data folder. Read:
   - the month plan: sport mode, focus, checks, and this week's row (role, hours, planned load, per-sport volumes, key sessions);
   - last week's "Actual vs plan", which carries that week's flags and subjective scores;
   - the athlete profile: anchors with their flags, the availability template and dated exceptions, limitations, and any target race in this week, the two before it or the two after it;
   - zones, from intervals.icu;
   - the intervals.icu calendar for the week, as context: races, notes, sessions added by hand;
   - the rules, through `coach-rules`.

   If last week has no "Actual vs plan", say so and offer `coach-review-week` first; plan without it only if the athlete says to.
   If a `DRAFT` for the week already exists, show that draft again instead of writing a new one, unless the athlete asks for a fresh one.
2. **Frame the week.** Take role and targets from the month plan's row. Where last week's review gives a reason to depart from it (a limit passed, a pain trend, missed key sessions), depart and say why. Missed load from an earlier week is not added, and load taken out of one sport for a limit is not moved to another. A percentage "of the previous week" is of that week's planned load as first approved.
3. **Place the sessions**, day by day:
   - inside each day's available time and facility access, with dated exceptions applied;
   - where a limit depends on a score the athlete gives on the day (a pain score), plan to the latest known score. If that shortens the week, say so under "Why", and say that the sessions can grow through `coach-adjust` if the score improves;
   - following the weekly shape in `ATHLETE-RULES.md`;
   - hard bike and run sessions about 48 hours apart and none the day after the long run, hard swims not on consecutive days, in the sport the focus names apart from the short hard set the other sports keep, within the weekly cap and the hard-swim count;
   - a race as a planned session on its day, with the days around it shaped by its priority ("Races" in `coach-rules`);
   - a brick as two sessions, the ride then the run, each naming the other in its purpose;
   - two sessions on one day in an order the day's usual times allow, the key or hard one first where they do, and a pool session with its travel time when the profile gives one;
   - strength as ordinary sessions, not the day before a key session;
   - each routine in the athlete rules as a one-line reminder, with no load.
4. **Set the targets** of each session from the latest tested anchor, and write the session's `Anchors:` line as `coach-format` says, for targets and caps alike; a cap set by an athlete rule gets no entry. Estimate planned load as the "Targets" default in `coach-rules` says. A swim gets a `Sets:` line, and a session the fuelling default covers a `Fuel:` line (see "A planned session" in `coach-format`). Where an anchor in use is estimated or more than 8 weeks old, say so beside the session. Percentage steps in workout text are worked out by intervals.icu from its own thresholds: if one of those differs from the profile, flag it in the message and suggest `coach-setup` before approval. A cap that workout text cannot carry (for example a heart-rate cap on an easy run) goes in the session's "Caps" field.
5. **Check the draft** before showing it. Each line gets an answer:
   - every limit in `coach-rules` and `ATHLETE-RULES.md`: met, with the figure (for the long run: the distance, the longest in the last 30 days, the percentage, its duration and its share of the week's run volume against the ceiling);
   - hard sessions counted by the rule: bike and run against the cap, swims against the hard-swim count;
   - every default: followed, or the departure named with its reason;
   - the week matches its role in the month plan's row: an easy week has no more load than the row gives and no added hard session; a taper, race or recovery week is shaped as "Races" and "Week roles" under "Season" in `coach-rules` say;
   - sessions add up to the week's targets per sport, in hours and planned load;
   - every day fits its availability.
6. **Write the draft**, then commit: the week plan with status `DRAFT`, and all seven day plans, in the `coach-format` templates. In a draft the header reads `Calendar sync: draft, nothing published` and each session `Calendar: draft`. Each planned session has its fixed fields and its steps in workout text. "Why this week looks like this" holds the reasoning, every use of judgement (sport split, which sport carries the hard sessions) and every departure. "Checks" holds the answers from step 5.
7. **Show the draft** in the message shape below and ask for approval. Stop here.
8. **On approval:** set the status to `APPROVED (<date time>)` and commit. Then publish the whole week, Monday to Sunday, following [calendar sync](../coach-format/calendar-sync.md) in `coach-format`: check for calendar differences first, send, read back, record the sync state.

Done when the week is `APPROVED` and its sync state is recorded (published, or "not synced" with the athlete told why); or when the draft is written and the athlete has been asked.

## Before approval

- **A change the athlete asks for:** revise the draft and the day plans, re-run step 5, show it again. The draft stays `DRAFT`.
- **A request that passes a limit:** name the limit and the figure, say what the most is that stays inside it, and ask whether they want to go past it. Only an explicit yes to that question counts. When it passes several, name each and ask once. When it does not fit the day's available time either, say that too; a yes to the limit does not make room.
- **"Looks good", "ok", "go"** in answer to the draft is approval. Anything else is not: silence, a question, a partial comment.

## Scheduled Sunday job

Runs after `coach-review-week`. It does steps 1 to 7: the draft is written, the message is sent to the chat channel, and it stops. Publishing waits for the athlete's answer, whenever that comes.

## Message shape

Short enough for a phone screen, plain lines, no tables. In this order: one line for the week (role, hours, load); the days, one line each; the reasoning in two or three lines; anything flagged; the request for approval.

```
Week 8 to 14 Feb, DRAFT: easy week, 6:35 h, load 319.

Mon  Swim easy 2.0 km
Tue  Run easy 45 min, flat + strength 20 min
Wed  Bike easy 90 min
Thu  Run easy 45 min, flat + swim 1.0 km + bike easy 30 min
Fri  Rest (travel)
Sat  Run easy 45 min, flat (travel)
Sun  Run easy 45 min, flat (travel)

Why: fourth week of the block, the easy one. No hard session. Fri to Sun are run-only because you are travelling.
Departure: every run is 45 min, easy and flat, and there is no long run. Your knee was at 2 today and your rule at 2 or 3 allows no more. That makes the week 6:35 h and load 319, under the month plan's 7:30 and 405. If the knee settles, the runs can grow through a plan update.

Flag: bike targets use CP from 2 Oct, older than 8 weeks.

Approve this week?
```

## Boundaries

- The calendar holds only what was approved.
- Calendar entries the suite did not create are read, and left as they are.
- The athlete profile is `coach-setup`'s. Garmin is reached only through intervals.icu.

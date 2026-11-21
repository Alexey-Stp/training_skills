---
name: coach-adjust
description: Use when an approved plan has to change because of what happened or a change in circumstances ("I missed it", "I'm tired", "move Thursday"), when the athlete is offered a session someone else organises (a group run, a club ride, a squad swim) and wants it fitted into the plan, when the athlete accepts a change offered by another coach skill, or when a calendar difference has to be settled. Makes a plan update.
---

# Plan update

Changes an existing plan in response to what actually happened or a change in the athlete's circumstances.

Every plan update is shown as before and after and waits for approval. Only a score the athlete mentions is written at once.

## Steps

1. **Log first.** If the athlete mentioned how they feel ("tired", "sore", a pain score, illness), write it under "How I felt" in today's day plan now, whatever happens to the change.
2. **Load.** Use `coach-data` to find the data folder and refresh. Read the current week plan, the affected day plans, recent "How I felt" entries, and the load state and recent activities. Load the rules through `coach-rules`.
3. **Scope.** Name the reason and the days it touches. Days in the past and sessions already paired with an activity are outside every plan update: they stay as they are. If that is all the request touches, say so, write nothing, and offer `coach-review-session` when the activity has no review. If what the athlete says happened differs from the record, say what the record shows and ask before going on.
4. **Check the calendar.** Read the affected published sessions in intervals.icu. If one differs from the plan, settle that first: see "Calendar differences".
5. **Work out the change** with the rules. The ones that matter most here:
   - A missed session's load is not added elsewhere. An easy one stays missed; a key session or a test, missed or eased by a readiness verdict before it started, may move once inside its week when every rule holds on the new day (the "Missed session" limit in `coach-rules`).
   - Hard bike and run days about 48 hours apart and none the day after the long run, hard swims not on consecutive days; the long run within 110% of the longest in the last 30 days, with its floor and ceiling.
   - A race keeps what its priority gives it before and after ("Races" in `coach-rules`).
   - Every limit and weekly-shape rule in `ATHLETE-RULES.md`.
   - After a gap in training, the gap default in `coach-rules`.
   - Change as little as the reason needs.
6. **A request that passes a limit, one of the athlete's own rules under any heading, or a check in the month plan:** show the change they asked for as before and after, name each rule it passes with the figure, say what the most is that stays inside them, and ask once whether they want to go past. An explicit yes to that question approves the change shown. This includes moving a missed session. A change that does not fit a day's available time is said to not fit; a yes does not make room.
7. **Show the change** as before and after for each affected day, with the effect on the week's targets, in the message shape below. Ask for approval. Stop here. Accepting another skill's offer ("yes, change it") starts this skill; it does not approve a change nobody has shown yet.
8. **On approval,** in this order, then commit:
   1. Rewrite each affected day plan so it shows the current plan cleanly. A session keeps its number on its day, and one moved to another day is renumbered; see "A planned session" in `coach-format`.
   2. Append one entry to "Changes" in the week plan: when, when approved, what changed from what to what, why, and the effect on the week's targets.
   3. Update whatever else in the week plan the change made stale: the targets table, the "Days" table, "Checks", and the month plan's row for the week when its figures or key sessions changed.
   4. Sync only the affected sessions (updated, added or removed), following [calendar sync](../coach-format/calendar-sync.md) in `coach-format`.

Done when the day plans, "Changes" and the calendar agree and the athlete has been told; or when the before and after has been shown and the athlete has been asked.

## Kinds of update

| What happened | What the update does |
|---|---|
| A readiness verdict of MODIFY or SKIP, accepted | Today's sessions change as the verdict said. A key session or test the verdict eased may move once to a later day of the week, as the "Missed session" limit allows; that day's easy session of the same sport comes to the verdict's day or is dropped. Other days stand unless a rule forces more. |
| A session fell short or was missed | Nothing is added. A missed key session or test may move once inside its week, as the "Missed session" limit allows. A later session changes only if the review's Next line said it should. |
| The athlete wants a session moved | Move it if every rule still holds on both days; otherwise step 6. |
| Tired, sore, ill | Ease or remove what is ahead, by the rules. Fever: no training, and the return as the limit in `coach-rules` gives it. |
| Back after a gap | Apply the gap default, labelled as a convention, to the days ahead. "Repeat the last load week" means bring this week to that week's targets with the smallest change; the block keeps its shape and its easy week. When the gap default steps back a phase, also say that the season plan's weeks no longer fit and offer `coach-plan-season`. |
| Availability changed (travel, a commitment) | Re-place the affected sessions inside the new availability; what does not fit is dropped, not squeezed in. |
| An anchor changed (from `coach-setup`, or from the daily check's anchor line) | Take every session still ahead, approved or draft, that is out of date for that anchor as "Anchors in a plan" in `coach-rules` defines it; leave today's out when today's verdict is MODIFY or SKIP. Recalculate as "Anchors in a plan" in `coach-rules` says, and rewrite the figures and the line. Re-publish a session only if its steps changed. Percentage steps follow the threshold intervals.icu holds: read it, and when it is not the new value, say that the watch shows the old figures until the athlete changes it there. |
| A session with no `Anchors:` line | The anchor value in force when the week plan was approved is the "from" value of the first change-log entry for that anchor dated after the approval, or the current value when there is none. Work out what percentages of it the figures are and write the line; where the value has changed since, recalculate as for a changed anchor. |
| A session someone else organises is offered | Choose the option that fits and swap it for the planned session: see "An outside session". |
| A sport cannot be done (injury) | Remove that sport's sessions for the period; nothing replaces them. If the focus sport is the one lost, change the focus; if only one sport is left, change the sport mode. Add a line to the month plan header: `<Sport> suspended <from> to <until> (<reason>)`. Then offer `coach-setup`, so the limitation and a dated exception reach the profile and later planning sees them. |

A change that reaches beyond the current week also updates the month plan's rows for the weeks it touches, in the same approval.

## An outside session

The athlete pastes or describes a session someone else organises, often with several distances or pace groups. Work it out inside step 5; steps 6 to 8 apply as for any update.

1. **Find what it replaces:** the planned session of the same sport on that day. With none, it is an added session, and the weekly-shape rules decide whether there is room.
2. **Read each option against the athlete,** using the anchors in the profile: what effort that pace or power would be for them (easy, steady, threshold, harder), and the distance or duration.
3. **Recommend one option:** the one closest to the planned session's purpose, targets and caps that stays inside every rule. Part of an option counts as a choice: where the group's distance is short of the plan, say what to add at the planned effort, before or after as the day's times allow; where it is long or turns hard, say where to turn or drop off. The group part and what is added are one session and one run for every limit.
4. **If no option fits,** say so, name the nearest one and what it would pass, and recommend keeping the planned session. The athlete can still ask for an option; that goes through step 6.
5. **Check the time:** the meeting and start times against that day's availability, and against the other sessions of the day.
6. **Show it** in the message shape below, with one line before the before-and-after for the recommended option and why, and one line for each other option and why not. The athlete approves the recommendation or names another option.

The rewritten session keeps its number and purpose. Its targets carry the chosen group, distance and pace; the start time and meeting place go on a plain `Where and when:` line between the fields and the steps (see "A planned session" in `coach-format`); its steps are rewritten to match, the added part included, so the calendar copy shows the whole session.

```
Plan update: club ride offered for Sunday, start 08:30.

Recommended: B group, 70 km at 27 km/h. For you that is steady endurance, the same purpose as the planned ride.
A group, 95 km at 31 km/h: near threshold for long stretches, and Saturday is already a hard day.
C group, 45 km at 23 km/h: easy, but 50 min short of the planned duration.

Sun
  before: endurance ride 2:45, solo
  after:  endurance ride 2:35 with B group, 08:30 from the clubhouse

Week: bike 6:15 to 6:05, load 310 to 302.

Approve B group, or name another?
```

## Calendar differences

A published session that differs in intervals.icu from the plan. Whoever found it, it is settled here:

1. Show both versions and ask which stands. If the athlete is also asking for a new value for that session, ask one question with all three. A new value is a plan update from the plan's version, and its "Changes" entry notes what the calendar had shown.
2. **The calendar's version stands:** treat it as a plan update. Steps 5 to 8 apply, including the limits.
3. **The plan's version stands:** re-publish that session, read it back, record the sync. Nothing goes in "Changes", because the plan did not change.

Both sides stay as they are until the athlete answers.

## Message shape

Short enough for a phone screen, plain lines, no tables. In this order: one line naming the reason; before and after per affected day; the effect on the week; anything flagged; the request for approval.

```
Plan update: poor sleep, MODIFY verdict today.

Wed
  before: easy bike 75 min
  after:  easy bike 60 min

Week: bike 2:30 to 2:15, load 130 to 118. Total 10:00 to 9:45, load 540 to 528.
Thu to Sun stand.

Approve this change?
```

After approval and sync, confirm in one line: what changed, and that the calendar has it or that nothing needed sending.

## Boundaries

- The athlete profile is `coach-setup`'s.
- Calendar entries the suite did not create are read, and left as they are.
- Load figures (fitness, fatigue, form) inform a change; one of them alone is not the reason for it.

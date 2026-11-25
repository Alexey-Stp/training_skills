---
name: coach-review-session
description: Use when the athlete asks for a review of a completed run, ride, swim or other training ("review my run", "review today's training", "was that ride ok"), and for the scheduled midday and evening jobs. Assesses one activity against its planned session.
---

# Session review

Assesses one activity against its planned session, where there is one, and says what it means for the days ahead.

The review advises. A planned session changes only through `coach-adjust`, after approval.

## Steps

1. **Load.** Use `coach-data` to find the data folder and refresh. Find the activity, then read the day plan for its date (the planned session it belongs to, the readiness verdict and "How I felt"), and the week and month plan for the context line. Load the rules through `coach-rules`.
2. **Get the figures** from `coach-data`: the analysis of the activity, the load state, and the week summary so far. For a swim, read [swim.md](swim.md) now. An empty stub is not reviewed: `coach-data` handles it, the day plan gets one line under "Session reviews" saying the review is waiting on real figures, and the athlete is told.
3. **Effort.** If the day plan has no effort score for this activity, the review goes out with `effort not given` and ends with one question asking for effort out of 10. That is the one ask for this activity, whoever asks it. When the answer comes, write it under "How I felt" in the day plan, on the activity in intervals.icu and in the review's load line, and confirm in a line.
4. **Verdict.** Judge the activity against the planned session's *purpose* and give one of three:
   - `DONE AS PLANNED`
   - `PARTLY DONE AS PLANNED`
   - `NOT DONE AS PLANNED`

   An activity with no planned session gets no verdict: see "Unplanned activity".
5. **Findings.** Two to four, each carrying the figure behind it. A cap that was reached or passed is always one of them. Use the figures table; add another figure only when it explains a finding. Athlete rules about reviews apply (for example, which breakdowns to leave out). When the activity for a planned easy session counts as hard by "Hard sessions and hard days" in `coach-rules`, say so with the minutes: its easy target is judged missed, and it takes a place in the week's cap, or in the hard-swim count for a swim.
6. **Next.** One line on what this means for the days ahead. If a coming planned session should change, say which and offer a plan update (that is `coach-adjust`; the athlete sees "plan update", not a skill name). After a test or a race whose result gives a new anchor, offer setup so the profile takes it. A session that fell short stays as it is: the next line never proposes repeating it or adding its load elsewhere. If the athlete proposes that, say that it stays as it is and which rule says so; a change they still want goes to `coach-adjust`.
7. **Write**, without asking, in this order: the day plan, then intervals.icu with a read-back, then commit.
   - the review, under "Session reviews" in the day plan;
   - the effort score, under "How I felt" in the day plan and on the activity in intervals.icu;
   - the coach's note to the activity's description in intervals.icu, as described under "Writes" in `coach-data`'s `intervals-icu.md`;
   - the activity's name: see "Naming".
8. **Send** the review in the sections of "Review shape". If the day plan's latest line under "Nutrition target" is an `estimate`, run `coach-nutrition` for that day afterwards; it sends the new target. The same after a planned session is written down as missed.

Done when, for each activity reviewed:

- the day plan holds the review, and the effort score or the fact that it was asked for;
- the message opens with the verdict line, or the unplanned line, and every line after it starts with a sign from the table, belongs to the Splits block, or is one of the closing lines "Review shape" allows;
- the activity holds the coach's note and its name as "Naming" gives it, or the athlete was told what could not be written;
- the commit is made.

An empty stub ends at step 2, and an effort answer that comes later ends with its confirmation.

## Figures

| Always | Run adds | Bike adds | Swim adds |
|---|---|---|---|
| duration, distance where the sport has one, average and maximum heart rate, load, time in zones, time in the target range, effort | average pace; pace and heart rate per rep; heart-rate drift for a steady run | average and normalised power; power per interval; heart-rate drift for a steady ride | per set: distance, pace per 100 m, rest, heart rate, strokes or SWOLF, and any equipment (paddles, pull buoy, fins) |

## Unplanned activity

Say what it was and what it cost: sport, duration, load, and how it sits against the week so far (from the week summary). The first line reads `<Sport>: UNPLANNED`, with no verdict and no judgement of whether it "should" have happened. Effort and the Next line work as for any review. In single-sport mode an activity in another sport is treated this way. It uses the same sections, without Goal and Execution, and its first line opens with ➕. An activity is planned when the day plan holds a session for it; the week plan's table does not decide. Write it under "Session reviews" as unplanned.

## A race

A race has a planned session (its form is in `coach-format`), so it is reviewed like any other, with the goal in place of the targets: the verdict is against the goal, Execution gives the result against it and the pacing (first half against second, or each leg and transition of a triathlon), and Next gives the easy days its priority calls for ("Races" in `coach-rules`). Where a triathlon arrives as several activities, one review covers them all. A race the day plan does not hold is reviewed as unplanned, with a line saying it looks like a race and offering setup to add it to the profile.

A brick is two activities and two reviews; the run's Notes say that it followed the ride.

## Planned session with no activity

1. Refresh.
2. If there is still no activity, ask once: was it skipped, or has it not synced yet?
3. Record under "Session reviews" that there was no activity, when you asked, and the answer or that there is none yet. A skipped session is counted as missed. If it was a key session or a test and the "Missed session" limit in `coach-rules` still allows a move this week, offer a plan update once; otherwise it stays missed. "Not synced yet" is checked again at the next run. When an activity later turns up for a session recorded as having none, review it and replace that entry.

Done when "Session reviews" records that there was no activity, with when it was asked and the answer or that there is none yet.

## Scheduled jobs

- **Midday and evening:** review each of today's activities that has no review yet, by the steps above.
- **Evening only:** then run "Planned session with no activity" for each of the day's planned sessions that still has none.
- With nothing to review and nothing missing, send nothing.

## Review shape

One review in two forms. The message to the athlete and "Session reviews" in the day plan take the fixed sections below: plain lines, no tables. The activity's description takes the coach's note, further down.

Two rules decide what goes in the sections:

- **The message stands alone.** The athlete reading it does not have the activity page open, so the Figures line carries the headline numbers once. Everything after it gives what the page cannot: the plan, the comparison, the meaning.
- **Say each fact once.** The Figures line gives numbers for the whole activity, Execution one per target and cap, Splits one per rep or set. The same number for the same thing is given in one of them, and comes back in Notes only where a line there says what it means.

Sections, in this order, each opened by its sign. Leave a section out when it has nothing to add. The message alone may end with up to three more lines: the effort question, `ℹ️ Basic figures` when the data came straight from intervals.icu, and `⚠️ Note not saved to intervals.icu` when the coach's note could not be written after one retry.

Several activities in one request: one message per activity, in the order of the day. The readiness line, fitness and form, and the Context line appear once, on the first. The effort question and the `ℹ️` line come once, at the end of the last message, and the question names each activity still without a score.

| Sign | Section | Holds |
|---|---|---|
| ✅ 🟡 ❌ | Verdict line | session name and verdict: done, partly, not done as planned. Unplanned: ➕ |
| 📏 | Figures | the headline numbers on one line: duration, distance where the sport has one, average power with normalised power, or average pace (per 100 m for a swim), average and maximum heart rate, and for a steady ride or run the heart-rate drift |
| 📊 | Load and state | load done against planned; effort out of 10, or `effort not given`; fitness and form, as context |
| 🟢 🟡 🔴 | Readiness | the day's verdict with sleep, HRV against baseline, resting heart rate, and any pain score |
| 🎯 | Goal | the planned session's purpose, targets and caps, in one line |
| ✅ 🟡 ❌ | Execution | one line per target and cap, with the figure. ✅ met. 🟡 missed for part of the session. ❌ missed for most of it. For a cap, time in the target range is time under the cap |
| ⏱ | Splits | reps and sets: one line each. A swim: as `swim.md` gives them. A steady session: only the splits that show where it changed, on one or two lines; all of them only when the splits are the finding. An athlete rule can switch this off for a kind of session |
| 📶 | Zones | one line: the share of the time in each zone, in percent, for power or pace zones and then for heart-rate zones. Leave out a zone under 2%, and a set of zones the analysis does not give |
| 🧠 | Notes | the coach's read, one to three lines: what went well, what to work on and how, and what it means for the block where the figures show that; with a comparison to the last session of the same kind where the day plans hold one, and any athlete limit the session passed, or one it could not be checked against because a score is missing |
| ➡️ | Next | what stands, and what to do differently next time |
| 📍 | Context | phase and week of the block, which session of the week this was, the week so far |

Sample with invented numbers:

```
🟡 Threshold run: PARTLY DONE AS PLANNED

📏 66 min · 13.3 km · 4:58/km · HR avg 151, max 170
📊 Load 74 of 78 · effort 8/10 · fitness 61 · form -6
🟢 GO · sleep 7.4 h · HRV 62 (60) · RHR 48 · knee 1/10
🎯 32 min at threshold: 4 x 8 min at 4:10/km, HR under 170

✅ Reps 1 to 3 on pace
❌ Rep 4 off pace by 11 s/km
🟡 HR cap reached in rep 4
🟡 24 of 32 min in the target range

⏱ Reps (pace · HR)
1 · 4:09 · 162
2 · 4:10 · 163
3 · 4:12 · 164
4 · 4:21 · 170

📶 Pace Z2 52% · Z3 12% · Z4 36% | HR Z2 47% · Z3 15% · Z4 38%

🧠 Reps 1 to 3 were threshold work done properly: on pace, HR flat.
🧠 Rep 4 slowed while HR rose 6 bpm: past threshold, not at it. When HR reaches 168 in a rep, ease 5 s/km and finish it.
🧠 Same fade as last week, when rep 4 was 4:19: the fourth rep is the limit for now.

➡️ Thursday's easy run stands. If rep 4 fades again next week, shorten to 3 x 8 before adding volume.

📍 Run build 1, load week 3 · hard session 1 of 2 · week so far: swim 2.0 km
```

A ride's two lines look like this: `📏 2:01 · 61 km · 184 W avg, 186 NP · HR avg 131, max 148 · drift 3.9%` and `📶 Power Z1 5% · Z2 89% · Z3 6% | HR Z1 58% · Z2 36% · Z3 6%`.

### The coach's note

What goes on the activity in intervals.icu. The page there already shows the numbers, so the note is the coach talking to the athlete about this one activity, in plain sentences and "you".

- **First line:** the verdict in words, and in one sentence whether the session did what it was for. For an unplanned activity: what it was and what it cost.
- **What went well:** one thing, with the figure or two that show it.
- **What to work on:** one thing, with its figure, why it matters, and what to do next time in terms the athlete can act on mid-session ("when heart rate reaches 168, ease 5 s/km").
- **Against last time:** the comparison with the last session of the same kind, where the day plans hold one, and what the two together say.
- **Zones:** the zones of the message's Zones section, here with minutes and percent, one line for each set of zones. This is the one block of figures the note carries. A set of zones the description above the note already gives is left out of the note.
- **Next:** the message's Next line, naming the planned sessions it concerns.

Leave out what the page shows as its headline for the whole activity: duration, distance, averages and maximums, load, fitness and form. Leave out, too, whatever the description above the note already states: read it first, and add to it. A figure for one block, rep or set, and heart-rate drift, may appear where a sentence needs it. Leave out a part that has nothing to say, and a sentence that only reads the zones back. Every sentence is about this activity: it could only have been written under this one.

Sample with invented numbers, for the run above:

```
Coach review

Partly done as planned. Three of the four reps were on pace and under the heart-rate cap; the fourth is where it got away from you.

What went well: reps 1 to 3 sat within 2 s/km of target with heart rate flat at 162 to 164. That is threshold work done properly.

What to work on: in rep 4 you slowed by 11 s/km while heart rate climbed to the cap. That is the effort going past threshold while the pace falls short of it. Next time, when heart rate reaches 168 in a rep, ease 5 s/km and finish the rep.

Against last time: the same fade, rep 4 at 4:19 then and 4:21 now. Twice running says the fourth rep is the limit for now, not a bad day.

Zones, pace: Z2 34 min (52%) · Z3 8 (12%) · Z4 24 (36%)
Zones, heart rate: Z2 31 min (47%) · Z3 10 (15%) · Z4 25 (38%)

Next: Thursday's easy run stands. If rep 4 fades again next week, shorten to 3 x 8 before adding volume.
```

## Naming

Rename an activity only when it still has the default name its device gave it: a time of day followed by the sport, such as `Morning Run`, `Lunch Ride`, `Afternoon Swim`, `Evening Run`, `Night Ride`, or the bare sport, such as `Pool Swim`. Any other name was chosen by someone or by an app (a race, a MyWhoosh or Zwift session) and stays as it is.

- Planned: the planned session's title in title case, for example `Threshold Run`.
- Unplanned: the sport and its character, for example `Easy Ride`.
- A swim, planned or not: named from its sets, as [swim.md](swim.md) gives it.

If the data index lists the naming question, run that command. Otherwise write the name to the activity in intervals.icu and read it back. The athlete can switch renaming off, for one activity or as a rule.

## Boundaries

- The plan and the calendar's planned sessions are left as they are.
- Every figure in a review comes from the analysis or the plan. One that is missing is named as missing.

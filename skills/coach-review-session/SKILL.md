---
name: coach-review-session
description: Use when the athlete asks for a review of a completed run, ride, swim or other training ("review my run", "review today's training"), and for the scheduled midday and evening jobs. Assesses one activity against its planned session.
---

# Session review

Assesses one activity against its planned session, where there is one, and says what it means for the days ahead.

The review advises. A planned session changes only through `coach-adjust`, after approval.

## Steps

1. **Load.** Use `coach-data` to find the data folder and refresh. Find the activity, then read the day plan for its date (the planned session it belongs to, the readiness verdict and "How I felt"), and the week and month plan for the context line. Load the rules through `coach-rules`.
2. **Get the figures** from `coach-data`: the analysis of the activity, the load state, and the week summary so far. An empty stub is not reviewed: `coach-data` handles it, the day plan gets one line under "Session reviews" saying the review is waiting on real figures, and the athlete is told.
3. **Effort.** If the day plan has no effort score for this activity, the review goes out with "Effort: not given" and ends with one question asking for effort out of 10. That is the one ask for this activity, whoever asks it. When the answer comes, write it in the three places of step 7 and confirm in a line.
4. **Verdict.** Judge the activity against the planned session's *purpose* and give one of three:
   - `DONE AS PLANNED`
   - `PARTLY DONE AS PLANNED`
   - `NOT DONE AS PLANNED`

   An activity with no planned session gets no verdict: see "Unplanned activity".
5. **Findings.** Two to four, each carrying the figure behind it. A cap that was reached or passed is always one of them. Use the figures table; add another figure only when it explains a finding. Athlete rules about reviews apply (for example, which breakdowns to leave out).
6. **Next.** One line on what this means for the days ahead. It advises only. If a coming planned session should change, say which and offer a plan update (that is `coach-adjust`; the athlete sees "plan update", not a skill name). A session that fell short stays as it is: the next line never proposes repeating it or adding its load elsewhere. If the athlete proposes that, say that it stays as it is and which rule says so; a change they still want goes to `coach-adjust`.
7. **Write**, without asking, in this order: the day plan, then intervals.icu with a read-back, then commit.
   - the review, under "Session reviews" in the day plan;
   - the effort score, under "How I felt" in the day plan and on the activity in intervals.icu;
   - the whole review to the activity's description in intervals.icu, as described under "Writes" in `coach-data`'s `intervals-icu.md`;
   - the activity's name: see "Naming".
8. **Send** the review.

Done when the day plan holds the review and the athlete has the message.

## Figures

| Always | Run adds | Bike adds | Swim adds |
|---|---|---|---|
| duration, load, time in the target range, effort | pace and heart rate per rep | power per interval, heart-rate drift | pace per 100 m per set |

## Unplanned activity

Say what it was and what it cost: sport, duration, load, and how it sits against the week so far (from the week summary). The first line reads `<Sport>: UNPLANNED`, with no verdict and no judgement of whether it "should" have happened. Effort and the Next line work as for any review. In single-sport mode an activity in another sport is treated this way. It uses the same sections, without Goal and Execution, and its first line opens with ➕. An activity is planned when the day plan holds a session for it; the week plan's table does not decide. Write it under "Session reviews" as unplanned.

## Planned session with no activity

1. Refresh.
2. If there is still no activity, ask once: was it skipped, or has it not synced yet?
3. Record under "Session reviews" that there was no activity, when you asked, and the answer or that there is none yet. A skipped session is counted as missed; it stays missed. "Not synced yet" is checked again at the next run. When an activity later turns up for a session recorded as having none, review it and replace that entry.

## Scheduled jobs

- **Midday and evening:** review each of today's activities that has no review yet, by the steps above.
- **Evening only:** then run "Planned session with no activity" for each of the day's planned sessions that still has none.
- With nothing to review and nothing missing, send nothing.

## Review shape

One review, in fixed sections, used in three places: the message to the athlete, "Session reviews" in the day plan, and the activity's description. Plain lines, no tables.

Two rules decide what goes in:

- **Add, don't repeat.** The activity page already shows distance, time, average pace or power, average heart rate, cadence and climb. Leave those out unless a finding needs one. Give what the page cannot: the plan, the comparison, the meaning.
- **Say each fact once.** A figure given under Execution is not given again under Splits or Notes.

Sections, in this order, each opened by its sign. Leave a section out when it has nothing to add. The message alone may end with two more lines: the effort question, and `ℹ️ Basic figures` when the data came straight from intervals.icu.

Several activities in one request: one message per activity, in the order of the day. The readiness line appears once, on the first. The effort question and the `ℹ️` line come once, at the end of the last message, and the question names each activity still without a score.

| Sign | Section | Holds |
|---|---|---|
| ✅ 🟡 ❌ | Verdict line | session name and verdict: done, partly, not done as planned. Unplanned: ➕ |
| 📊 | Load and state | load done against planned; effort out of 10, or "effort not given"; fitness and form, as context |
| 🟢 🟡 🔴 | Readiness | the day's verdict with sleep, HRV against baseline, resting heart rate, and any pain score |
| 🎯 | Goal | the planned session's purpose, targets and caps, in one line |
| ✅ 🟡 ❌ | Execution | one line per target and cap, with the figure. ✅ met. 🟡 missed for part of the session. ❌ missed for most of it. For a cap, time in the target range is time under the cap |
| ⏱ | Splits | reps and sets: one line each. A steady session: only the splits that show where it changed, on one or two lines; all of them only when the splits are the finding. An athlete rule can switch this off for a kind of session |
| 🧠 | Notes | what the numbers mean: one to three findings, with a comparison to the last session of the same kind where the day plans hold one, and any athlete limit the session passed |
| ➡️ | Next | what stands, and what to do differently next time |
| 📍 | Context | phase and week of the block, which session of the week this was, the week so far |

Sample with invented numbers:

```
🟡 Threshold run: PARTLY DONE AS PLANNED

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

🧠 Rep 4 slowed while HR rose 6 bpm: past threshold, not at it.
🧠 Same fade as last week, when rep 4 was 4:19.

➡️ Thursday's easy run stands. If rep 4 fades again next week, shorten to 3 x 8 before adding volume.

📍 Run build 1, load week 3 · hard session 1 of 2 · week so far: swim 2.0 km
```

## Naming

Rename an activity only when it still has the default name its device gave it: a time of day followed by the sport, such as `Morning Run`, `Lunch Ride`, `Afternoon Swim`, `Evening Run`, `Night Ride`. Any other name was chosen by someone or by an app (a race, a MyWhoosh or Zwift session) and stays as it is.

- Planned: the planned session's title in title case, for example `Threshold Run`.
- Unplanned: the sport and its character, for example `Easy Ride`.

If the data index lists the naming question, run that command. Otherwise write the name to the activity in intervals.icu and read it back. The athlete can switch renaming off, for one activity or as a rule.

## Boundaries

- Every figure in a review comes from the analysis or the plan. One that is missing is named as missing.
- The plan and the calendar's planned sessions are left as they are.

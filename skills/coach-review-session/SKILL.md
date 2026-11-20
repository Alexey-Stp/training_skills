---
name: coach-review-session
description: Use when the athlete asks for a review of a completed run, ride, swim or other training ("review my run", "review today's training"), and for the scheduled midday and evening jobs. Assesses one activity against its planned session.
---

# Session review

Assesses one activity against its planned session, where there is one, and says what it means for the days ahead.

The review advises. A planned session changes only through `coach-adjust`, after approval.

## Steps

1. **Load.** Use `coach-data` to find the data folder and refresh. Find the activity, then read the day plan for its date: the planned session it belongs to and "How I felt". Load the rules through `coach-rules`.
2. **Get the analysis** of the activity from `coach-data`. An empty stub is not reviewed: `coach-data` handles it, the day plan gets one line under "Session reviews" saying the review is waiting on real figures, and the athlete is told.
3. **Effort.** If the day plan has no effort score for this activity, the review goes out with "Effort: not given" and ends with one question asking for effort out of 10. That is the one ask for this activity, whoever asks it. When the answer comes, write it in the three places of step 7 and confirm in a line.
4. **Verdict.** Judge the activity against the planned session's *purpose* and give one of three:
   - `DONE AS PLANNED`
   - `PARTLY DONE AS PLANNED`
   - `NOT DONE AS PLANNED`

   An activity with no planned session gets no verdict: see "Unplanned activity".
5. **Findings.** Two to four, each carrying the figure behind it. A cap that was reached or passed is always one of them. Use the figures table; add another figure only when it explains a finding. Athlete rules about reviews apply (for example, which breakdowns to leave out).
6. **Next.** One line on what this means for the days ahead. It advises only. If a coming planned session should change, say which and point to `coach-adjust`. A session that fell short stays as it is: the next line never proposes repeating it or adding its load elsewhere. If the athlete proposes that, say that it stays as it is and which rule says so; a change they still want goes to `coach-adjust`.
7. **Write**, without asking, then commit:
   - the review, under "Session reviews" in the day plan;
   - the effort score, under "How I felt" in the day plan and on the activity in intervals.icu;
   - a short version (verdict line and Next line) to the activity's description in intervals.icu, as described under "Writes" in `coach-data`'s `intervals-icu.md`;
   - the activity's name, only when the data index lists the naming question.
8. **Send** the review in the shape below.

Done when the day plan holds the review and the athlete has the message.

## Figures

| Always | Run adds | Bike adds | Swim adds |
|---|---|---|---|
| duration, load, time in the target range, effort | pace and heart rate per rep | power per interval, heart-rate drift | pace per 100 m per set |

## Unplanned activity

Say what it was and what it cost: sport, duration, load, and how it sits against the week so far (from the week summary). The first line reads `<Sport>: UNPLANNED`, with no verdict and no judgement of whether it "should" have happened. Effort and the Next line work as for any review. In single-sport mode an activity in another sport is treated this way. Write it under "Session reviews" as unplanned; the short version is the first line and the Next line.

## Planned session with no activity

1. Refresh.
2. If there is still no activity, ask once: was it skipped, or has it not synced yet?
3. Record under "Session reviews" that there was no activity, when you asked, and the answer or that there is none yet. A skipped session is counted as missed; it stays missed. "Not synced yet" is checked again at the next run. When an activity later turns up for a session recorded as having none, review it and replace that entry.

## Scheduled jobs

- **Midday and evening:** review each of today's activities that has no review yet, by the steps above.
- **Evening only:** then run "Planned session with no activity" for each of the day's planned sessions that still has none.
- With nothing to review and nothing missing, send nothing.

## Message shape

In this order: verdict line with the session name; planned against actual for the main set; how much of the purpose was achieved; the findings; the Next line. Short enough for a phone screen, plain lines, no tables.

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

## Boundaries

- Every figure in a review comes from the analysis or the plan. One that is missing is named as missing.
- The plan and the calendar's planned sessions are left as they are.

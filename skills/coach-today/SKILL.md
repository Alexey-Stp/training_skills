---
name: coach-today
description: Use when the athlete asks what today's or tomorrow's session is or whether they are ready ("what's today", "am I ready", "what's tomorrow"), and for the scheduled morning job. Gives the daily check and its readiness verdict.
---

# Daily check

What is today's planned session, and is the athlete ready for it. Ends in a readiness verdict: **GO**, **MODIFY** or **SKIP**.

The verdict advises. The plan and the calendar change only through `coach-adjust`, after approval.

## Steps

1. **Load.** Use `coach-data` to find the data folder and refresh. Read today's day plan, yesterday's day plan (its verdict and "How I felt"), the week plan header, and the readiness bands and limits in `ATHLETE-RULES.md` (through `coach-rules`).
2. **Get readiness** for today from `coach-data`: one score and its inputs. If sleep and HRV are both missing, there is no score to judge: go to "No data yet".
3. **Band.** Map the score to go, modify or skip with the cut-offs in `ATHLETE-RULES.md`.
4. **Apply the safeguards**, in this order. The first that fits decides.
   1. Fever or systemic symptoms reported: **SKIP**, whatever the score. Rest only.
   2. A limit in `ATHLETE-RULES.md` is met (for example a pain score): apply it exactly as written, whatever the score. If it rules out every session planned today, the verdict is **SKIP**; if it rules out or restricts some, **MODIFY**. Say which rule decided and what it still allows.
   3. The score is in the lowest band: it is **SKIP** only with a reported symptom, or when yesterday's verdict was also modify or skip. Otherwise **MODIFY**.
   4. Otherwise the band stands.
5. **Say what the verdict means for today's session.**
   - GO: the planned session as planned.
   - MODIFY: a hard session becomes an easy one of the same or shorter duration; an easy session is shortened, and the message gives the new duration.
   - SKIP: rest, or 30 minutes very easy. With fever or systemic symptoms: rest.
   - The verdict is for the day. On a day with several sessions, say what happens to each; a session the verdict does not touch stands.
6. **Log.** Write to today's day plan, once per day: the verdict with the time and its inputs under "Readiness verdict", and anything the athlete said about how they feel under "How I felt". Commit. These two sections are everything this skill writes.
7. **Send the message** in the shape below. On MODIFY or SKIP, end with one line offering `coach-adjust` to change the plan. If the week plan header says "not synced", add one line saying the session may be missing from the watch. If an athlete limit depends on a score the athlete gives on waking and they have not given it, add one line asking for it; this is the morning's one question.

Done when the athlete has the message and the day plan holds the verdict.

## No data yet

**Scheduled morning job** (runs at 08:00, 09:00 and 10:00, speaks once):

- Sleep and HRV present: run the steps above and send. Later runs that day see the verdict in the day plan and stay silent. A provisional verdict does not count: replace it with the real one and send.
- Missing at 08:00 or 09:00: send nothing and write nothing.
- Still missing at 10:00: send today's session, say that no verdict is possible because last night's data has not arrived, and ask how the athlete feels unless they were already asked today. Write under "Readiness verdict": no verdict at 10:00, data missing.

**Asked by the athlete before the data arrives:** send the session, say no verdict is possible yet, and ask how they feel if they have not said. From what they report, give a verdict labelled **provisional** and log it with that label: poor sleep, heavy legs or soreness give MODIFY; nothing of note gives GO. Safeguards 1 and 2 still apply in full. An answer to the 10:00 question is handled the same way.

Ask how the athlete feels at most once each morning. No answer is fine.

## Tomorrow

First line `Tomorrow, <weekday date>`. Show tomorrow's planned session from its day plan and say the verdict comes in the morning. Add the "not synced" line if it applies. No verdict is written; a score the athlete mentions is still logged in today's day plan.

## Message shape

Verdict first. Then the planned session with its targets and caps, as it now stands under the verdict. Then one line with the three or four inputs that carried the verdict; when a symptom or a limit decided, that line says so. Short enough for a phone screen, plain lines, no tables.

```
GO

Threshold run, 65 min: 4 x 8 min at 4:10/km, 2 min easy between.
Cap: heart rate under 170 in the reps.
Then strength, 20 min.

Readiness 78. Sleep 7.4 h, HRV 62 (baseline 60), resting HR 48.
```

A provisional verdict reads `MODIFY (provisional)`. With no verdict, the first line is `NO VERDICT YET`.

## Boundaries

- Report symptoms in the athlete's own words and apply the limit. What the symptom is, is for a clinician.
- A figure that did not arrive is named as missing.
- This skill reads the week plan's sync line and leaves the calendar itself unread.

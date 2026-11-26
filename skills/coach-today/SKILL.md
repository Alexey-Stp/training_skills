---
name: coach-today
description: Use when the athlete asks what today's or tomorrow's session is or whether they are ready ("what's today", "am I ready", "what's tomorrow"), when they ask why about today's verdict or dispute it, or ask about today's targets (how they were worked out, whether they may go above or below), and for the scheduled morning job. Gives the daily check and its readiness verdict.
---

# Daily check

What is today's planned session, and is the athlete ready for it. Ends in a readiness verdict: **GO**, **MODIFY** or **SKIP**.

The verdict advises. The plan and the calendar change only through `coach-adjust`, after approval.

## Steps

1. **Load** in the rounds `coach-data` gives. Read today's day plan, yesterday's day plan (its verdict with its inputs, "How I felt" and its session reviews), the week plan header, the illness flags with one search across the day plans dated in the last 14 days, and the readiness bands and limits in `ATHLETE-RULES.md` (through `coach-rules`). From `coach-data`, yesterday's and today's activities. Once there is a score:
   - a hard session is planned today: in a third round, the analysis of each of those activities, for safeguard 5, with this week's row of the month plan, which names the key sessions, and the day plans from tomorrow to Sunday, which step 5 needs if a key session or a test has to move;
   - no hard session is planned and the verdict eases a session: that row and those day plans in one more round.
2. **Get readiness** for today from `coach-data`, with the questions of step 1: one score and its inputs. If sleep and HRV are both missing, there is no score to judge: go to "No data yet".
3. **Band.** Map the score to go, modify or skip with the cut-offs in `ATHLETE-RULES.md`. Then apply the HRV trend rule under "Readiness" in `coach-rules`.
4. **Apply the safeguards**, in this order. The first that fits decides, except that safeguard 2 only sets a floor.
   1. Fever or systemic symptoms reported: **SKIP**, whatever the score. Rest only.
   2. A return day after fever or systemic symptoms, counted as the limit in `coach-rules` says: easy sessions only, so the verdict is **MODIFY** at least when a hard session is planned. Go on down the list; a stricter verdict below stands.
   3. A limit in `ATHLETE-RULES.md` is met (for example a pain score): apply it exactly as written, whatever the score. If it rules out every session planned today, the verdict is **SKIP**; if it rules out or restricts some, **MODIFY**. Say which rule decided and what it still allows.
   4. The score is in the lowest band: it is **SKIP** only with a reported symptom, or when yesterday's score was in the lowest band too. A MODIFY yesterday that came from a limit or from spacing does not count. Otherwise **MODIFY**.
   5. Yesterday held a hard bike or run activity, planned or not, or the long run, and today holds a hard bike or run session: **MODIFY**, and say that the hard-days limit decided. The same for a hard swim yesterday and a hard swim today. What counts as hard is in `coach-rules`.
   6. Otherwise the band stands, as it is after the HRV trend rule.
5. **Say what the verdict means for today's session.**
   - GO: the planned session as planned.
   - MODIFY: what "Readiness" in `coach-rules` gives for each kind of session; the message gives the new duration.
   - MODIFY or SKIP on a key session or a test: first look for a later day this week that can take it under the "Missed session" limit in `coach-rules`. If there is one, offer the earliest such day as the first choice: the key session goes there, and that day's easy session of the same sport comes to today (shortened under MODIFY) or is dropped (under SKIP). Otherwise say that it is eased and not moved, and why.
   - A race today: no verdict eases or moves it, and no move to a later day is offered. Safeguards 1 to 3 apply as written. Otherwise the first line of the message and the logged verdict read `RACE DAY`, with the score and its inputs as information; whether to start is the athlete's decision.
   - An activity already recorded today: if it belongs to one of today's planned sessions, say so and leave that session out of the verdict. If it is unplanned, name it; when it was hard, a hard session still ahead today is treated as safeguard 5 treats one after a hard day. The verdict then speaks to the sessions still ahead; with none ahead, give the score and its inputs as information for the rest of the day.
   - SKIP: rest, or 30 minutes very easy. With fever or systemic symptoms: rest.
   - The verdict is for the day. On a day with several sessions, say what happens to each; a session the verdict does not touch stands.
6. **Check the anchors** of each of today's sessions against the athlete profile, as "Anchors in a plan" in `coach-rules` says. Where they call for something to be said (a session out of date, or figures in watts or pace with no `Anchors:` line), the message gets an anchor note: one line for each anchor, with what those rules give for today's sessions. The note is given once a day: the log holds it, and a later message that day repeats only the offer, in a few words, unless the athlete asks about a target or a later verdict changes the note.
7. **Log.** Write to today's day plan, once per day (a later verdict only as [questions.md](questions.md) says): the verdict with the time, its inputs, what it means for each of today's sessions and the anchor note when there is one, under "Readiness verdict"; and anything the athlete said about how they feel under "How I felt". Commit. These two sections are everything this skill writes: no week plan, no other plan file, and no session's duration or targets.
8. **Send the message** in the shape below. When the verdict is MODIFY or SKIP, or an anchor note is there, end with one line offering `coach-adjust`, naming what it would change: the session the verdict eased, the sessions built on the old anchor value or recording none, or all of these. If the week plan header says "not synced", add one line saying which session may be missing from the watch. If the week plan is still `DRAFT`, say first that this week's plan is a draft waiting for approval, and that nothing is on the watch. If an athlete limit depends on a score the athlete gives on waking and they have not given it, add one line asking for it; this is the morning's one question.

Done when the athlete has the message and the day plan holds the verdict.

## No data yet

**Scheduled morning job** (runs at 08:00, 09:00 and 10:00, speaks once):

- Sleep and HRV present: run the steps above and send. Later runs that day see the verdict in the day plan and stay silent. A provisional verdict does not count: replace it with the real one and send, naming the provisional verdict it replaces.
- Missing at 08:00 or 09:00: send nothing and write nothing.
- Still missing at 10:00: send today's sessions still ahead, say that no verdict is possible because last night's data has not arrived, and ask how the athlete feels unless they were already asked today. Write under "Readiness verdict": no verdict at 10:00, data missing, and the anchor note when there is one.

**Asked by the athlete before the data arrives:** send the session, say no verdict is possible yet, and ask how they feel if they have not said. From what they report, give a verdict labelled **provisional** and log it with that label: poor sleep, heavy legs or soreness give MODIFY; nothing of note gives GO. Safeguards 1 to 3 and 5 still apply in full. An answer to the 10:00 question is handled the same way.

Ask how the athlete feels at most once each morning. No answer is fine.

The anchor check of step 6 runs on each of these paths that sends a message. With no verdict, a session is treated as one the verdict leaves alone. When a verdict that comes later that day changes what the note said, the message with that verdict says so in one line (for example that the figures given earlier no longer apply today), and the note is logged as it now stands.

## Questions after the message

When the athlete asks why, disputes today's verdict, asks for today's session again after a verdict was logged, or asks about a target, read [questions.md](questions.md) first.

## Tomorrow

First line `Tomorrow, <weekday date>`. Show tomorrow's planned session from its day plan and say the verdict comes in the morning. Add the "not synced" line if it applies, and the anchor note of step 6 for tomorrow's sessions, with the same offer; nothing of it is logged, so it is given each time tomorrow is asked about. No verdict is written; a score the athlete mentions is still logged in today's day plan.

## Message shape

Verdict first. Then the planned session with its targets and caps, as the verdict advises. Then one line with the three or four inputs that carried the verdict; when a symptom or a limit decided, that line says so. Short enough for a phone screen, plain lines, no tables.

```
GO

Threshold run, 65 min: 4 x 8 min at 4:10/km, 2 min easy between.
Cap: heart rate under 170 in the reps.
Then strength, 20 min.

Readiness 78. Sleep 7.4 h, HRV 62 (7-night 61, baseline 60), resting HR 48.
```

The anchor note, when step 6 calls for one, comes after the inputs: `Run threshold is now 4:05 /km (plan used 4:10): the reps would be at 4:05.` For a session with no `Anchors:` line: `The plan does not record what the reps were built on: 4:10 is 98% of your run threshold now.` Where an athlete rule forbids targets from an old value, it comes straight after the session instead and says that the rule is not met until the plan is updated.

A provisional verdict reads `MODIFY (provisional)`. With no verdict, the first line is `NO VERDICT YET`.

## Boundaries

- Report symptoms in the athlete's own words and apply the limit. What the symptom is, is for a clinician.
- A figure that did not arrive is named as missing.
- Targets and caps are given as the day plan holds them.
- Report only what was read. What another message, a scheduled job or a file says is read first when it is in the data folder or in this conversation, and quoted from there; otherwise it is named as not checked.
- Reasons come from the rules: the band, a safeguard, a limit. What fitness, fatigue and form are for is under "Load figures" in `coach-rules`: they argue neither for more training nor for less.
- This skill proposes no change to the readiness bands of its own accord. The week review says when tuning may be due, and `coach-setup` makes the change.
- This skill reads the week plan's sync line and leaves the calendar itself unread.

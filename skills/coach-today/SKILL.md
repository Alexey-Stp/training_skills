---
name: coach-today
description: Use when the athlete asks what today's or tomorrow's session is or whether they are ready ("what's today", "am I ready", "what's tomorrow"), when they ask why about today's verdict or dispute it, or ask how today's targets were worked out, and for the scheduled morning job. Gives the daily check and its readiness verdict.
---

# Daily check

What is today's planned session, and is the athlete ready for it. Ends in a readiness verdict: **GO**, **MODIFY** or **SKIP**.

The verdict advises. The plan and the calendar change only through `coach-adjust`, after approval.

## Steps

1. **Load.** Use `coach-data` to find the data folder and refresh. Read today's day plan, yesterday's day plan (its verdict with its inputs, "How I felt" and its session reviews), yesterday's and today's activities from `coach-data`, the illness flags in the day plans of the last 14 days, the week plan header, and the readiness bands and limits in `ATHLETE-RULES.md` (through `coach-rules`).
2. **Get readiness** for today from `coach-data`: one score and its inputs. If sleep and HRV are both missing, there is no score to judge: go to "No data yet".
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
6. **Log.** Write to today's day plan, once per day (a later verdict only as "Asked about the verdict" says): the verdict with the time, its inputs and what it means for each of today's sessions under "Readiness verdict", and anything the athlete said about how they feel under "How I felt". Commit. These two sections are everything this skill writes: no week plan, no other plan file, and no session's duration.
7. **Check the anchors.** For each of today's sessions, compare the anchor value its "Targets" and "Caps" name with the athlete profile. Where the profile now holds another value, the message gets one line: which anchor changed, what the "Thresholds" default in `coach-rules` gives from the new value, and an offer of `coach-adjust`. Where a figure in watts or pace names no anchor, say in one line that the plan does not record what it came from, and offer `coach-adjust` to restate it. A target with no figure from an anchor ("easy, heart rate under 140") needs no line. The check runs each time the session is given, and nothing of it is logged.
8. **Send the message** in the shape below. On MODIFY or SKIP, end with one line offering `coach-adjust` to change the plan; where the anchor line is there too, one offer covers both. If the week plan header says "not synced", add one line saying which session may be missing from the watch. If the week plan is still `DRAFT`, say first that this week's plan is a draft waiting for approval, and that nothing is on the watch. If an athlete limit depends on a score the athlete gives on waking and they have not given it, add one line asking for it; this is the morning's one question.

Done when the athlete has the message and the day plan holds the verdict.

## No data yet

**Scheduled morning job** (runs at 08:00, 09:00 and 10:00, speaks once):

- Sleep and HRV present: run the steps above and send. Later runs that day see the verdict in the day plan and stay silent. A provisional verdict does not count: replace it with the real one and send, naming the provisional verdict it replaces.
- Missing at 08:00 or 09:00: send nothing and write nothing.
- Still missing at 10:00: send today's sessions still ahead, say that no verdict is possible because last night's data has not arrived, and ask how the athlete feels unless they were already asked today. Write under "Readiness verdict": no verdict at 10:00, data missing.

**Asked by the athlete before the data arrives:** send the session, say no verdict is possible yet, and ask how they feel if they have not said. From what they report, give a verdict labelled **provisional** and log it with that label: poor sleep, heavy legs or soreness give MODIFY; nothing of note gives GO. Safeguards 1 to 3 and 5 still apply in full. An answer to the 10:00 question is handled the same way.

Ask how the athlete feels at most once each morning. No answer is fine.

## Asked about the verdict

When the athlete asks why, questions the verdict, or asks for today's session again after a verdict was logged:

1. **Refresh and compare.** Refresh, then compare the inputs with the ones logged, and check the anchors again as step 7 says.
2. **Explain it, when asked why.** Asked only for today's session again, give the logged verdict and the session once more. Asked why: give the score, the band it fell in, and the rule or safeguard that decided, with the figures, and what that rule does to the session. Where the band alone decided, say so.
3. **The verdict stands** unless one of these two holds:
   - **Something new.** A symptom, a pain score, an activity, or an input that arrived or changed at its source since the verdict was logged and before the session started. Name it, run the steps again and give the new verdict. A good feeling is logged under "How I felt" and is not something new.
   - **A mistake in applying the rules.** The wrong band (the bands as they stood when the verdict was logged), a safeguard or the HRV trend rule left out, a duration more than 10 minutes from what the MODIFY rule gives, a key session with no move offered. Say what was wrong, give what the rules give, and log it as a correction.
   Whether the rule itself suits the athlete is neither: that view changes no verdict.
4. **Log a new or corrected verdict** as `coach-format` says for a later verdict. With neither, write nothing but what the athlete said about how they feel.
5. **End with where things stand:** the verdict; what the day plan holds for the session now, where a change approved today stands over the verdict's duration; and, unless a fever, a return day after illness or an athlete limit decided, that training as planned is the athlete's own decision. A change to the plan goes through `coach-adjust`.

Three cases:

- **"Should I do it anyway":** the answer is the verdict, then step 5.
- **Another message disagrees:** the verdict logged in the day plan is the one in force.
- **Asked to move a band:** the bands are the athlete's rules, and `coach-setup` changes them after approval: offer it in one line. Today's logged verdict is unchanged.

With nothing new and no mistake, say that nothing new has arrived.

## Asked about a target

When the athlete asks what a target is, how it was worked out, or whether they may go above or below it:

1. **Answer whole, in one message.** The target as the day plan holds it; the anchor and the percentages of it the target names; the profile's value for that anchor now, with its test date; and whether the two agree. Where the target names no anchor, say that the plan does not record it; do not work one out from zones or a typical range.
2. **Anchor changed since:** say so in the same message, with what the "Thresholds" default in `coach-rules` gives from the current value, and offer `coach-adjust`. Until the athlete takes the offer, the session stands as planned.
3. **Above or below the range:** the range and the caps are the plan. Train to the target and ease when a cap is reached: say that in one line, and keep both.

A target or a cap moves only through `coach-adjust`, after approval, and the calendar follows as `coach-adjust` says. Being asked again is not a reason to give another figure.

## Tomorrow

First line `Tomorrow, <weekday date>`. Show tomorrow's planned session from its day plan and say the verdict comes in the morning. Add the "not synced" line if it applies. No verdict is written; a score the athlete mentions is still logged in today's day plan.

## Message shape

Verdict first. Then the planned session with its targets and caps, as the verdict advises. Then one line with the three or four inputs that carried the verdict; when a symptom or a limit decided, that line says so. Short enough for a phone screen, plain lines, no tables.

```
GO

Threshold run, 65 min: 4 x 8 min at 4:10/km, 2 min easy between.
Cap: heart rate under 170 in the reps.
Then strength, 20 min.

Readiness 78. Sleep 7.4 h, HRV 62 (7-night 61, baseline 60), resting HR 48.
```

The anchor line, when step 7 calls for one, comes after the inputs: `Run threshold is now 4:05 /km (plan used 4:10): the reps would be at 4:05. Say "adjust" to change them.`

A provisional verdict reads `MODIFY (provisional)`. With no verdict, the first line is `NO VERDICT YET`.

## Boundaries

- Report symptoms in the athlete's own words and apply the limit. What the symptom is, is for a clinician.
- A figure that did not arrive is named as missing.
- Targets and caps are given as the day plan holds them. Another figure is given only as what a changed anchor gives, with the offer of `coach-adjust`; never from zones or a typical range.
- Report only what was read. What another message, a scheduled job or a file says is read first when it is in the data folder or in this conversation, and quoted from there; otherwise it is named as not checked.
- Reasons come from the rules: the band, a safeguard, a limit. What fitness, fatigue and form are for is under "Load figures" in `coach-rules`: they argue neither for more training nor for less.
- This skill proposes no change to the readiness bands of its own accord. The week review says when tuning may be due, and `coach-setup` makes the change.
- This skill reads the week plan's sync line and leaves the calendar itself unread.

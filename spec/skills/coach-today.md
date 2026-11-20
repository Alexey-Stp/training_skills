# coach-today

## Purpose

The daily check: what is today's planned session, and is the athlete ready for it. Ends in a readiness verdict of go, modify or skip. Also answers "what's tomorrow".

## Triggers

- "what's today", "am I ready", "what's tomorrow".
- The scheduled morning job.

## Reads

- Today's day plan, and yesterday's and today's subjective log.
- Readiness for the date, through the training data skill: one score plus the inputs behind it (sleep, HRV, resting heart rate, form, device readiness; the last is optional).
- Readiness bands and limits from the athlete rules.
- The week plan's calendar sync state.

## Writes

To today's day plan, once per day, and nothing else ([today skill][t20], [subjective log][t23]):

- The readiness verdict with its inputs.
- The morning feel answer, if the athlete gives one.

## Steps

1. Ask the training data skill to refresh, then for readiness.
2. Map the score to a band using the athlete rules' cut-offs.
3. Apply the safeguards:
   - A low score alone gives at most modify.
   - Skip needs a low score plus a reported symptom, or a second poor day in a row.
   - Fever or systemic symptoms mean skip, whatever the score.
   - A limit in the athlete rules (for example a pain score) applies as written.
4. State what the verdict means for today's session:
   - Go: the planned session as planned.
   - Modify: a hard session becomes an easy one of the same or shorter duration; an easy session is shortened.
   - Skip: rest, or 30 minutes very easy.
5. On modify or skip, offer `coach-adjust`. The verdict itself changes no plan.
6. Write the verdict to the day plan.
7. If the week plan is approved but not synced, say so. It does not look for calendar differences; the skills named under "Calendar sync" in [plan format](plan-format.md) do. ([calendar sync][t13])

Scheduled morning job:

- Tries at 08:00, 09:00 and 10:00. Speaks once, as soon as last night's sleep and HRV are present.
- At 10:00 without data: sends the session, states that no verdict is possible, and asks how the athlete feels.

Asked by hand before the data arrives: the same as the 10:00 fallback, plus a provisional verdict from what the athlete reports, labelled provisional.

"Tomorrow": shows tomorrow's planned session and states that no verdict is possible until morning. ([skill list][t7])

It may ask how the athlete feels at most once each morning. No answer is fine.

## Reply shape

Verdict first, then the planned session with targets, then the three or four inputs behind the verdict. Phone-sized, no tables. Sample with invented numbers:

```
GO

Threshold run, 65 min: 4 x 8 min at 4:10/km, 2 min easy between.
Cap: heart rate under 170 in the reps.
Then strength, 20 min.

Readiness 78. Sleep 7.4 h, HRV 62 (baseline 60), resting HR 48.
```

## Must never

- Give skip from a score alone.
- Change a plan or the calendar.
- Invent a verdict when the data is missing; say it is missing.
- Ask about feel more than once in a morning.
- Diagnose illness.

## Source tickets

[Today skill][t20], [subjective log][t23], [skill list][t7], [coaching method][t11], [training data contract][t21], [everyday athlete usage][t4].

[t4]: https://github.com/Alexey-Stp/training_skills/issues/4
[t7]: https://github.com/Alexey-Stp/training_skills/issues/7
[t11]: https://github.com/Alexey-Stp/training_skills/issues/11
[t13]: https://github.com/Alexey-Stp/training_skills/issues/13
[t20]: https://github.com/Alexey-Stp/training_skills/issues/20
[t21]: https://github.com/Alexey-Stp/training_skills/issues/21
[t23]: https://github.com/Alexey-Stp/training_skills/issues/23

---
name: coach-format
description: Use when reading or writing the athlete's plan files (month, week or day plan), writing a planned session, logging a plan update, or publishing sessions to the intervals.icu calendar.
user-invocable: false
---

# Plan format

How the athlete's plan files are laid out and how a planned session reaches the calendar. The markdown files are the truth; intervals.icu receives a copy.

## Files

All paths are relative to the data folder; the `coach-data` skill finds it.

| File | Path | Written by |
|---|---|---|
| Month plan | `plan/months/<first Monday of the block>.md` | `coach-plan-month` |
| Week plan | `plan/weeks/<Monday>.md` | `coach-plan-week`, `coach-adjust`, `coach-review-week` |
| Day plan | `plan/days/<date>.md` | `coach-plan-week`, `coach-adjust`, `coach-today`, `coach-review-session` |

Dates are `YYYY-MM-DD`. Each file follows its template in [templates/](templates/): same headings, same order, same field names. The templates hold invented data; copy the layout, never the values.

- **Status.** Week and month plans carry `DRAFT`, then `APPROVED`, then `CLOSED`. Closed means reviewed. A day plan follows its week.
- **How far ahead.** Month plan: the current block, plus the next one drafted during the current block's last week. Week plan: the current week, plus next week's draft from Sunday. Day plans: all seven are created when the week is drafted.
- **One file per week**, from the moment it is drafted. The current week is found by date.
- **Commit** to the workspace's local repository after each write.
- **Tables** belong in files. A message to the athlete is short and has none.

## A day plan

Four sections, filled in as the day goes on:

1. **Planned sessions**, written in full here and nowhere else.
2. **Readiness verdict**, with the inputs behind it.
3. **How I felt**: the subjective log.
4. **Session reviews**, including a planned session that had no activity.

## A planned session

Fixed fields, in this order: sport, duration, planned load, purpose, targets, caps, calendar. The title is the heading. Write `none` for an empty field. Then the steps in intervals.icu workout text, in a code block, so calendar sync publishes them as written.

Workout text, as far as it is tested:

- One step per line: `- 10m 60%` is 10 minutes at 60% of threshold.
- `m` means minutes and `s` seconds. `200m` is 200 minutes.
- Pace targets (`65-75% Pace`) need the sport's threshold pace set in intervals.icu.
- Distances in metres and repeats with rests are not established. That includes the repeat form the day plan template uses (`Main set 4x`, then its steps). Until they are, the read-back check in [calendar-sync.md](calendar-sync.md) is what catches a session that was parsed wrongly.

## A plan update

1. Rewrite each affected day plan so it shows the current plan cleanly, with no struck-through history.
2. Append one entry to "Changes" in the week plan: when, when approved, what changed from what to what, why, and the effect on the week's targets.

A day in the past, or a session already paired with an activity, stays as it is.

## The subjective log

The athlete's own scores, under "How I felt" in the day plan. Every score is optional.

| Score | Scale | When |
|---|---|---|
| Effort | 0 to 10 | per activity; also written to the activity in intervals.icu |
| Overall feel | 1 to 5 | per day |
| Soreness | 1 to 5 | per day |
| Pain | 0 to 10 | per limitation in the athlete profile |
| Illness | flag | per day |
| Note | free text | any time |

Whichever skill hears a score writes it, at once and without asking, including a plain remark such as "tired". Ask at most once each morning and once per activity; carry on without an answer.

## Calendar sync

Any skill about to publish, update or remove a calendar event reads [calendar-sync.md](calendar-sync.md) first.

## Vocabulary

Use these terms, with these meanings, in every file and message.

| Term | Meaning |
|---|---|
| Athlete | the one person being coached |
| Sport mode | which sports a plan covers: triathlon, or a single sport |
| Focus | the sport given priority inside a plan |
| Planned session | one unit of training the plan prescribes for a specific day |
| Activity | one recorded, completed unit of training, as it arrives from the activity source |
| Session review | the assessment of one activity, against its planned session where one exists |
| Day plan, week plan, month plan | the plan at three resolutions |
| Plan update | a change to an existing plan after something happened or circumstances changed |
| Athlete profile | the standing facts about the athlete: goals, anchors, availability, limitations, equipment |
| Athlete rules | the athlete's own rules; they override the coaching rules |
| Coaching rules | the general limits and defaults |
| Daily check | the morning answer to "what is today's session and am I ready for it" |
| Readiness verdict | the daily check's conclusion: go, modify or skip |
| Week review | the assessment of a finished week against its week plan |
| Subjective log | the athlete's own scores for a day |
| Calendar sync | publishing approved planned sessions to intervals.icu |
| Approval | the athlete's explicit acceptance of something a skill proposes to write |

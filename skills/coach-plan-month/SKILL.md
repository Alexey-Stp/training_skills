---
name: coach-plan-month
description: Use when the athlete asks for the next block or month of training to be planned ("plan the next block"), usually in the last week of the current block. Drafts the month plan that week plans are built from.
---

# Month planning

Drafts the next block of whole weeks, normally four, between the athlete's season plan and the week plans.

A month plan sets the shape of its weeks. It holds no planned sessions and reaches the calendar only through the weeks `coach-plan-week` publishes.

## Steps

1. **Load.** Use `coach-data` to find the data folder. Read:
   - the season plan: the phase, key dates and tests for the period;
   - the athlete profile: goals and target races, default sport mode, anchors with their flags, availability exceptions in the period, limitations;
   - the block just ending: its month plan with any "suspended" line, its weeks' "Actual vs plan", its "Block review" if written;
   - the load state, from `coach-data`;
   - the rules, through `coach-rules`.
2. **Phase.** Take it from the season plan and name it in the header. If the season plan gives no phase for the period, stop and ask the athlete, with a recommended answer; the season plan is theirs to maintain. Their answer in chat is enough to go on: the header then reads `Phase (stated by athlete <date>)`, and you ask them to add it to the season plan.
3. **Count back from the races.** Take the next A and B races from the profile and say in the header how many weeks the block's start is from the next one, in whole weeks from the block's first Monday to the Monday of race week. Place the taper the race's priority calls for so that it ends on race day, then fit the block to it: three to five weeks instead of four, so that an easy week does not sit directly before a taper and a load week does not land on race week. Say what was shortened or lengthened under "Why". With no race inside 12 weeks, the block keeps its normal shape.
4. **Sport mode and focus.** State both for the block. A block boundary is where they can change: keep the previous block's unless the season plan, the athlete or an injury says otherwise, and give the reason for a change. If the focus the athlete asks for does not match the phase's name, make the change, keep the phase line as the season plan has it, and flag the mismatch for them to settle in the season plan.
5. **Block shape.** How many load weeks, where the easy week sits, how big it is. An athlete rule on any of these stands; a rule that sizes the easy week does not by itself require one. A percentage "of the previous week" applies to planned load, with hours and volumes scaled to match. Otherwise decide from the phase and the block just ended; with nothing else to go on, use the block-shape default and label it as a convention.
6. **Weeks.** For each week set role, hours, planned load, per-sport volumes and key sessions, and place any test the season plan calls for in the week it names, an easy week included. Where an anchor in use is estimated, or will be more than 8 weeks old before the block ends, and the season plan has no test for it, propose one: in the easy week, or in the first week when the block has none, one test per sport per block. Mark it as a proposal the athlete can drop. Start from what the athlete actually did in the last block, not from what was planned; the first week is measured against the last load week done, not against the easy week. If the last block's final week is not reviewed yet, say so under "Why". Apply what the phase shifts, as `coach-rules` describes. Mark weeks that hold an availability exception.
7. **Check the draft** before showing it. Each line gets an answer:
   - every limit that can be judged at this resolution (long-run progression against the 110% cap and its ceiling, hard sessions and hard swims per week, what each race's priority calls for before and after, a key session or test that already moved once), and every athlete limit and limitation: met;
   - every default: followed, or the departure named with its reason;
   - what the last block's review flagged (a limit passed, a block check tripped, a fading key session): carried into this block, and how.
8. **Write the draft**, then commit: `plan/months/<first Monday of the block>.md` with status `DRAFT`, in the `coach-format` template. "Why this block looks like this" holds the reasoning, every use of judgement and every departure. "Checks for the block" holds the checks the weeks will be held to.
9. **Show the draft** in the message shape below and ask for approval. Stop here.
10. **On approval:** set the status to `APPROVED (<date>)` and commit. Confirm in one line, and say that nothing is on the calendar until the first week is drafted by `coach-plan-week` and approved. If the last block's review later gives a reason to change this block, that is a plan update through `coach-adjust`.

Done when the month plan is `APPROVED`; or when the draft is written and the athlete has been asked.

## Before approval

- **A change the athlete asks for:** revise the draft, re-run step 7, show it again.
- **A change that departs from a default** (for example four load weeks and no easy week): make it, name the default and write the athlete's reason into "Why". Say once what the default is for.
- **A change that passes a limit:** name the limit and the figure, say what the most is that stays inside it, and ask whether they want to go past it. Only an explicit yes to that question counts.
- **A target in fitness, fatigue or form:** these are reported, not planned to, and the plan carries no projected figure for them. Say what the block plans by instead: hours, planned load and key sessions. Nothing is written for a request that is declined.
- **"Looks good", "ok", "go"** in answer to the draft is approval. Silence, a question or a partial comment is not.

## When it is asked early or late

- Earlier than the current block's last week: say the last weeks are not in yet, and draft only if the athlete still wants it; mark the draft as made before the block ended.
- A `DRAFT` for the block already exists: show it again instead of writing a new one, unless the athlete asks for a fresh one.

## Message shape

Short enough for a phone screen, plain lines, no tables. In this order: one line for the block (dates, phase, mode and focus); one line per week; the reasoning in two or three lines; departures and flags, with the load state as one line of context; the request for approval.

```
Block 15 Feb to 14 Mar, DRAFT: run build 2, triathlon, focus run. Next race: 10 km (B), 16 weeks out.

15 Feb  load 1   9:15 h, load 490, run 52 km. Threshold 3 x 8; long run 24. CP test.
22 Feb  load 2   9:45 h, load 520, run 55 km. Threshold 4 x 8; long run 26.
1 Mar   load 3  10:15 h, load 550, run 58 km. Threshold 4 x 8; long run 28.
8 Mar   easy     7:40 h, load 410, run 43 km. 5 km time trial; nothing else hard.

Why: builds on what you did last block, not on what was planned. Threshold restarts at 3 x 8 because rep 4 faded twice. Three load weeks then an easy one is a convention; the easy week at 75% is your rule.

Flags
- Knee check tripped last block. Run volume starts below last block's peak and the knee check stays.
- Fitness 61, fatigue 52, form 9: context only.

Approve this block?
```

## Boundaries

- The season plan and the athlete profile are read here and written elsewhere: the first by the athlete, the second by `coach-setup`.
- A convention (three-to-one weeks, the easy-week percentage, the 10% figure) is called a convention wherever it appears.

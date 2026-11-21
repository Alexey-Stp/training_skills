---
name: coach-nutrition
description: Use when the athlete asks how much to eat or for a calorie or macro target for a day ("what's my calorie target"), how a target was worked out or why it changed, or how what they ate compares with it; after a session review while the day's target is an estimate; and for a scheduled job that sends a target. Gives the day's nutrition target.
---

# Nutrition target

How much energy, carbohydrate, protein and fat a day calls for, from the base day and the training done or still planned.

## Steps

1. **Load.** Use `coach-data` to find the data folder and refresh. Read the day's day plan (planned sessions, readiness verdict, the lines under "Nutrition target"), the activities of that day and of the day before from `coach-data`, the athlete's weight, the athlete rules through `coach-rules`, and `nutrition.md` in `coach-rules`. Every figure and formula comes from that file, as read in this run.
2. **Sort the day's training.**
   - *Done*: an activity is recorded. A planned session and its activity count once, as the activity. An unplanned activity counts too.
   - *Still ahead*: a planned session of today or a later day with no activity. Where today's readiness verdict eased or dropped it, take the minutes and the intensity the verdict gives.
   - *Missed*: the athlete said so, its review says so, or the day is over. It counts nothing.
3. **Same as before?** If the day plan already holds a target and the sort gives the same activities and planned sessions with the same figures, give that target again, add no line, and go to step 8.
4. **Work out the energy**: the base day, then gross and net exercise energy for each activity and each planned session still ahead, as "Exercise energy" in `nutrition.md` says. Keep the source of each figure, in that file's words for it. An activity with no work and no device figure takes the next row that gives one at once; nothing waits for it.
5. **Work out the target**: the load tier with its recovery floor, protein, carbohydrate, fat, and the sum. Where "Before a race" or an athlete rule on weight applies, apply it and say so.
6. **Set the status.** `estimate` while a planned session is still ahead. `final` when none is: each is done or missed, or the day had none. A target from "Before a race" is `final` when given and is not worked out again, since no activity changes it.
7. **Log** for today or a past day: add one line under "Nutrition target" in the day plan, as `coach-format` gives it, and commit. A target for a later day is not logged.
8. **Send the message** in the shape below.
   - An estimate says which planned sessions it waits for, and that the figure is worked out again when they are recorded and reviewed, or when the athlete asks.
   - A target that replaces an earlier one of the same day names the earlier figure and each thing that changed, in one line.
   - Whatever `nutrition.md` asks to be said is said: an assumed base day, a rough rate, a rule that moved a figure.
   - A base day that is derived or assumed, or one the weight check finds off, is offered to `coach-setup` in one closing line, once.

Done when the athlete has the message and, for today or a past day, the day plan holds the line.

## Asked how it was worked out

Give the working in the order of step 4 and step 5, one line each: the base day and where it comes from, each activity and planned session with gross, net and source, the day's load and tier, the grams per kg, then the sum. Explain the target that was given; where the steps would now give another, say so after the explanation.

## Asked which figure is correct

Run the steps first; the target they give is the day's. Say that first, then the earlier figure, its status, and what changed between them, in two or three lines. For an estimate that turned out low or high, say what it was built on. A figure given earlier that these rules do not give is corrected once, and named as a correction.

## Against what was eaten

When the athlete asks how they are doing, or a scheduled job checks the day:

1. Get the food intake for the date from `coach-data`. With no command for it, say that intake is not available and give the target alone.
2. Apply "Food intake against the target" in `nutrition.md`, the incomplete-log rule first.
3. Compare with the latest target. If that is an estimate, say so.
4. Unless the log is incomplete, say what is still to eat: the target minus what was eaten, for each figure that is under and for none that is on target, carbohydrate first on a day with training. One line with a kind of food is enough; a meal plan only when asked.

Done when each of the four figures is given as on target, under or over, or the log is named as incomplete.

## Message shape

Target and status first, then the grams, then one line per part of the energy. Plain lines, no tables, short enough for a phone screen.

```
Target today: 3,242 kcal (estimate, both sessions still ahead)
Carbs 455 g · Protein 126 g · Fat 102 g

Base day 2,350.
Threshold run, planned: about 920 kcal (plan), 810 above base.
Strength, planned: about 110 kcal (history), 80 above base.
Load 88: a moderate day, carbs 6.5 g/kg at 70 kg.

Worked out again when both are recorded and reviewed, or when you ask.
```

Later that day:

```
Target today: 3,251 kcal (final)
Carbs 455 g · Protein 126 g · Fat 103 g

Base day 2,350.
Threshold run, done: about 1,010 kcal (device), 900 above base.
Strength: missed.
Load 74: a moderate day, carbs 6.5 g/kg at 70 kg.

Replaces the earlier 3,332: strength was missed.
```

## Boundaries

- A figure that did not arrive is named as missing, and the target says what it leaves out.
- This skill writes only the "Nutrition target" lines of a day plan. A base day or a weight rule changes through `coach-setup`; the training plan through `coach-adjust`.
- Food is logged elsewhere. This skill reads intake and writes none.
- A target from anywhere else (an older job, a script, an earlier message that these steps did not log) is not the day's. The latest line in the day plan is; say that the other figure was not worked out by these rules. Switching the other source off is the athlete's step.
- A lasting deficit or surplus is said only with the weight evidence `nutrition.md` asks for.
- An illness, a medical diet or a history of disordered eating is for a clinician. Say so.

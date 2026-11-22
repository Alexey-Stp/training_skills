---
name: coach-predict
description: Use when the athlete asks what time they could do for a race or a distance ("predict my 10k", "what can I run a marathon in", "what's my half-distance triathlon time"), whether a goal time is within reach, or what a target race in the profile will take. Gives a prediction, a time with a range and the pace or the legs behind it, from today's anchors and recent results.
---

# Prediction

The time the athlete's fitness today supports for a race: a run of any distance, a swim, or a triathlon as swim, bike, run and transitions.

Every figure and formula is in `prediction.md` in `coach-rules`. Read it in this run before giving any figure; nothing comes from memory or from an earlier message.

A prediction advises. It changes no plan and no goal.

## Steps

1. **Load.** Use `coach-data` to find the data folder and refresh. Read the athlete profile (anchors with their dates and methods, target races with their goals and priorities), the athlete rules through `coach-rules`, and `prediction.md` in `coach-rules`.
2. **Settle the race.** A target race in the profile, or the distance the athlete named. A distance that matches one target race in the profile is that race; "my race" with several means the next A race. Say which one was taken. A triathlon with no distance named and none in the profile is the one question this skill may ask.
3. **Gather the evidence**, for each sport the race has:
   - results of the last 12 weeks, and older ones at the same distance up to 12 months back: the session reviews of races and tests in the day plans, each with its activity's time and distance from `coach-data`, and the best efforts where the data index has that question;
   - the sport's anchor, with its date and method;
   - for "The slow end": the activities of the last 8 weeks, and the load state when the race is within 7 days;
   - for a triathlon: the rides, bricks and earlier triathlons its sections ask for.
4. **Pick the evidence** each figure rests on, best first as `prediction.md` ranks it, and keep its name for the message.
5. **Work out the prediction**: the time, the pace or power behind it, and the range. For a triathlon: each leg, the transitions, the total and its range. Then the cross-check against an older result, where there is one.
6. **Check "The slow end"**, and apply what that section says.
7. **Compare with the goal**, from the profile or the question.
8. **Send the message** in the shape below. Say what the prediction assumes, and name each figure that was assumed and each anchor that is estimated or older than 8 weeks. End with the one thing "What sharpens it" gives.

Done when the athlete has a time, its range, the pace or the legs behind it, and what each rests on; or has been told which evidence is missing and what would supply it.

## No evidence

A sport with none of the four kinds of evidence has no prediction. Say what is missing and offer the test "What sharpens it" names for the sport (its result is recorded through setup). For a triathlon, give the legs that can be predicted and name the one that cannot; no total.

## Message shape

The time first, with its range. Then the pace, or one line per leg. Then, in this order: what it rests on, the slow end where it applies, the goal, what it assumes, the today's-figure line, and what would sharpen it. Plain lines, no tables, short enough for a phone screen.

Samples with invented numbers. A run:

```
5 km: about 19:35 (19:00 to 20:00)
Pace 3:55 /km

From your threshold pace, 4:10 /km, tested 20 Dec.
Assumes a flat course, cool weather, even pace, and that you are rested.

Sharper with: a 5 km race or time trial.
```

A race in the profile with a goal:

```
Autumn half marathon: about 1:30 (1:27 to 1:33)
Pace 4:16 /km

From your threshold pace, 4:10 /km, tested 20 Dec.
Plan on the slow end, 1:33 (4:23 /km): your longest run in 8 weeks is 13 km and the race needs 16. The long runs are still to come.
Goal under 1:35: about 5 min inside, and the slow end still meets it. The goal asks for a threshold of 4:23 /km; you are at 4:10.
Assumes a flat course, cool weather, even pace, and that you are rested.
Today's figure: the race is 8 months away and the anchors will be tested again.

Sharper with: a 10 km race or a half marathon in the build.
```

A triathlon:

```
Olympic-distance triathlon: about 2:22 (2:14 to 2:31)

Swim 1,500 m: 25:30 at 1:42 /100 m
Bike 40 km: 1:10 at 246 W, 34.3 km/h
Run 10 km: 42:50 at 4:17 /km
Transitions: 4 min, assumed

Swim from CSS 1:40, estimated.
Bike power is 88% of FTP 280 W, tested 8 Jan. Your rules name CP, but it is older than 8 weeks. The speed is assumed: no outdoor rides with power on record.
Run from threshold 4:10 /km, tested 20 Dec, with 5% for running off the bike.
Goal under 2:40: about 18 min inside, and the slow end still meets it.
Assumes a flat course, a wetsuit swim, even pace, and that you are rested.
Today's figure: the race is 5 months away and the anchors will be tested again.

Sharper with: two outdoor rides of 90 minutes or more with power.
```

## Boundaries

- A prediction is given with its range, every time. A single time with no range is not a prediction.
- This skill writes nothing. A new anchor goes through `coach-setup`, a change of goal too, and the plan through the planning skills.
- Pacing on the day, fuelling and the taper are outside a prediction: the taper is in `coach-rules`, fuelling in the race's planned session.

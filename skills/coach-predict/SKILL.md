---
name: coach-predict
description: Use when the athlete asks what time they could do for a race or a distance ("predict my 10k", "what can I run a marathon in", "what's my half-distance triathlon time"), whether a goal time is within reach, or what a target race in the profile will take. Gives a prediction, a time with a range and the pace or the legs behind it.
---

# Prediction

The time the athlete could race today: a run of any distance, or a triathlon as swim, bike, run and transitions. It is built from the best evidence of what the athlete can do, then moved by what training has shown since.

Every figure and formula is in `prediction.md` in `coach-rules`. Read it in this run before giving any figure; nothing comes from memory or from an earlier message.

A prediction advises. It writes nothing, and changes no plan and no goal.

## Steps

1. **Load.** Use `coach-data` to find the data folder and refresh. Read the athlete profile (anchors with their dates and methods, target races with their goals), the athlete rules through `coach-rules`, and `prediction.md` in `coach-rules`.
2. **Settle the race.** A target race in the profile, or the distance the athlete named. A distance that matches one target race in the profile is that race; "my race" with several means the next A race. Say which one was taken. A triathlon with no distance named and none in the profile is the one question this skill may ask.
3. **Gather what `prediction.md` reads**, for each sport the race has, over the spans it gives:
   - results: the session reviews of races and tests in the day plans, each with its activity's time and distance from `coach-data`;
   - best efforts, where the data index has that question;
   - the sport's anchor, with its date and method;
   - the session reviews of threshold sessions, the longest run and the longest ride, and the load state today and on the day of the evidence;
   - for a triathlon: the outdoor rides, bricks and earlier triathlons its section asks for.
4. **Base time.** Pick the evidence each run or leg rests on, as "Evidence for the base time" ranks it, and work out the base time.
5. **Adjust.** Go through every row of "What training since then shows" and apply each one that holds. Keep each adjustment and its figure for the message.
6. **Range, cross-check and goal**, as their sections say. For a triathlon: each leg, the transitions, the total and its range.
7. **Send the message** in the shape below.

Done when the athlete has a time and its range, the pace or the legs behind it, the evidence each rests on, and every adjustment with its figure, or "none" for each row checked; or has been told which evidence is missing and what would supply it.

## No evidence

A sport with no evidence of any kind has no prediction. Say what is missing and offer what "What sharpens it" names for the sport (a test's result is recorded through setup). For a triathlon, give the legs that can be predicted and name the one that cannot; no total.

## Message shape

The time first, with its range. Then the pace, or one line per leg. Then, in this order: what it rests on, what training since then shows (each row that moved the time, the others in a few words), the goal, what it assumes, the line "Today's figure" asks for, and what would sharpen it. Plain lines, no tables, short enough for a phone screen.

Samples with invented numbers. A race in the profile with a goal:

```
10 km road race, 6 Jun: about 40:45 (39:30 to 42:00)
Pace 4:05 /km

From your threshold pace, 4:10 /km, tested 20 Dec.
Since then: threshold sessions sit on that pace. Fitness 61, up from 58: no change, a test would show the gain.
Goal under 43:00: about 2 min inside, and the whole range meets it. The goal asks for a threshold of 4:23 /km.
Assumes a flat course, cool weather, even pace, and that you are rested.
Today's figure: the race is 4 months away and the anchors will be tested again.

Sharper with: a 10 km test or race.
```

A distance the athlete named:

```
Marathon: about 3:15 (3:05 to 3:25)
Pace 4:37 /km

From your threshold pace, 4:10 /km, tested 20 Dec: 3:08.
Since then: 4% slower for the long run, a convention. Your longest in 8 weeks is 19 km, 45% of the distance; at 30 km it goes. Threshold sessions sit on the pace; fitness is up, and a test would show the gain.
Assumes a flat course, cool weather, even pace, and that you are rested.

Sharper with: a half marathon race.
```

A triathlon:

```
Half-distance triathlon: about 5:06 (4:48 to 5:25)

Swim 1,900 m: 32:55 at 1:44 /100 m
Bike 90 km: 2:48 at 215 W, 32.1 km/h
Run 21.1 km: 1:39 at 4:42 /km
Transitions: 6 min, assumed

Swim from CSS 1:40, estimated.
Bike power is 78% of CP 275 W, tested 2 Oct, older than 8 weeks; FTP was tested on 8 Jan, but your rules name CP. The speed is assumed: no outdoor rides with power on record.
Run from threshold 4:10 /km, tested 20 Dec, with 8% for running off the bike.
Since then, by convention: bike 2% slower, your longest ride is 2 h against a 2:45 leg; run 2% slower, your longest run is 13 km of 21. Threshold sessions sit on the anchors; fitness is up.
Assumes a flat course, a wetsuit swim, cool weather, even pace, and that you are rested.

Sharper with: a new CP test.
```

## Boundaries

- A prediction is given with its range, every time.
- A new anchor goes through `coach-setup`, a change of goal too, and the plan through the planning skills.
- Pacing on the day, fuelling and the taper are outside a prediction: the taper is in `coach-rules`, fuelling in the race's planned session.

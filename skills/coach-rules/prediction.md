# Race prediction

The defaults behind a prediction: the time the athlete's fitness today supports for a race. An athlete rule replaces any figure here.

It covers a run of any distance, a swim, and a triathlon. A ride on its own has no prediction: say so.

Where the figures come from: the distance formula is Riegel's (1981). The bike shares of FTP and the run-off-the-bike factors are the ranges coaches commonly use for age-group triathletes. Everything else is convention: this suite's own choice. All of it predicts a rested athlete on a flat course in cool weather, pacing evenly.

## Evidence, best first

Each figure rests on the first of these that exists. Name it in the message.

1. **A result at the same distance** in the last 12 weeks: a race or a time trial, raced rested and on its own. It is the prediction, scaled as "Fitness since" says.
2. **A result at another distance** in the last 12 weeks, between a fifth of the race distance and five times it: through the distance formula. A result raced unrested, or as a leg of a triathlon, counts here and takes the wide range.
3. **A tested anchor** of the sport, 8 weeks old or less: through "From an anchor".
4. **An anchor that is estimated, derived or older than 8 weeks**: as 3, with the wide range. A swim leg of a triathlon of the same distance in the last 12 months ranks above an estimated CSS.

An older result at the same distance, up to 12 months back, is a cross-check: scale it as "Fitness since" says, for each leg and for the total of a triathlon, and where it differs from the prediction by more than 3%, give both and say which one the prediction rests on. A leg that itself rests on the older result is cross-checked against the sport's anchor instead.

## The distance formula

For a run: T2 = T1 x (D2 / D1) ^ 1.06, with 1.08 when D2 is longer than 30 km. A swim does not use it: it rests on a result at the same distance or on CSS.

## From an anchor

- **Run:** the threshold pace is the pace of a 60-minute race. D1 is the distance covered in 60 minutes at that pace, T1 is 60 minutes; then the distance formula.
- **Swim:** race pace per 100 m is CSS x 1.00 up to 750 m, x 1.02 up to 1,500 m, x 1.04 up to 1,900 m, x 1.07 up to 3,800 m. In open water with a wetsuit, or in a pool; in open water without a wetsuit add 4 s per 100 m.
- **Bike:** see "The bike leg".

## Fitness since

A result from before the current anchor value is scaled by the same anchor, then and now: time x (pace now / pace then) for a run or a swim, so a faster threshold gives a shorter time; time x (FTP then / FTP now) ^ (1/3) on the bike. With no value on record for "then", the result is used unscaled and that is said.

## The range

| What the figure rests on | Range around the prediction |
|---|---|
| Evidence 1 | 2% |
| Evidence 2 or 3 | 3% |
| Evidence 4, a result raced unrested or as a leg, an assumed pace or speed, or a bike speed from a single ride | 6% |
| A marathon, unless on evidence 1 | 5% at least |
| A triathlon as a whole | 4%; 6% when any leg's pace or speed takes the 6% row; 6% at least for a full distance |

## The slow end

Give the prediction and its range as worked out, then name the slow end of the range as the figure to plan on, when any of these holds:

- **Endurance for the distance is not shown** in the activities of the last 8 weeks:

  | Race | Shown when |
  |---|---|
  | Half marathon | the longest run is 16 km or more |
  | Marathon | the longest run is 28 km or more, and three runs or more of 24 km or more |
  | Half-distance triathlon | a ride of 2 h 30 or more, and a run of 16 km or more |
  | Full-distance triathlon | a ride of 4 h 30 or more, and a run of 24 km or more |

  For a race more than 8 weeks away, say also that the long sessions are still to come.
- **A gap** of 15 days or more with no activity in the sport in the last 8 weeks.
- **Form:** the race is within 7 days and form is below -10. Form changes no figure; the message then says that the athlete would not start rested, in place of assuming that they are.

## A triathlon

Predict each leg, add the transitions, and give the total. Add unrounded legs. Standard distances: sprint 750 m / 20 km / 5 km; Olympic 1,500 m / 40 km / 10 km; half 1,900 m / 90 km / 21.1 km; full 3,800 m / 180 km / 42.2 km. A race's own distances, where the profile holds them, replace these.

### The bike leg

1. **The anchor:** the bike anchor the athlete rules name. Where that one is older than 8 weeks and another bike anchor is tested and newer, use the newer one and say so.
2. **Target power** as a share of it: sprint 92%, Olympic 88%, half 78%, full 68%. Where the leg comes out longer than 3 hours for a half or 6 hours for a full, use 75% or 65% and work it out again.
3. **Speed at that power**, first that exists:
   - outdoor rides with power of 90 minutes or more in the last 12 weeks: scale each ride's average speed to the target power by (target power / the ride's average power) ^ (1/3), and take the median (of one ride, that ride). A ride on a trainer has no usable speed;
   - the bike leg of a triathlon of the same distance in the last 12 months, its time scaled as "Fitness since" says;
   - neither: assume 32 km/h at 200 W on a road bike on the flat and scale the same way. Say that it is assumed.
4. Time = distance / speed. A course with long climbs is slower than this: say that the figure is for a flat course.

### The run off the bike

The stand-alone prediction for the distance, with its time longer by: sprint 3%, Olympic 5%, half 8%, full 15%. The athlete's own figure replaces these when the last 12 weeks hold two bricks or more whose runs can be compared with a stand-alone run of those weeks.

### Transitions

Both together, from the athlete's last triathlon of the same distance in the last 24 months. Otherwise assumed: sprint 3 min, Olympic 4 min, half 6 min, full 10 min.

## Today, not race day

The prediction is for the fitness the athlete has today. It is not projected forward. For a race more than 4 weeks away, say that it is today's figure and that the anchors will be tested again before the race. A distance with no date is taken as raced today.

## Against a goal

A goal from the profile, or one named in the question. Give the gap between the prediction and the goal in time, and say whether the slow end of the range still meets it; where the goal lies inside the range, say that it is in the balance. For a run that rests on an anchor, add what the goal asks of the threshold pace by the same formula.

## What sharpens it

Name one thing: what would replace the weakest evidence in the prediction; on a tie, the weakest of the longest leg. A run: a race or time trial near the distance, or a 5 km time trial when there is no tested anchor. A swim: a CSS test. A bike leg: an FTP test when the anchor is the weak part, outdoor rides of 90 minutes or more with power when the speed is. Within 4 weeks of the race, say that nothing will sharpen it before the day.

## Rounding

Work with unrounded figures. In a message: a time to the nearest 5 seconds up to an hour and to the nearest minute beyond; the ends of a range to the nearest 30 seconds up to an hour and to the nearest minute beyond.

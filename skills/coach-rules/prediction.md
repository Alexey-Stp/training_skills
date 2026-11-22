# Race prediction

The defaults behind a prediction: the time the athlete could race today. An athlete rule replaces any figure here.

It covers a run of any distance and a triathlon. A ride or a swim on its own has no prediction: say so, and offer the triathlon in the profile that holds that leg, where there is one.

Where the figures come from: the distance formula is Riegel's (1981). The bike shares of the anchor and the run-off-the-bike factors are ranges coaches commonly use for age-group triathletes. Everything else is convention: this suite's own choice. That includes every adjustment under "What training since then shows"; load figures as predictors of performance are contested, so say "convention" when one of them moves a time.

A prediction is built in three passes: a base time from the best evidence, adjustments from what training has shown since, and a range around the adjusted time.

## Evidence for the base time

Each run, and each leg of a triathlon, rests on the first of these that exists. Name it in the message.

| Kind | What it is | Range, each side |
|---|---|---|
| Same-distance result | a race or a test at the race distance in the last 12 weeks, raced rested and on its own | 2% |
| Other-distance result | a race or a test in the last 12 weeks at between a fifth of the race distance and five times it, through the distance formula. One raced unrested, or as a leg of a triathlon, takes 6% | 3% |
| Tested anchor | the sport's anchor, tested, 8 weeks old or less | 3% |
| Weak anchor | an anchor that is estimated, derived or older than 8 weeks | 6% |

- **Best efforts.** A best effort in training in the last 8 weeks is rarely all-out, so it is a floor. Carry it to the race distance by the distance formula; where that is faster than the base time, it becomes the base time, with a range of 5%. With no evidence in the table, a best effort alone gives the base time, also at 5%.
- **A marathon** takes 5% at least, unless on a same-distance result.
- **A test and its anchor.** A test that set the current anchor is not a separate result: rest on the anchor.
- **An older result** at the same distance, up to 12 months back, is a cross-check. Scale it as "Anchor change" says, for each leg and for the total of a triathlon. Where it differs from the prediction by more than 3%, give both and say which one the prediction rests on.

## The distance formula

For a run: T2 = T1 x (D2 / D1) ^ 1.06.

## From an anchor

- **Run:** the threshold pace is the pace of a 60-minute race. D1 is the distance covered in 60 minutes at that pace, T1 is 60 minutes; then the distance formula.
- **Swim leg:** race pace per 100 m is CSS x 1.00 up to 750 m, x 1.02 up to 1,500 m, x 1.04 up to 1,900 m, x 1.07 up to 3,800 m, with a wetsuit. Without one add 4 s per 100 m. The swim leg of a triathlon of the same distance in the last 12 months ranks above a weak CSS.
- **Bike leg:** see "A triathlon".

## Anchor change

A result older than the current anchor value is scaled by that anchor, then and now: time x (pace now / pace then) for a run or a swim; time x (power then / power now) ^ (1/3) on the bike. With no value on record for "then", the result is used unscaled and that is said.

## What training since then shows

Each of these moves the base time. Apply every one that holds, multiply them, and stop at 10% in all. Name each in the message with its figure.

| Sign | Read from | Moves the time |
|---|---|---|
| **Threshold sessions** | the session reviews of the last 4 weeks with 20 minutes or more of work at threshold in the sport | only where the base time rests on an anchor. Two sessions or more held faster than target by 1.5% or more, under their caps, or two or more missed by 1.5% or more: work the base time out again from the midpoint between the anchor and the mean pace or power those sessions held. The range stays the anchor's. Fewer than two such sessions: none; say that the sessions sit on the anchor, or that there are too few to tell |
| **Long run** | the longest run of the last 8 weeks as a share of the race's run distance, for a run of 15 km or more | 70% or more: none. 55 to 69%: 2% slower. 40 to 54%: 4% slower. Under 40%: 7% slower. A longest run of 2 h 30 or more, the long-run ceiling of `coach-rules`, counts as 55% at least |
| **Long ride** | the longest ride of the last 8 weeks, indoors or out, as a share of the predicted bike time, for a half or full distance | 75% or more: none. 50 to 74%: bike 2% slower. Under 50%: bike 4% slower |
| **Fitness** | the load state's fitness today against the date of the evidence the run or leg rests on | down by 10 to 20%: 2% slower. Down by more than 20%: 4% slower. Down by less, steady, or no date to compare with: none. Up: none; say that a test would show the gain. Where this row and the long-run row both apply to a run, take the larger of the two only |
| **Form** | the load state's form, for a race today or in the next 2 days | below -10: 2% slower, and the message says the athlete would not start rested. Further out, none: the figure assumes the taper |

The long-run and long-ride rows describe today. For a race more than 8 weeks away, apply them and say that the long sessions still to come would remove them.

## A triathlon

Predict each leg, add the transitions, and give the total from unrounded legs. A race's own distances, where the profile holds them, replace the standard ones.

| Distance | Swim / bike / run | Bike power, share of the anchor | Run off the bike, time longer by | Both transitions, assumed |
|---|---|---|---|---|
| Sprint | 750 m / 20 km / 5 km | 92% | 3% | 3 min |
| Olympic | 1,500 m / 40 km / 10 km | 88% | 5% | 4 min |
| Half | 1,900 m / 90 km / 21.1 km | 78%; 75% when the leg at 78% comes out over 3 hours | 8% | 6 min |
| Full | 3,800 m / 180 km / 42.2 km | 68%; 65% when the leg at 68% comes out over 6 hours | 15% | 10 min |

- **The bike anchor** is the one the athlete rules name, or else FTP. It is a tested or a weak anchor like any other. Where it is weak and another bike anchor is tested and newer, say so; the rule still decides.
- **Bike speed at the target power**, first that exists:
  1. outdoor rides with power of 90 minutes or more in the last 12 weeks: scale each ride's average speed to the target power by (target power / the ride's average power) ^ (1/3), and take the median. A ride on a trainer has no usable speed;
  2. the bike leg of a triathlon of the same distance in the last 12 months, its time scaled as "Anchor change" says;
  3. neither: assume 32 km/h at 200 W on a road bike on the flat and scale the same way. Say that it is assumed.

  Time = distance / speed. Say that the figure is for a flat course.
- **The run leg** is the stand-alone prediction for its distance, with the long-run adjustment, then longer by the table's share. The athlete's own share replaces the table's when the last 12 weeks hold two bricks or more whose runs can be compared with a stand-alone run of those weeks.
- **Transitions** come from the athlete's last triathlon of the same distance in the last 24 months, or else from the table.
- **The range of the total**, each side: 4%. 6% when any leg rests on a weak anchor, on an assumed speed, or on fewer than three rides; and for a full distance.

## Today's figure

The prediction is what the athlete could race today. Gains the plan hopes for are not added. For a race more than 4 weeks away, say that it is today's figure and that the anchors will be tested again before the race. A distance with no date is taken as raced today.

## Against a goal

A goal from the profile, or one named in the question. Give the gap between the prediction and the goal in time, in seconds when it is under a minute, and say where the goal lies: met by the whole range, inside the range, or outside it. Judge that on unrounded figures. For a run that rests on an anchor, add the threshold pace the goal asks for by the same formula, before adjustments.

## What sharpens it

Name one thing: what would replace the weakest evidence; on a tie, that of the longest leg, and the anchor before the speed. A run: a race or a test near the distance. A swim leg: a CSS test. A bike leg: a test of the anchor when it is weak, outdoor rides of 90 minutes or more with power when the speed is. With nothing weak: a race near the distance. Within 4 weeks of the race, say that nothing will sharpen it before the day.

## What it assumes

Say it in one line: a flat course, cool weather, even pace, and a rested athlete (left out when the form row applied); for a triathlon, a wetsuit swim.

## Rounding

Work with unrounded figures. In a message: a time to the nearest 5 seconds up to an hour and to the nearest minute beyond; the ends of a range to the nearest 30 seconds up to an hour and to the nearest minute beyond; a pace to the second, power to the watt, speed to 0.1 km/h.

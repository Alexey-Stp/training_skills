# Nutrition target

The defaults behind a day's nutrition target. An athlete rule replaces any figure here.

Where the figures come from:

- The carbohydrate bands of the moderate, high and very high tiers and the fat range of 20 to 35%: the 2016 position stand of the American College of Sports Medicine, the Academy of Nutrition and Dietetics and Dietitians of Canada.
- Protein: that stand gives 1.2 to 2.0 g/kg and the position stand of the International Society of Sports Nutrition 1.4 to 2.0, with more in a deficit. The figures here sit inside both.
- Carbohydrate before a race: the same 2016 stand, 10 to 12 g/kg a day for 36 to 48 hours before an event longer than 90 minutes.
- Energy availability of 30 kcal per kg of fat-free mass as the lower bound: the IOC consensus on low energy availability.
- Every other figure is convention: this suite's own choice, from use. That covers the load cut-offs, the rest and light tiers, the recovery floor, the factor on resting metabolism, the rough rates, the size of a deficit, and the tolerances of the intake check.

## The order

1. Energy = base day + the net exercise energy of every activity of the day and every planned session still ahead.
2. Carbohydrate and protein in grams per kg of body weight, from the day's load tier.
3. Fat takes the energy that is left, inside its range.
4. The target in kcal = protein x 4 + carbohydrate x 4 + fat x 9, so the four figures always agree.

Body weight is the weight the athlete profile says how to compute. Grams are whole numbers.

## Base day

What the athlete uses on a day with no training: resting metabolism plus ordinary daily life. Take the first that is there:

1. **Stated**: an athlete rule gives it.
2. **Derived**: food intake is logged on at least 28 of the last 56 days (a day the incomplete-log rule below leaves out does not count) and the 7-day average weight moved less than 1% over that time. Base day = mean intake minus mean net exercise energy over the logged days.
3. **Assumed**: Mifflin-St Jeor resting metabolism (10 x kg + 6.25 x cm - 5 x age, plus 5 for a man or minus 161 for a woman) x 1.45. Age is this year minus the year of birth. Where the profile does not say man or woman, use minus 78, say so, and point to `coach-setup` to record it. Say `assumed` each time it is used.

The base rate is the base day divided by 1,440: kcal a minute.

## Exercise energy

Gross energy of one activity or one planned session. Take the first row that gives a figure.

| Kind | Done: an activity | Still ahead: a planned session |
|---|---|---|
| Ride with power | kcal = the work in kJ. At about 24% gross efficiency 1 kJ of work costs about 1 kcal | from the steps: minutes x watts x 0.06 = kJ, a range at its middle, a percentage step from the anchor the session's `Anchors:` line or the athlete rules name. With no steps: 0.36 x FTP x the square root of (planned load x hours) |
| Run | the device's kcal; without one, 1 kcal per kg per km | 1 kcal per kg per km, the distance from the steps' paces and minutes: a percentage is of the threshold speed, a range at its middle. An easy run with no pace in its steps, or one a verdict turned easy, is taken at 70% of the threshold speed |
| Anything else | the device's kcal | from history: the athlete's own median kcal a minute over the last ten activities of that sport of the same kind (easy with easy, hard with hard), times the planned minutes |
| No figure from the rows above | minutes x kg x a rate: swim 0.12, ride 0.11, strength 0.06, anything else 0.08. Say that it is rough | the same |

Net exercise energy = gross minus the base rate times the minutes trained, and never below 0. The base day already covers those minutes. Work with unrounded figures; in a message the kcal of one activity or planned session are rounded to the nearest 10 and given as "about".

- Load is not turned into kcal by a fixed factor. A long easy ride costs about twice the energy per point of load that a short hard one does.
- Work on a power meter is measured. A device's kcal is estimated from heart rate and is less exact; the rates in the last row are rougher still. Name the source of each figure with one of five words: `power meter`, `device`, `plan` (worked out from the planned steps), `history` or `rough rate`.
- A device's kcal is taken as gross: resting energy included. Where an athlete rule says the device reports active energy only, nothing is subtracted for those minutes.
- Carbohydrate eaten during training counts towards the day's target. It is not added on top.

## Load tier

The day's load is the load of its activities plus the planned load of its sessions still ahead. A session a readiness verdict eased has the load its new minutes and intensity give: hours x the square of the intensity x 100, an easy session at 0.7 of threshold.

| Tier | Day's load | Carbohydrate, g/kg | Band, g/kg | Protein, g/kg |
|---|---|---|---|---|
| Rest | under 15 | 4 | 3 to 5 | 1.8 |
| Light | 15 to 59 | 5 | 4 to 6 | 1.8 |
| Moderate | 60 to 119 | 6.5 | 5 to 7 | 1.8 |
| High | 120 to 199 | 8 | 6 to 10 | 2.0 |
| Very high | 200 and above | 10 | 8 to 12 | 2.0 |

- **Recovery floor**: the tier is at most two below the tier yesterday's own load gave (its planned load, where yesterday is still ahead). After a very high day, today is at least moderate.
- Protein stays inside 1.6 to 2.2 g/kg; the top of that is for a day with a deficit.

## Fat

Fat = (energy - protein x 4 - carbohydrate x 4) / 9, kept between 20% and 35% of the target's kcal and at 0.8 g/kg or more. It is a range to land in, not a cap in grams. With K the kcal of protein and carbohydrate together, the floor is the larger of 0.8 g/kg and K / 36 grams, rounded up, and the ceiling is K / 16.7 grams, rounded down. Where a rule below moves carbohydrate, move it in whole grams and work fat out again each time.

- **Under the floor**: raise fat to the floor. If the target then stands more than 5% above the energy, lower carbohydrate inside the tier's band, and fat with its floor, until the target is within 5% or the bottom of the band is reached. Say so when it still stands above. Where the recovery floor set the tier, carbohydrate is not lowered: the target stands above the energy, which is what that floor is for.
- **Over the ceiling**: raise carbohydrate until fat is at its ceiling. Carbohydrate may leave the tier's band for this, up to 12 g/kg. Past that, fat takes the rest; say so.

A rule here that moved carbohydrate off the tier's figure is named in the message and in the log.

## Before a race

For an A or B race expected to last longer than 90 minutes, these replace the tier on the two days before it.

| Carbohydrate | Protein | Fat |
|---|---|---|
| 10 g/kg | 1.6 g/kg | 0.6 g/kg |

The target is the sum of these, whatever the energy comes to, and "Fat" above does not apply. Add: low fibre, familiar foods, and on race morning 1 to 4 g/kg of carbohydrate 1 to 4 hours before the start. Race day itself follows the tier.

## Holding, losing or gaining weight

The target holds weight. A deficit or a surplus comes only from an athlete rule that gives the amount.

**Limit**: a deficit is at most 500 kcal a day, and there is none on a day with a hard session, a session longer than 90 minutes or a race, on the two days before an A or B race, or on a return day after illness, and none for an athlete who reports an illness, a medical diet or a history of disordered eating. Where the athlete profile holds fat-free mass, (target minus net exercise energy) / kg of fat-free mass stays at 30 or above.

On a day with a deficit the energy is the holding energy minus the deficit. Set protein first, at 2.2 g/kg; then fat at its floor at least. The 5% allowance of "Fat" does not apply: lower carbohydrate until the target equals the energy or the bottom of the band is reached. Say how much of the deficit was not reached.

## Checking the base day against weight

When the 7-day average weight has moved more than 1% over 28 days while logged intake was on target, the base day is off by about (kg moved x 7,700 / 28) kcal a day. The corrected figure is the base day less that amount when weight rose, plus it when weight fell. Less evidence than that changes nothing: one day short or over is a note for that day.

## Food intake against the target

| Figure | On target when |
|---|---|
| Energy | from 10% under to 15% over |
| Carbohydrate | at 90% of the target or more. On a day with training this comes first |
| Protein | at 1.6 g/kg or more, or within 5 g of its target; above 2.2 is not a fault |
| Fat | 20% to 35% of what was eaten, or under 20% with 0.8 g/kg reached. On a day under "Before a race": at or under its target |

**Incomplete log**: under 1,500 kcal or fewer than five items logged is a log that is not finished. Say that, judge nothing from it, and give the target alone.

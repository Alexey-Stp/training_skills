# Athlete profile

Written only by `coach-setup`. All values in this example are invented.

## 1. Basics

- Born: 1985
- Height: 180 cm
- Timezone: Europe/London
- Weight: computed, 7-day average of the wellness record. Not typed in.
- HRV baseline: computed, 60-day average. Not typed in.
- Resting heart rate baseline: computed, 30-day average. Not typed in.

## 2. Sport mode

- Default sport mode: triathlon

## 3. Goals and target races

| Priority | Race | Date | Goal |
|---|---|---|---|
| A | Autumn half marathon | 2027-10-10 | under 1:35 |
| B | 10 km road race | 2027-06-06 | under 43:00 |
| A | Olympic-distance triathlon | 2027-07-18 | under 2:40 |

## 4. Anchors

| Anchor | Value | Date | Method | Source | Flag |
|---|---|---|---|---|---|
| Bike FTP | 280 W | 2027-01-08 | tested (ramp test) | intervals.icu | |
| Bike CP / W′ | 275 W / 20 kJ | 2026-10-02 | tested (3 and 12 min) | stated by athlete | older than 8 weeks |
| Run threshold pace | 4:10 /km | 2026-12-20 | tested (5 km time trial) | intervals.icu | |
| Run LTHR | 168 bpm | 2026-12-20 | derived (5 km time trial) | intervals.icu | |
| Max HR | 186 bpm | 2026-12-20 | tested (5 km time trial) | intervals.icu | |
| Swim CSS | 1:40 /100 m | 2026-11-22 | estimated | imported: SEASON-PLAN.md | estimated, untested |

## 5. Zones

Zones are read from intervals.icu sport settings. Only what intervals.icu does not hold is written here.

- Bike targets derive from: see `ATHLETE-RULES.md`.

## 6. Availability

Weekly template:

| Day | Time available | Usual times | Fixed commitments | Facility access |
|---|---|---|---|---|
| Mon | 60 min | evening | | |
| Tue | 90 min | evening | | |
| Wed | 90 min | evening | | pool closed |
| Thu | 2 h | lunch and evening | | pool 15 min away |
| Fri | rest day | | | |
| Sat | 3 h | morning | | |
| Sun | 3 h | morning | | |

Dated exceptions:

- 2027-02-12 to 2027-02-14: travelling, running only

## 7. Limitations

| Limitation | Since | Athlete rule it triggers |
|---|---|---|
| Right knee | 2026-08 | Limits: the two knee pain rules |
| Lower back | 2026-10 | Limits: aero position rule |

Daily pain scores are logged in each day plan under "How I felt", not here.

## 8. Equipment

- Indoor trainer with power, road bike with power meter
- GPS watch with wrist and chest-strap heart rate
- 25 m pool; no open water before May

## Change log

- 2027-01-10: Bike FTP 272 W to 280 W (ramp test). Zones recalculated in intervals.icu.
- 2026-12-21: Run threshold pace 4:15 to 4:10 /km (5 km time trial).
- 2026-11-22: Profile created by first setup run.

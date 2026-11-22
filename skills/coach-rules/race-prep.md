# Race preparation

What is planned between today and a target race, beyond what "Races" in `coach-rules` and [season.md](season.md) already fix: how far out decides which plan carries the work, what the last weeks and days hold, how form shapes a taper, and what to do when illness, a late entry or a clash gets in the way. An athlete rule replaces any figure here.

The taper's size is the taper default in `coach-rules` (from the taper meta-analysis that default rests on). Everything else here is convention: this suite's own choice. Say "convention" when form moves a taper.

## How far out

Count whole weeks from the coming Monday to the Monday of race week. T is the number of taper weeks "Races" gives the race, race week included (B and C: 1; a race with no priority yet: as for an A race).

| The race is | The work is carried by | What to settle now |
|---|---|---|
| Beyond the current block and the next | the season plan | the race's week roles and phases; where the build starts; nothing by day |
| Inside the current block or the next, with more than T weeks to go | the month plan | the load weeks left, the key sessions, the last long session and the taper weeks |
| T weeks away or less | the week plans and day plans | the taper and race week by day |

## Choosing priorities

The priority is the athlete's to set; this is what to recommend, and when to ask. Ask once, in one message, only when the goals in the profile do not tell which race the season is for.

- **A:** the race the season is built for. Two in twelve months as a rule, three at most. Eight load weeks or more between the recovery of one and the taper of the next is comfortable; fewer than four is a clash.
- **B:** a race worth a short rest but not a taper. It fits best 3 to 6 weeks before an A race of the same sport or of one of its legs, at the same distance or shorter.
- **C:** a race trained through: one the athlete enters for practice.
- **A late entry:** a race entered with fewer than T + 4 weeks to go is recommended as B, or as C when "Ready for the distance" is not met. Say why.
- A clash between races, and a race inside another's taper or recovery, is settled as "Clashes" in [season.md](season.md) says.

## Ready for the distance

Before preparing for a run of 15 km or more, or a half or full triathlon, check whether the long sessions can get there. Use the shares in "What training since then shows" in [prediction.md](prediction.md): a longest run of 70% of the race's run, and for a half or full triathlon a longest ride of 75% of the bike time (from the goal, or from `coach-predict`).

1. Take the longest run and ride the long-run limit and the long-ride default of `coach-rules` count from.
2. Grow each by that limit and that default, week by week, through the load weeks from this one to the latest day "The last long and hard sessions" allows. Easy weeks do not grow.
3. Where one cannot reach its share, say so with the figures: what it reaches and what the race asks. Recommend the race as B or C, or as a training day, and leave the choice to the athlete. The limits are not stretched to fit a race.

A long run that stops at the long-run ceiling is as ready as the rules allow: say that the ceiling stands and what the race will ask beyond it.

## Key sessions in the build

One line each for the month plan's rows, by the next A or B race the block builds to; the week plan writes the sessions.

| Race | Each load week holds |
|---|---|
| 10 km | reps at threshold, and reps at 10 km pace in the last 6 weeks |
| Half marathon | a tempo run, and a long run with its last third at race pace every second week |
| Marathon | a long run with blocks at marathon pace every second week, with the fuelling of race day practised in it |
| Sprint or Olympic triathlon | a brick, bike intervals at race power, and open water once it is available |
| Half or full triathlon | a long ride with blocks at race power and race fuelling, a brick off it every second week, and open water once it is available |

## The last long and hard sessions

| Before race day | Latest day for it |
|---|---|
| The longest run | marathon 21 days, half marathon 14, shorter races 10. A triathlon's run counts as a run of its distance |
| The longest ride | full distance 21 days, half distance 14, shorter 10 |
| The last hard session at full length | 10 days for an A race with two taper weeks or more, 6 otherwise |

A session of one of these kinds that the plan holds later than this is proposed for a move earlier or a cut, through a plan update.

## The taper by week

Volume is cut against the average of the last two load weeks. Race week's cut covers Monday to the day before the race; the race is not counted. Intensity stays; the hard sessions get shorter, not slower. The number of sessions stays at 80% or more of a load week's. Every session is shortened by about the week's share, the long session by more.

| Taper | Cut |
|---|---|
| One week | 50% |
| Two weeks | 41%, then 60% in race week |
| Three weeks | 41%, 50%, then 60% in race week |

"Form in the taper" moves these inside the default's range.

## Race week by day

Counted back from race day, for an A race. A day with nothing in its row is easy, 30 to 45 minutes. A B race keeps its week from "Races" and takes only the day-before row.

| Day | Holds |
|---|---|
| 6 and 5 days before | easy sessions; one of them may be the week's short hard session |
| 4 or 3 days before | the short hard session, if not done yet: half the work of a normal one or less, at race pace or power |
| 2 days before | rest, or 30 minutes very easy |
| The day before | openers: 20 to 30 minutes easy with 4 to 6 pickups of 20 to 30 seconds. A triathlon: a short swim, a short ride with pickups that also checks the bike, and an optional 10-minute run |
| Race day | the race, as its planned session gives it |

- An athlete rule on the week's shape (a long-run day, a fixed rest day) stands. Where it cannot hold beside this table or beside "The last long and hard sessions", name the clash, recommend what the table gives, show in one line what keeping the rule would look like at the week's cut, and let the athlete choose.
- The day before and race morning: food is `coach-nutrition`'s "Before a race". Kit laid out, the bike checked, transitions walked, nothing new.
- Targets for the race come from its planned session. Offer `coach-predict` where the athlete asks what to expect.

## Form in the taper

Read the load state when the taper starts and again on the Monday of race week.

| Form | Taper |
|---|---|
| Below -20 | the deepest cut the default allows, 60%, from the first taper week; the first two days easy |
| -20 to -10 | as the table gives it |
| Above -10 | as the table gives it |
| Still below -10 on the Monday of race week | race week's short hard session is cut to 10 minutes of work or less; the openers stay |

Form names the depth of the cut. It adds no session and no load. Inside a taper this stands over the line in `coach-adjust` that one load figure alone is not a reason for a change.

## Illness or a gap before a race

Inside the three weeks before a race, these come first, in this order:

1. The fever limit and the return it sets, as `coach-rules` gives them. The return's easy days are not shortened for a race.
2. Nothing missed is made up, and the gap default does not apply: the taper goes on from today's date. After 5 days or more without training, a taper week before race week takes the 41% cut and no deeper; race week stays as its table gives it.
3. After a fever, race week's short hard session happens only when an easy session two days before it felt normal; otherwise the openers alone.
4. Where the last day of the return is fewer than 5 days before race day, recommend racing it as a C race or not starting. Otherwise the race keeps its priority.
5. Offer `coach-predict` for a new figure and, where it has moved off the goal, a new goal through setup.

Whether to start is the athlete's decision, and what the illness was is for a clinician.

## The plan that already exists

Before proposing anything, compare what exists with what the race asks, and list each difference:

- a week whose role in the season or month plan is not the one the race fixes;
- a taper or race week planned at a load week's volume;
- a long or hard session later than "The last long and hard sessions" allows;
- a race-week day that differs from "Race week by day".

Each difference is changed by the skill that owns the file, after approval. Change no more than the race asks.

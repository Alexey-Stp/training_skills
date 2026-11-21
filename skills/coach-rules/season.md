# Season rules

How a season is laid out in weeks. Part of `coach-rules`: where another skill says "Season" in `coach-rules`, it means this file. All of it is convention, and an athlete rule on any part stands.

## Week roles

`load`, `easy`, `taper`, `race` and `recovery`.

- An easy week is sized by the block-shape default.
- Taper and race weeks follow "Races" in `coach-rules`.
- A recovery week is easy sessions only, at about half of the load of the last load week done.

## What a race fixes

- An A race fixes its race week, the taper before it and the recovery after it, in whole weeks. The race week is the last taper week: a one-week taper is the race week alone, and each further taper week comes before it. "Races" gives the lengths.
- Recovery of a week or two is that many recovery weeks. Recovery of a few days adds none, and the next week is a load week that starts easy.
- A B race fixes its race week, which stands in for an easy week.
- A C race fixes nothing and goes in its week's note.

## Load pattern

Three load weeks and an easy one, the block-shape default. Two and one where an athlete rule says so, or where the third load week of each of the last two blocks came in under 90% of its planned load.

A phase may have its own pattern, set by an athlete rule or by the athlete when the season is drafted. The season plan's phases table carries the pattern of each phase, and a block takes the pattern of the phase it starts in.

## Blocks

A block is a run of load weeks and the week that ends it: an easy week, a B race week, or an A race week with its taper.

- A block that ends in an easy week or a B race week has two to four load weeks.
- A block that ends in an A race has one to three load weeks before the taper, two at most before a three-week taper.
- Recovery weeks open the next block and are not counted in its length. After the season's last race they close that race's block.
- The one exception is a first block shortened under "Weeks already trained", which may have fewer load weeks, or none.

## Fill

A stretch runs from the plan's first week, or from the week after a B race week or after an A race's recovery, to the next B race week or A race week. Fill each stretch with whole blocks, in this order:

1. The last block of the stretch takes the pattern's load weeks. When that leaves weeks before it that cannot be filled as step 2 allows, it takes the nearest number "Blocks" allows that does fill them, trying fewer before more.
2. The blocks before it take the pattern's load weeks. Where the weeks do not divide, some take one fewer, or one more only when one fewer cannot fill the stretch, and those go as early in the stretch as they can.
3. A stretch that no whole blocks can fill is flagged, and its weeks are load weeks, apart from the weeks a race has fixed.

The plan says under "Why" which blocks differ from the pattern. A block that differs from a pattern an athlete rule sets is named there as a departure from that rule.

## Weeks already trained

A plan that starts with no month plan behind it counts the weeks just done.

1. Take the highest weekly load of the last four weeks.
2. Going back from last week, count the weeks in a row at 90% or more of it. Stop at the first week below.
3. A count of zero changes nothing: last week was lighter, and the first block starts fresh.
4. Otherwise the first block gets the pattern's load weeks less the count. When none are left, the plan's first week is an easy week, which ends that block.
5. Fill the rest of the stretch as "Fill" says. The shortened first block is one of the blocks that differ.

## Phases

- Build starts at the earliest block boundary that is 10 to 14 weeks before an A race's taper and after the previous A race's recovery. With fewer than 10 weeks, it starts straight after that recovery, or at the plan's first week. What lies before a build is base.
- The phases table says of each phase what kind it is: base, build, taper and race, or recovery. The kind, not the name, decides which rules under "Phase" in `coach-rules` apply. A base phase with a focus may be named for it, for example a run build, and a long phase may be numbered block by block.
- A base or build phase starts on a block's first Monday, or after the recovery weeks that open the block. Taper with race, and recovery, are phases of their own.
- Sport mode is the profile's default. Focus is what the athlete or the existing season plan says; otherwise the race's sport in a build to a single-sport race, and none elsewhere. A taper keeps its build's focus.

## Tests

Marked in easy weeks: each anchor that plans are prescribed from once every two or three blocks, two tests in a week at most. The first tests go in the first easy week allowed, an estimated or flagged anchor first; after that, choose between two and three blocks so that no week holds more than two tests. None in a taper, race or recovery week, nor in a week the athlete is partly away. A B race counts as a test of its sport's anchor.

## A week the athlete is away

A whole week with no training possible is an easy week, and the blocks are filled around it as around a B race week. A block that then comes out shorter than "Blocks" allows is kept and flagged.

## No race ahead

With no A or B race ahead, the plan covers 16 weeks in the load pattern, as one base phase.

## Clashes

Flag each with a recommendation. The plan follows the profile until the athlete changes it there.

- Two A races with fewer than 4 load weeks between the recovery of the first and the taper of the second. Recovery weeks come first, then the taper; when no load week is left between them, say that the load week before the taper could not be planned. Recommend which race to plan as B: the one whose goal matters less to the season, or with nothing to tell them apart, the earlier.
- A B race inside an A race's taper or recovery: the week keeps the role the A race gave it. Recommend planning that race as C.

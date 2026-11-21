---
name: coach-plan-season
description: Use when the athlete asks for the season to be planned or re-planned ("plan my season", "lay out the weeks to my race", "I added a race"), or when a target race was added, moved, dropped or given another priority. Drafts the season plan, with every week marked load, easy, taper, race or recovery, counted back from the target races.
---

# Season planning

Drafts the season plan: the phases, and a role for every week, counted back from the athlete's target races. Month plans take their weeks' roles from it.

A season plan holds no hours, no planned load and no planned sessions. Those belong to the month plan and the week plan.

## Steps

1. **Load.** Use `coach-data` to find the data folder. Read:
   - the athlete profile: target races with their priority, date and goal; default sport mode; dated availability exceptions that cover a whole week; limitations; anchors with their dates;
   - the season plan as it is now, whatever its layout. A file with no `Status` line was written by hand;
   - every month plan that is `APPROVED` or `CLOSED`, and the week reviews of the last two blocks;
   - with no month plan, the week summaries of the last four weeks, from `coach-data`;
   - the rules, through `coach-rules`: "Season" and "Races" are the ones this skill applies.
2. **Span.** Start at the first week of the current block. With no month plan, start at the coming Monday, or today when today is a Monday. End with the last recovery week after the last target race, or with its race week when it has none. With no A or B race ahead, cover 16 weeks in the load pattern as one base phase, and say that there is nothing to count back from.
3. **Race weeks.** For each target race work out its expected duration: the goal time, or with none an estimate from the distance and the anchors, labelled as estimated. Then fix its race week, taper weeks and recovery weeks as "What a race fixes" under "Season" says. A race with no priority is planned as B; say so.
4. **Fill the weeks between** as "Blocks" and "Fill" under "Season" say. Weeks inside an approved or closed month plan keep the roles it gave them, and the fill starts after them. With no month plan, count the load weeks already trained into the first block, as "Weeks already trained" under "Season" says.
5. **Phases.** Name each phase with its sport mode and focus, as "Phases" under "Season" says. Where a hand-written season plan already names phases, keep their names and order; a phase it gives by month starts on the nearest block boundary. Where it contradicts a race date in the profile, the profile stands, and the draft names the difference.
6. **Notes.** In the "Note" column: tests, as "Tests" under "Season" says; C races; and dated availability exceptions shorter than a week.
7. **Check the draft** before showing it. Each line gets an answer:
   - every week inside an approved or closed month plan has the role that month plan gave it;
   - every block has the number of load weeks "Blocks" allows, and the week before a taper is a load week;
   - every race has what its priority calls for before and after, or the clash is flagged;
   - a whole week the athlete is away is an easy or recovery week, or is flagged;
   - every athlete rule on the pattern, the easy week or the phases is followed.
8. **Write the draft**, then commit. First, when the season plan file is not in the repository or has uncommitted changes, commit it as it is, so that the version before the draft can be restored. Then write the season plan file the data index names, with status `DRAFT`, in the `coach-format` template. From a hand-written file, read dated notes that take out a whole week as availability, move its change log lines into the new change log, and carry everything else the template has no place for into "Kept from the earlier plan", word for word.
9. **Show the draft** in the message shape below and ask for approval. Stop here.
10. **On approval:** set the status to `APPROVED (<date>)`, add a line to the change log and commit. Confirm in one line, and say that the next run of `coach-plan-month` takes its weeks' roles from this plan and that nothing has changed on the calendar.

Done when the season plan is `APPROVED`; or when the draft is written and the athlete has been asked.

## Planning it again

A season plan is redrafted when a target race is added, moved, dropped or given another priority, when the gap default in `coach-rules` steps back a phase, or when the athlete asks.

- Weeks inside an approved or closed month plan stay as that month plan has them. A change to those weeks is a plan update through `coach-adjust`.
- Fill again from the first week the change reaches to the next A race week after it. Weeks before and after keep their roles. Then name the phases again and move any test whose week changed role.
- The change log says what moved and why.
- A draft the athlete turns down: restore the version before the draft from the repository and commit.

## Before approval

- **A change the athlete asks for:** revise the draft, re-run step 7, show it again.
- **A change that departs from a default** (five load weeks running, an easy week directly before a taper, no recovery week): make it, name the default and write the athlete's reason into "Why". Say once what the default is for.
- **A race's date, priority or goal:** these are in the athlete profile. `coach-setup` changes the profile first; then count again.
- **Hours, load or a fitness figure for the season:** the season plan carries none. Say that the month plan sets hours and planned load block by block, from what was actually done.
- **"Looks good", "ok", "go"** in answer to the draft is approval. Silence, a question or a partial comment is not.

## Message shape

Short enough for a phone screen, plain lines, no tables. In this order: one line for the season (dates, sport mode, load pattern); the races, one line; the phases, one line; one line per block, with its first Monday, one letter per week and its race or tests; the reasoning in two or three lines; one line for anything estimated or assumed (a race duration, a priority); flags, when there are any; the request for approval.

Letters: `L` load, `E` easy, `T` taper, `R` race with its priority, `Rec` recovery. All values in this sample are invented.

```
Season 18 Jan to 17 Oct, DRAFT: triathlon, 3 load weeks then 1 easy.
Races: 10 km (B) 6 Jun · Olympic triathlon (A) 18 Jul · half marathon (A) 10 Oct.
Phases: run builds to 14 Mar · triathlon base to 11 Apr · triathlon build to 4 Jul · half marathon build from 26 Jul.

18 Jan  L L L E
15 Feb  L L L E     CP test, swim CSS test
15 Mar  L L L E     5 km time trial
12 Apr  L L L E     CP test
10 May  L L L R(B)  10 km
7 Jun   L L E       CP test, swim CSS test
28 Jun  L T R(A)    triathlon
19 Jul  Rec L L E   5 km time trial
16 Aug  L L E       CP test, swim CSS test
6 Sep   L L L T R(A) Rec  half marathon

Why: counted back from the three races; all of it is convention. Four blocks differ from three and one: the two after the 10 km, because only four weeks lie between it and the taper, and the two after the triathlon, so that three load weeks lead into the half marathon taper.

Approve this season?
```

## Boundaries

- Target races and goals are read from the athlete profile and written only by `coach-setup`.
- The roles, patterns and phase lengths are conventions. Call them that wherever they appear, and let an athlete rule stand over them.

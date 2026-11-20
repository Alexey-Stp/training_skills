# Cut-over from the existing setup

The athlete already runs a coaching setup in OpenClaw. This page says what the suite takes over and in what order. From [replace, absorb or coexist][t18] and [cut-over][t19].

## What happens to each existing piece

| Existing piece | Outcome |
|---|---|
| Profile, daily check, session review, week review, weekly and monthly planning, plan updates | Taken over by the suite |
| Nutrition: food logging, nutrition targets, nutrition jobs | Coexists unchanged, outside the suite |
| Live analysis scripts | Stay private as the analysis layer; skills call them through the data index |
| Season plan, then week plan; "markdown is truth"; "nothing pushed before approval" | Kept; a month plan and day plans are added |
| Weekly archive | Not continued: each week is its own file from the start |
| Documents and skills that restate anchors, goals or zones | Imported once into the athlete profile, then pointed at it or archived |
| The athlete's existing rules | Moved into the athlete rules file; none dropped without the athlete saying so |
| Four coaching scheduled jobs (morning, midday, evening, Sunday) | Repointed to suite skills |
| Activity-naming skill | Retired; its live scripts remain in the analysis layer |
| Coaching parts of the umbrella health skill | Retired; it keeps nutrition and sync |
| Readiness-verdict part of the wearable skill | Retired; it stays as a data source |
| Stale plan and goal files | Retired |
| Dormant race-strategy skill | Left alone, out of scope |

## Scheduled jobs after cut-over

| Job | Runs |
|---|---|
| Morning, at 08:00, 09:00 and 10:00 | `coach-today`; speaks once ([today skill][t20]) |
| Midday and evening | `coach-review-session` |
| Sunday | `coach-review-week`, then `coach-plan-week`; ends with a request for approval ([skill list][t7]) |

Claude Code gets no scheduled jobs of its own.

## Prerequisite

One piece of private work before stage 1: a JSON mode for the six required data commands of the [training data contract][t21]. The seventh, naming an activity, is optional. Without it the skills run on basic intervals.icu figures only.

## Stages

Each stage is finished before the next starts.

1. **Setup.** `coach-setup` creates the data index, the athlete profile and the athlete rules from the existing documents.
2. **By hand.** The athlete uses session review, today and the planning skills on request while the existing scheduled jobs keep running.
3. **Scheduled jobs.** Repointed one at a time: the morning daily check, then midday and evening review, then Sunday planning.
4. **Retire.** Old pieces are archived.

Claude Code is added after stage 3, once OpenClaw is stable: the same skills pointing at the same data folder.

## Rules for the overlap

- Old and new run side by side, but never as two chat messages for the same thing. In stage 2 the old job sends its message and the new skill is run by hand for comparison.
- A job is switched when the athlete says its skill is good enough. The old job is disabled, not deleted.
- Plans move at a week boundary. The current week finishes in the old weekly plan file; the next Sunday job writes the first week in the new layout. Old weekly archives are not converted.

## Undo

Each stage is one commit in the workspace's local repository. Undoing a stage is re-enabling the old job and reverting that commit. How this sits with skills committing after each write is an open point in the [README](README.md).

## Safe to retire

A piece is retired after two weeks in which its replacement ran on schedule with no correction from the athlete. It moves to the archive folder; nothing is deleted. This applies to the old naming skill, the coaching parts of the health skill, the readiness part of the wearable skill, the old weekly plan file and its procedure documents, and stale plan and goal files.

[t7]: https://github.com/Alexey-Stp/training_skills/issues/7
[t18]: https://github.com/Alexey-Stp/training_skills/issues/18
[t19]: https://github.com/Alexey-Stp/training_skills/issues/19
[t20]: https://github.com/Alexey-Stp/training_skills/issues/20
[t21]: https://github.com/Alexey-Stp/training_skills/issues/21

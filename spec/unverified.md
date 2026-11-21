# Unverified

Claims this spec relies on that nobody has tested. Check these first when building. Status is one of: untested, tested (with the date), failed.

## Trial checks

The [trial install][t22] put a stub skill in both runtimes. The Claude Code half ran on 2026-11-19. The OpenClaw half is four checks the athlete's OpenClaw agent ran on 2026-11-20. The watch part of check 4 was skipped, because the test event had been written with the wrong notation:

1. The stub is listed, its chat command name is recorded, and it reads its sibling file.
2. A scheduled job invokes the stub, once named in plain language and once as `/skill <name>`.
3. A calendar event sent twice with the same `external_id` and a personal API key, then read back.
4. A pool-swim session published and checked on the watch.

## Runtimes

| # | Claim | How to test | Status |
|---|---|---|---|
| 1 | A skill folder in the Claude Code user skills folder is listed under its hyphenated name and can read a sibling file by relative path | Stub skill, see [trial install][t22] | tested 2026-11-19 |
| 2 | A skill folder in the OpenClaw workspace `skills/` folder is listed, and Telegram registers a command for it | Trial check 1 | tested 2026-11-20 |
| 3 | Telegram turns the hyphen in a skill name into an underscore, so `coach-today` is `/coach_today`; there is no hyphen form | Trial check 1 | tested 2026-11-20 |
| 4 | A scheduled job can invoke a skill named in plain language | Trial check 2 | tested 2026-11-20 |
| 5 | A scheduled message starting with `/skill <name>` is expanded like a chat command | Trial check 2 ran the skill, but the run record cannot show whether the message was expanded or only understood as text. Needs a test whose result differs between the two | untested |
| 6 | A scheduled job in a default isolated session receives the workspace files and the skills list | Trial check 2 showed the skills list arrives. The workspace files were not checked; run a job that must quote the pointer line | untested |
| 7 | `openclaw plugins install --link <clone>` exposes this repo's skills on the installed OpenClaw version, and whether names gain a prefix | Not in the trial; needs the athlete's go-ahead because it changes OpenClaw configuration | untested |
| 8 | How a bare skill name resolves under Claude Code plugin namespacing | Install the plugin and call one skill from another | untested |
| 9 | The pointer line in `AGENTS.md` or the user-level `CLAUDE.md` reaches a skill, because the runtime loads that file | Start a fresh session in each runtime and run a skill that must find the data index | untested |
| 10 | Skills installed as a bundle or through `extraDirs` load at the lowest precedence | Install one with the same name as a workspace skill and see which runs | untested |
| 11 | A sibling file of a skill is read by skill-relative path in OpenClaw | Trial checks 1 and 2 | tested 2026-11-20 |

Scheduled messages name the skill in plain language, not as `/skill <name>`, at least until 5 is tested. ([OpenClaw skill format][t16])

## intervals.icu

From [intervals.icu API][t2] and [calendar sync][t13]. No call was made with credentials during research.

| # | Claim | How to test | Status |
|---|---|---|---|
| 12 | Sending an event again to `POST /athlete/{id}/events` with the same `external_id` updates it, with a personal API key | Trial check 3: a second event was created | failed 2026-11-20 |
| 13 | Sending it to `/events/bulk?upsert=true` with the same `external_id` updates the first event in place | Trial check 3 | tested 2026-11-20 |
| 14 | `external_id` is returned when the event is read back, so the suite can recognise its own events | Trial check 3 | tested 2026-11-20 |
| 15 | Workout text in an event's `description` is parsed into a structured workout | Trial check 3, with a single step | tested 2026-11-20 |
| 16 | The exact workout text syntax used in [the example day plan](examples/plan/days/2027-02-02.md) | Publish it and read it back | untested |
| 17 | Events created through the API reach the watch like ones created in the web app | Publish one for tomorrow and check the watch | untested |
| 18 | Pool-swim sessions on the watch: pace units and timed rests | Not checked in the trial. Publish a pool swim written in the correct notation and look at it on the watch | untested |
| 19 | Distances in workout text can be written as `200m`, and repeats as `4x 100m` with a rest | Trial check 4: `200m` was read as 200 minutes, and the repeats with their rest became one step. Find the notation for metres and for repeats in the intervals.icu workout text reference, publish and read back | failed 2026-11-20 |
| 20 | Units of the zone arrays in sport settings | Read sport settings and compare with the web app | untested |
| 21 | The effort score can be written to an activity through the API | Write one and read it back | untested |
| 22 | A short review can be written to an activity's description through the API | The athlete's existing script already does this; confirm it still works | untested |

## If intervals.icu stops serving Garmin data

From [activity source resilience][t15]. The restriction was last checked on 2026-11-19: not final, no date.

| # | Claim | How to test | Status |
|---|---|---|---|
| 23 | Whether the restriction applies to an athlete's own API key | Watch for empty stubs on Garmin-recorded activities | untested |
| 24 | An activity file uploaded by the athlete is served in full by the API | Upload one file and read its streams | untested |
| 25 | An uploaded file does not duplicate the synced stub of the same activity | Same test; count activities for that day | untested |
| 26 | Planned sessions still reach the watch after the restriction | Only observable once the restriction exists | untested |

## Garmin

From [Garmin as secondary source][t3]. No account was signed in to during research.

| # | Claim | How to test | Status |
|---|---|---|---|
| 27 | The official Personal API serves sleep, HRV with baseline, resting heart rate and the original activity file | Create a key and make one read call each | untested |
| 28 | Its rate limits are enough for a daily refresh | Read the terms behind sign-in | untested |
| 29 | Garmin's terms of use allow automated access with a personal key | Read the terms behind sign-in | untested |
| 30 | The athlete's watch accepts structured planned sessions for all three sports; the model was not established | Note the model under equipment in the profile and check it against Garmin's support list | untested |
| 31 | Which wellness values the Garmin sync fills in intervals.icu today | Compare one day's wellness record in intervals.icu with the same day in Garmin | untested |

## Coaching research

From [best-practice coaching][t5]: several sources were cited from memory or checked at abstract level only. The list is in the research file's "Not verified" section on the `research/coaching-best-practice` branch. The numbers in [coaching-rules](skills/coaching-rules.md) are defaults the athlete rules can override, and the ones marked as convention are labelled so. How to test: re-read each listed source in full before a number is relied on.

## Shapes judged on invented data

- The session review shape was chosen from an invented activity, not a real one. ([session review][t14])
- The six file templates use invented data. ([file templates][t24])
- The season rules (how weeks between races are filled, the week roles, the size of a recovery week) were checked only by dry run on invented races. No season plan has been drafted from a real race calendar or lived through.
- The nutrition target was checked only by dry run on invented days. Its base day, load cut-offs and rough rates have not been compared with a real athlete's weight over time, and the intervals.icu fields it reads for work and device energy (`icu_joules`, `calories`) are taken from use, not from the API's documentation. Whether a device's energy figure for an activity includes resting energy has not been checked; the target assumes it does.

How to test: during cut-over stage 2, run `coach-review-session` on real activities and `coach-plan-week` on a real week, and let the athlete react to the result.

[t2]: https://github.com/Alexey-Stp/training_skills/issues/2
[t3]: https://github.com/Alexey-Stp/training_skills/issues/3
[t5]: https://github.com/Alexey-Stp/training_skills/issues/5
[t13]: https://github.com/Alexey-Stp/training_skills/issues/13
[t14]: https://github.com/Alexey-Stp/training_skills/issues/14
[t15]: https://github.com/Alexey-Stp/training_skills/issues/15
[t16]: https://github.com/Alexey-Stp/training_skills/issues/16
[t22]: https://github.com/Alexey-Stp/training_skills/issues/22
[t24]: https://github.com/Alexey-Stp/training_skills/issues/24

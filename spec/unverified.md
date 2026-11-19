# Unverified

Claims this spec relies on that nobody has tested. Check these first when building. Status is one of: untested, tested, failed.

## Runtimes

| # | Claim | How to test | Status |
|---|---|---|---|
| 1 | A skill folder in the Claude Code user skills folder is listed under its hyphenated name and can read a sibling file by relative path | Stub skill, see [trial install][t22] | tested 2026-11-19: works |
| 2 | A skill folder in the OpenClaw workspace `skills/` folder is listed, and Telegram registers a command for it | Trial check 1 | untested |
| 3 | Whether Telegram shows `coach-today` as `coach_today` | Trial check 1 | untested |
| 4 | A scheduled run can invoke a skill named in plain language | Trial check 2 | untested |
| 5 | A scheduled message starting with `/skill <name>` is expanded like a chat command | Trial check 2 | untested |
| 6 | A default isolated scheduled run receives the workspace files and the skills list | Trial check 2 | untested |
| 7 | `openclaw plugins install --link <clone>` exposes this repo's skills on the installed OpenClaw version, and whether names gain a prefix | Not in the trial; needs the athlete's go-ahead because it changes OpenClaw configuration | untested |
| 8 | How a bare skill name resolves under Claude Code plugin namespacing | Install the plugin and call one skill from another | untested |

| 24 | The pointer line in `AGENTS.md` or the user-level `CLAUDE.md` reaches a skill, because the runtime loads that file | Start a fresh session in each runtime and run a skill that must find the data index | untested |
| 25 | Skills installed as a bundle or through `extraDirs` load at the lowest precedence | Install one with the same name as a workspace skill and see which runs | untested |

Until 4 to 6 are tested, scheduled messages name the skill in plain language. ([OpenClaw skill format][t16])

## intervals.icu

From [intervals.icu API][t2] and [calendar sync][t13]. No call was made with credentials during research.

| # | Claim | How to test | Status |
|---|---|---|---|
| 9 | Sending an event again with the same `external_id` updates it, with a personal API key | Trial check 3 | untested |
| 10 | `external_id` is returned when the event is read back, so the suite can recognise its own events | Trial check 3 | untested |
| 11 | Workout text in an event's `description` is parsed into a structured workout | Trial check 3 | untested |
| 12 | The exact workout text syntax used in [the example day plan](examples/plan/days/2027-02-02.md) | Publish it and read it back | untested |
| 13 | Events created through the API reach the watch like ones created in the web app | Publish one for tomorrow and check the watch | untested |
| 14 | Pool-swim sessions on the watch: pace units and timed rests | Trial check 4 | untested |
| 15 | Units of the zone arrays in sport settings | Read sport settings and compare with the web app | untested |
| 16 | The effort score can be written to an activity through the API | Write one and read it back | untested |
| 17 | A short review can be written to an activity's description through the API | The athlete's existing script already does this; confirm it still works | untested here |

## If intervals.icu stops serving Garmin data

From [activity source resilience][t15]. The restriction was last checked on 2026-11-19: not final, no date.

| # | Claim | How to test | Status |
|---|---|---|---|
| 18 | Whether the restriction applies to an athlete's own API key | Watch for empty stubs on Garmin-recorded activities | untested |
| 19 | An activity file uploaded by the athlete is served in full by the API | Upload one file and read its streams | untested |
| 20 | An uploaded file does not duplicate the synced stub of the same activity | Same test; count activities for that day | untested |
| 21 | Planned sessions still reach the watch after the restriction | Only observable once the restriction exists | untested |

## Garmin

From [Garmin as secondary source][t3]. No account was signed in to during research.

| # | Claim | How to test | Status |
|---|---|---|---|
| 22 | The official Personal API serves sleep, HRV with baseline, resting heart rate and the original activity file | Create a key and make one read call each | untested |
| 23 | Its rate limits are enough for a daily refresh | Read the terms behind sign-in | untested |
| 26 | Which wellness values the Garmin sync fills in intervals.icu today | Compare one day's wellness record in intervals.icu with the same day in Garmin | untested |

## Coaching research

From [best-practice coaching][t5]: several sources were cited from memory or checked at abstract level only. The list is in the research file's "Not verified" section on the `research/coaching-best-practice` branch. The numbers in [coaching-rules](skills/coaching-rules.md) are defaults the athlete rules can override, and the ones marked as convention are labelled so. How to test: re-read each listed source in full before a number is relied on.

## Shapes judged on invented data

- The session review shape was chosen from an invented activity, not a real one. ([session review][t14])
- The six file templates use invented data. ([file templates][t24])

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

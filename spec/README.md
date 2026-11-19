# Training skills: spec

A suite of agent skills that coach one athlete: reviewing completed training and planning what comes next. This folder says what to build. Building, testing and publishing the skills is a separate effort.

Assembled from the decisions on the [wayfinder map][map]. Each section names the decision it came from. Terms are defined in [`GLOSSARY.md`](../GLOSSARY.md).

## Ground rules

- **One athlete.** No multi-user support. Sports: swim, bike, run, plus strength as ordinary sessions. ([map][map])
- **Two runtimes.** OpenClaw first, Claude Code second, same skill files. ([private training data][t8], [OpenClaw skill format][t16])
- **Public skills, private data.** This repo holds skills only. The athlete profile, athlete rules, plans, reviews and keys never enter it. ([private training data][t8])
- **Markdown is the truth.** Plans live in markdown in the data folder. intervals.icu receives a copy. ([replace, absorb or coexist][t18], [calendar sync][t13])
- **Approval before publishing.** Nothing reaches the calendar before the athlete approves it. A scheduled run that would change a plan leaves a draft and asks in the chat channel. ([skill list][t7])
- **Defaults are overridable.** Public coaching rules are best-practice defaults; the athlete's private rules override them. ([replace, absorb or coexist][t18], [coaching method][t11])
- **Never invent a number.** Missing data is said to be missing. ([training data contract][t21])

## Skills

Seven the athlete starts ([skill list][t7]):

| Skill | Triggered by | Writes | Spec |
|---|---|---|---|
| `coach-setup` | "set up my profile", "my FTP changed" | index, profile, rules; after approval | [coach-setup](skills/coach-setup.md) |
| `coach-today` | "what's today", "am I ready", "what's tomorrow" | the readiness verdict and morning feel, to the day plan | [coach-today](skills/coach-today.md) |
| `coach-review-session` | "review my run" | the session review, without asking | [coach-review-session](skills/coach-review-session.md) |
| `coach-review-week` | "how was my week" | Actual vs plan, without asking | [coach-review-week](skills/coach-review-week.md) |
| `coach-plan-week` | "plan next week" | a draft week; publishes after approval | [coach-plan-week](skills/coach-plan-week.md) |
| `coach-plan-month` | "plan the next block" | a draft month plan; after approval | [coach-plan-month](skills/coach-plan-month.md) |
| `coach-adjust` | "I missed it", "I'm tired", "move Thursday" | a plan update, before and after; after approval | [coach-adjust](skills/coach-adjust.md) |

Three shared, called only by other skills:

| Skill | Holds | Spec |
|---|---|---|
| Coaching rules | best-practice defaults; loads the athlete rules | [coaching-rules](skills/coaching-rules.md) |
| Training data | finding the data folder, reading activity sources, calling the analysis layer | [training-data](skills/training-data.md) |
| Plan format | how the files are written, calendar sync mechanics, the runtime vocabulary | [plan-format](skills/plan-format.md) |

No skill in the first version for: the season plan (athlete-maintained), an "am I on track" check (folded into week review), race preparation and debrief, and "why" questions (answered in conversation from the coaching rules). ([skill list][t7])

## How the pieces fit

```
athlete (chat) -> coach-* skill -> shared skills
                                    |- coaching rules + ATHLETE-RULES.md
                                    |- plan format   -> files in the data folder -> intervals.icu calendar -> watch
                                    '- training data -> analysis layer (private scripts), else intervals.icu directly
```

- The data folder and its files: [data-folder.md](data-folder.md).
- Moving from the athlete's existing setup: [cut-over.md](cut-over.md).
- Everything not yet tested: [unverified.md](unverified.md).
- Filled examples with invented data: [examples/](examples/).

## Packaging

From [Pocock skills as a template][t6] and [OpenClaw skill format][t16]:

- One `skills/<name>/SKILL.md` tree in this repo. Frontmatter: `name` and `description`; `user-invocable` and `disable-model-invocation` behave the same in both runtimes.
- The seven `coach-*` skills are entry points. The three shared skills are model-invoked, so other skills can call them.
- Keep each `SKILL.md` short. Put material only some branches need (formats, per-sport figures, sport mode branches) in sibling files behind a one-line pointer. Use skill-relative paths.
- Write to the common subset. Do not use the OpenClaw-only `{baseDir}` and `command-dispatch`, nor the Claude Code-only `${CLAUDE_SKILL_DIR}`, `$ARGUMENTS`, inline shell commands, `context: fork` and `allowed-tools`.
- Do not rely on `AGENTS.md`, `USER.md` or `CLAUDE.md` content. Every skill starts by reading the data index, found through the one-line pointer those files carry.
- Do not gate skills on environment variables; keys are in home-directory files.
- Add a Claude Code plugin manifest (`.claude-plugin/plugin.json` with an explicit `skills` array, plus `marketplace.json`). The OpenClaw install route is untested; see [unverified.md](unverified.md).
- Telegram command names allow only `a-z0-9_`, at most 32 characters.

## Build order

From [spec assembly][t26]; it matches the stages in [cut-over.md](cut-over.md).

1. Plan format, training data, coaching rules
2. `coach-setup`
3. `coach-today`
4. `coach-review-session`
5. `coach-review-week`
6. `coach-plan-week`
7. `coach-adjust`
8. `coach-plan-month`

## Open points

Gaps the decisions leave. They are listed, not filled.

1. Names of the three shared skills. Only the seven `coach-*` names were decided.
2. Field names of the JSON answers in the training data contract. That they are fixed was decided; the fields were not.
3. Reply shapes for `coach-review-week`, `coach-plan-week`, `coach-plan-month` and `coach-adjust`. Only the session review and the daily check were given a shape. The decided constraints are in each skill's file.
4. The illustrative default readiness bands the public skill carries when the athlete rules give none.
5. Who writes the month plan's "Block review" section. The example assigns it to week review when the last week closes; no decision says so.
6. What `coach-review-week` does when asked mid-week.
7. Exact wording of the pointer lines in `AGENTS.md` and the user-level `CLAUDE.md`.
8. Whether the short review posted to the activity description is the whole review or only its verdict and Next line.

## Out of scope

Building and publishing the skills; more than one athlete; sports beyond swim, bike and run; nutrition (coexists unchanged); the athlete's dormant race-strategy skill; porting the private analysis scripts into this repo. ([map][map], [replace, absorb or coexist][t18])

## Decisions this spec is assembled from

| Decision | Type |
|---|---|
| [intervals.icu API][t2] | research |
| [Garmin as secondary source][t3] | research |
| [Everyday athlete usage][t4] | research |
| [Best-practice coaching][t5] | research |
| [Pocock skills as a template][t6] | research |
| [Skill list][t7] | decision |
| [Private training data][t8] | decision |
| [Athlete profile contents][t9] | decision |
| [Plan files][t10] | decision |
| [Coaching method][t11] | decision |
| [Sport mode][t12] | decision |
| [Calendar sync][t13] | decision |
| [Session review][t14] | prototype |
| [Activity source resilience][t15] | decision |
| [OpenClaw skill format][t16] | research |
| [Replace, absorb or coexist][t18] | decision |
| [Cut-over][t19] | decision |
| [Today skill][t20] | decision |
| [Training data contract][t21] | decision |
| [Trial install][t22] | task, open |
| [Subjective log][t23] | decision |
| [File templates][t24] | prototype |
| [Athlete setup flow][t25] | decision |
| [Spec assembly][t26] | decision |

Five small points were decided in conversation without a ticket and are recorded on the [map][map]: a planned session with no activity, mobility, runtime memory notes, hand-offs, and vocabulary at runtime.

# Training skills

Agent skills that coach one endurance athlete: they review completed training and plan what comes next. Built for swim, bike and run, with strength as ordinary sessions.

They run in OpenClaw first and Claude Code second, from the same files. Plans live as markdown in a private folder on the athlete's machine; intervals.icu receives a copy of approved sessions and forwards them to the watch.

## Status

Early. All ten skills exist and each was checked by dry run on invented data: an agent worked through the same situations with and without the skill. None has been through a full week on real data yet, and several API details are still untested. [`spec/unverified.md`](spec/unverified.md) lists what is not yet proven.

## The skills

Seven the athlete calls, by name or in plain words:

| Skill | Ask it | What it does |
|---|---|---|
| [`coach-setup`](skills/coach-setup/SKILL.md) | "set up my profile", "my FTP changed" | Creates and updates the data index, the athlete profile and the athlete's own rules |
| [`coach-today`](skills/coach-today/SKILL.md) | "what's today", "am I ready" | The daily check: today's session and a readiness verdict of go, modify or skip |
| [`coach-review-session`](skills/coach-review-session/SKILL.md) | "review my run" | Assesses one activity against its planned session |
| [`coach-review-week`](skills/coach-review-week/SKILL.md) | "how was my week" | Reviews a finished week and says whether the athlete is on track |
| [`coach-plan-week`](skills/coach-plan-week/SKILL.md) | "plan next week" | Drafts the coming week; publishes it after approval |
| [`coach-adjust`](skills/coach-adjust/SKILL.md) | "I missed it", "I'm tired", "move Thursday" | Changes an approved plan, shown as before and after |
| [`coach-plan-month`](skills/coach-plan-month/SKILL.md) | "plan the next block" | Drafts the next block of weeks from the season plan |

Three shared ones the others call:

| Skill | Holds |
|---|---|
| [`coach-rules`](skills/coach-rules/SKILL.md) | Coaching limits and defaults; the athlete's own rules override them |
| [`coach-data`](skills/coach-data/SKILL.md) | Finding the data folder and getting training figures |
| [`coach-format`](skills/coach-format/SKILL.md) | Plan file layouts, calendar sync and the shared vocabulary |

## How it behaves

- **Markdown is the truth.** Plans are files; the calendar is a copy.
- **Approval before publishing.** A plan or plan update is shown first. Nothing reaches the calendar until the athlete approves it.
- **Limits and defaults.** A limit is not planned past without the athlete's explicit say-so. A default can be departed from, with the reason written into the plan.
- **No invented numbers.** A figure that is missing is said to be missing.
- **Few questions.** A skill looks for a value, works it out from history, or assumes a marked default before it asks.

## Your data stays out of this repo

The skills are public; the athlete's data is not. Everything personal lives in a data folder on the athlete's machine: profile, rules, plans, reviews. Keys live in files in the home directory.

`coach-setup` writes a small index, `COACH.md`, into that folder. It tells the other skills where each file is and which private command answers each data question. The skills find the index through one line in the runtime's standing instructions:

```
Coach data index: <path to COACH.md>
```

The files a skill writes follow the templates in [`skills/coach-format/templates/`](skills/coach-format/templates/). All values in them are invented.

## Install

**OpenClaw.** Copy the ten folders under `skills/` into your workspace's `skills/` folder. They are picked up without a restart. In Telegram the commands appear with underscores, for example `/coach_setup`.

**Claude Code.** Copy the ten folders into `~/.claude/skills/`.

Then run `coach-setup`. It proposes which of your existing documents to import from and shows the profile and rules for approval before writing them.

The repo also carries a Claude Code plugin manifest in `.claude-plugin/`. Installing it as a plugin, or as a linked bundle in OpenClaw, is untested.

## What you need

- An [intervals.icu](https://intervals.icu) account with a personal API key. It is the primary source of activities and the calendar the plans are published to.
- A watch that receives planned sessions from intervals.icu, if you want them on your wrist.
- Optional: your own scripts that turn raw activity data into figures (a readiness score, per-rep analysis). The skills call them through the index and expect JSON in the shape listed in [`coach-data`](skills/coach-data/SKILL.md). Without them the skills work from basic intervals.icu figures.

## Repo layout

| Path | What |
|---|---|
| `skills/` | The ten skills |
| `spec/` | The decisions the skills were built from, and what is still untested |
| `GLOSSARY.md` | The terms the project uses |
| `AGENTS.md` | Rules for agents working on this repo |

## Not in scope

More than one athlete, sports beyond swim, bike and run, and nutrition.

# Working on this repo

For agents changing the skills or the spec. To *use* the skills, read [README.md](README.md).

## This repo is public

It holds skills only. Keep every personal detail out of files, examples, commit messages, issues and pull requests: names, health and performance numbers, race names and dates, limitations, personal rules, timezone, athlete ids, chat ids, local paths, keys.

- Examples and templates use invented data, and say so on their first line.
- Invented data must not mirror a real athlete's. Change the shape, not just the numbers.
- Before committing, search the diff for anything that came from a real workspace.

## Words

Use the terms in [GLOSSARY.md](GLOSSARY.md) with their meanings, and none of the words it lists under "Avoid". `coach-format` carries the same vocabulary to runtime; change both together.

## Spec and skills

- [`spec/`](spec/) records the decisions the skills were built from. `spec/README.md` lists amendments and open points; [`spec/unverified.md`](spec/unverified.md) lists claims nobody has tested.
- When a skill change departs from the spec, say so in the pull request. Settle an open point in the skill, then name it in the pull request.
- State each rule in one place. Limits and defaults live in `coach-rules`; file layouts and calendar sync in `coach-format`; data access in `coach-data`. Other skills point to them.

## Writing a skill

- One `skills/<name>/SKILL.md` per skill, kept short. Material only some branches need goes in a sibling file behind a one-line pointer.
- Write to what OpenClaw and Claude Code share. Leave out `{baseDir}`, `command-dispatch`, `${CLAUDE_SKILL_DIR}`, `$ARGUMENTS`, inline shell commands, `context: fork` and `allowed-tools`.
- Every skill can be called by the model. The three shared skills set `user-invocable: false`.
- Say what to do. Keep a prohibition only for a hard guardrail, next to the positive target.
- End each run of steps on a "Done when" the agent can check.
- A skill finds a value, derives it from history, or assumes a marked default before it asks the athlete. Questions are the last resort and go in one message.
- Messages to the athlete are short enough for a phone screen and have no tables. Files may have tables.
- A skill never names a private script. It names a question; the athlete's data index maps it to a command.

## Checking a change

There is no test suite. A skill is checked by dry run:

1. Write a handful of situations that tempt the failure you care about.
2. Have a fresh agent answer them with only invented data, then another with the skill as well.
3. Compare. Close the gaps the second run reports.
4. Say in the pull request what was run, and whether it was re-run after the last edit.

The invented data folder for these runs is `skills/coach-format/templates/`.

## Git

Branch from `main` and open a pull request. One skill or one concern per pull request.

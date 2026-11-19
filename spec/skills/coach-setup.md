# coach-setup

## Purpose

Create and keep current the three standing files every other skill reads: the data index, the athlete profile and the athlete rules. It is the only skill that writes the athlete profile.

## Triggers

- "set up my profile", "my FTP changed", "update my availability".
- A suggestion from `coach-review-week`. Setup never runs on a schedule.

## Reads

- The data folder, if it exists, and the existing documents the athlete confirms.
- intervals.icu sport settings: thresholds and zones.
- One read call to each service, to confirm the keys work.

## Writes

After approval only, then commits:

- `COACH.md`, `ATHLETE.md`, `ATHLETE-RULES.md`.
- A key file for a service that has none yet (the athlete supplies the key; the index records the path only).
- The goals and anchors sections of the season plan, replaced by a pointer to the athlete profile, in the same commit.

## Steps

First run ([athlete setup flow][t25]):

1. Find or create the data folder and write the data index: file paths, key file paths, the command for each training data question.
2. Make one read call to each service to confirm the keys work.
3. Read thresholds and zones from intervals.icu.
4. Propose a list of existing documents to import from. Read only the ones the athlete confirms. Leave out files marked stale.
5. Import. Record for every anchor its source, date and method; flag anything estimated or untested.
6. Collect existing rules and show each for keep or drop. Drop none without the athlete saying so.
7. Ask only for what is still missing, section by section, with a recommended answer.
8. Show the whole profile and rules file for approval.
9. Write, replace the season plan's goals and anchors sections with a pointer, and commit.

Later runs:

- Can cover one section only, without asking about the rest.
- When an anchor changes: show old and new values with recalculated zones, and list the already-approved planned sessions whose targets would move. On approval, update the profile and add a change-log line. Offer `coach-adjust` for those sessions.
- When the profile and intervals.icu differ on a threshold: show both and ask which stands. ([athlete profile contents][t9])

## Reply

A before-and-after of what will be written, then a request for approval. See [ATHLETE.md](../examples/ATHLETE.md), [ATHLETE-RULES.md](../examples/ATHLETE-RULES.md) and [COACH.md](../examples/COACH.md) for the files it produces.

## Must never

- Write a key, token or password into the data folder, the index or a chat message.
- Import from a document the athlete did not confirm.
- Overwrite the profile or intervals.icu silently when they differ.
- Edit a planned session. That is `coach-adjust`.
- Type in weight, HRV baseline or resting-heart-rate baseline; they are computed.

## Source tickets

[Private training data][t8], [athlete profile contents][t9], [athlete setup flow][t25], [training data contract][t21], [file templates][t24], [replace, absorb or coexist][t18].

[t8]: https://github.com/Alexey-Stp/training_skills/issues/8
[t9]: https://github.com/Alexey-Stp/training_skills/issues/9
[t18]: https://github.com/Alexey-Stp/training_skills/issues/18
[t21]: https://github.com/Alexey-Stp/training_skills/issues/21
[t24]: https://github.com/Alexey-Stp/training_skills/issues/24
[t25]: https://github.com/Alexey-Stp/training_skills/issues/25

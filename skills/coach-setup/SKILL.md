---
name: coach-setup
description: Use when the athlete asks to set up or update their profile or rules ("set up my profile", "my FTP changed"), reports a changed anchor, goal, availability, limitation or equipment, or when a coach skill finds no data index.
---

# Coach setup

Creates and keeps current the three standing files every coach skill reads: the data index (`COACH.md`), the athlete profile (`ATHLETE.md`) and the athlete rules (`ATHLETE-RULES.md`). This is the only skill that writes the athlete profile.

Layouts are the templates in the `coach-format` skill. Copy headings and field names; every value comes from the athlete, a confirmed document or intervals.icu.

## Which run is this

- No `COACH.md` yet, or no `ATHLETE.md`: **first run**.
- Both exist: **later run**. Go to the section for what changed.

## First run

This run stops for the athlete twice at most and asks as little as it can. Whatever can be found or worked out is filled in, marked with where it came from, and corrected by the athlete when they see the result.

- **Gate 1, the import list.** "Just do it" or "use whatever you find" confirms the list as proposed: send the list, with what was left out, as information and carry on. Silence does not confirm it.
- **Gate 2, the profile and rules.** Always holds: nothing is written to either before the athlete has seen it and approved.

1. **Write the data index.** Find or create the data folder and write `COACH.md`: file paths, key file paths, and the command for each training data question that the analysis layer offers. Add the pointer line `Coach data index: <path to COACH.md>` to the workspace `AGENTS.md` when the workspace has one (OpenClaw), otherwise to the user-level `CLAUDE.md` (Claude Code). Commit. List a command only when the analysis layer's own documentation or the athlete says which question it answers; a question without a confirmed command is left without one, and `coach-data` then falls back to intervals.icu. This step happens before anything is approved, because every later step needs it.
2. **Check the keys.** For each service, make one read call with its key file. A service with no key file: tell the athlete the path where the file belongs, in the format the analysis layer expects, and record the path in the index. Without a working intervals.icu key the run stops here. A missing Garmin key does not block: note it and carry on.
3. **Read intervals.icu**: thresholds and zones per sport, from sport settings.
4. **Propose the import list.** List the existing documents that look like sources for goals, anchors, availability, limitations, equipment or rules. Add, as one item each, the runtime's memory notes of the last 8 weeks and its chat history where it keeps one: much of what a profile needs was said there once. If the runtime keeps neither, say so. Judge from file and folder names only at this point. Leave out any that look stale and any that are not about training, and say which you left out. Existing plan files stay as they are; plans move to the new layout at the next week boundary. **Gate 1: wait for the athlete to confirm the list.** Read only the confirmed ones. A confirmed document that turns out to be marked stale inside is set aside and reported.
5. **Import.** For every anchor record value, date, method (tested, derived, estimated) and source (intervals.icu, the named document, or stated by the athlete). Flag an anchor that is estimated or more than 8 weeks old. Where a document and intervals.icu give different values for a threshold, keep both to show at gate 2; the intervals.icu value is the one that stands unless the athlete says otherwise there.
6. **Collect the rules.** Take every existing rule of the athlete's, one by one, and mark each keep or drop as your recommendation. File the kept ones under the seven headings of the rules template. A rule is dropped only when the athlete says so.
7. **Fill the gaps without asking.** For each thing still missing, try these in order and stop at the first that gives an answer:
   1. *Found*: look again in the confirmed documents and notes.
   2. *Derived*: work it out from intervals.icu. Time available per weekday from the days and durations actually trained over the last 8 weeks, shown as "what you trained, which may be less than what you have free"; pool days and pool length from recent swims; the usual time of day per weekday from the start times of recent activities; which bikes have power and whether a chest strap is used from recent activities; baselines from wellness data.
   3. *Assumed*: take the default you would have recommended. Sport mode and focus from the season plan; readiness bands from the athlete's existing readiness rule, or the starting bands in `coach-rules` when they have none; a target race with no priority takes the one "Races" in `coach-rules` gives; the chat channel is the one this conversation is in; an anchor with no test on record has the method "estimated".

   Mark every such value `found in <document>`, `derived from <what>` or `assumed`. Ask only when none of the three gives an answer and a wrong guess would change what gets planned, and then put every question in one message.
8. **Show everything.** First a short list of what was derived or assumed, so the athlete can correct it in the same reply. Then the whole profile, the whole rules file, each rule with keep or drop already applied as you recommend, and each threshold conflict with both values. **Gate 2: wait for approval.** A correction is applied and shown again; "ok" approves.
9. **Write and commit.** `ATHLETE.md`, `ATHLETE-RULES.md`, and in the season plan replace the goals and anchors sections with one line pointing to the athlete profile. One commit.

Done when the three files exist, the pointer line is in place, the season plan points to the profile, and the commit is made; or when the run is stopped at a gate and the athlete has been told exactly what is waiting.

A run can stop after any step and resume later; say where it stopped.

## Later run

Cover only the section that changed. Show before and after, wait for approval, write, add a change-log line (date, what changed, why), commit.

**An anchor changed** (for example a new FTP):

1. Record value, date, method and source. Ask for the method if the athlete did not give it.
2. Read the same threshold in intervals.icu. If it differs from the new value, show both and ask which stands. When the new value stands, the athlete changes it in intervals.icu; this skill does not write thresholds there.
3. Show old and new values. Once intervals.icu holds the new value, show the zones it calculates.
4. List every approved planned session still ahead whose targets derive from this anchor.
5. On approval, update the profile and its change log, and commit.
6. Offer `coach-adjust` for the sessions in step 4. Their targets change there.

**The profile and intervals.icu differ on a threshold** (often raised by `coach-review-week`): show both values with their dates and ask which stands. Their answer is the approval. Then write the profile, or tell the athlete to change intervals.icu, according to the answer, and continue from step 4 of "An anchor changed". Both stay as they are until the athlete answers.

**A rule changed**: show the rule before and after under its heading, then the same approval, write, commit.

## What goes where

| Fact | Lives in | Notes |
|---|---|---|
| Goals, target races, anchors | athlete profile | the season plan keeps phases, key dates and its own change log |
| Zones | intervals.icu | read when needed |
| Weight, HRV baseline, resting heart rate baseline | computed from wellness data | the profile states how each is computed, never a typed-in value |
| Limitations | athlete profile: what, since when, which athlete rule it triggers | daily pain scores go in the day plan |
| Availability | athlete profile: weekly template (time, fixed commitments, facility access) plus dated exceptions | |
| Keys | key files in the home directory | the index holds paths |

## Keys

A key belongs in its key file and nowhere else. If the athlete sends a key in the chat, write it to that service's key file in the home directory, record the path in the index, and confirm by path alone. Leave the key out of every file in the data folder, every commit and every message you write.

## Boundaries

- Planned sessions belong to `coach-adjust`; this skill lists the affected ones and hands over.
- This skill runs when asked or when a coach skill suggests it, never on a schedule.
- Scheduled jobs are outside this skill. Moving a job to a coach skill is a cut-over step the athlete starts.
- Commit after each write. If the workspace is not a git repository, say so and carry on; setting one up is the athlete's call.

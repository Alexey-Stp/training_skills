# Matt Pocock's skills as a structural template

Research for ticket #6 (part of map #1).

**Question.** How is the `mattpocock/skills` suite organised (how skills are split, how a setup skill configures the rest, how skills share standing context and reference documents, how they are invoked), and which of these patterns transfer to a training skill suite?

## Sources

All claims are read from the upstream repo at commit [`abeeaf9`][root] (`main`, 2026-11-19, plugin version 1.3.2). Paths below are relative to that commit; every link is a permalink to it.

- Cross-checked against the locally installed plugin copy, version 1.3.1. The two differ in 12 skill files, none of them structural. In the setup skill the only differences are a legacy `CONTEXT.md` rename offer and a "tracker needs a reachable repo" paragraph, both added upstream after 1.3.1.
- The stub at [`ctaxnagomi/agent-kd-skill`][stub] is a third-party gallery copy, not a primary source. It keeps the name and a four-line process ("Detect tracker, Configure integration, Set up labels, Verify") and drops everything that makes the original work: the seed templates, the `## Agent skills` block, the domain docs section, and `disable-model-invocation`. Its frontmatter is a JSON object and its description is rewritten as a model trigger, so it would be model-invoked, the opposite of the original. Its "Verify" step contradicts upstream, which rejected a verify mode ([`.out-of-scope/setup-skill-verify-mode.md`][oos-verify]). Do not use it as the reference.

Where a statement is my inference instead of something a file says, it is marked **(inference)**.

## 1. How the suite is split and grouped

**Buckets.** Skills sit in bucket folders under `skills/`: `engineering/` (daily code work), `productivity/` (non-code workflow tools), `misc/` (kept, not promoted), `in-progress/` (public beta, not shipped in the plugin), `deprecated/` (currently empty). Only `engineering/` and `productivity/` are **promoted**: each promoted skill must appear in the top-level `README.md`, in the plugin manifest's `skills` array, and have a human docs page under `docs/<bucket>/<skill>.md` ([`CLAUDE.md`][claude-md]).

**Counts at this commit.** 27 promoted skills: 20 engineering, 7 productivity ([`plugin.json`][plugin-json]). 16 are user-invoked, 11 model-invoked (counted from frontmatter).

**The one axis that splits skills is invocation**, not topic ([`.agents/invocation.md`][invocation]):

- **User-invoked**: only the human typing the name can start it. `disable-model-invocation: true`. No other skill can call it.
- **Model-invoked**: the model can reach for it, another skill can call it, and the human can still type it.

Bucket READMEs and the top-level README list skills under these two headings ([`skills/engineering/README.md`][eng-readme]).

**Roles the skills play** (my grouping of what the files show):

| Role | Examples | Shape |
| --- | --- | --- |
| Entry-point workflows | `to-spec`, `to-tickets`, `triage`, `implement`, `wayfinder`, `teach` | User-invoked; own a multi-step process and write artifacts |
| Thin wrappers | `grill-me` (7 lines), `grill-with-docs` (7 lines), `implement` (17 lines) | User-invoked; body is little more than "call the Skill tool with X" |
| Reusable primitives | `grilling`, `tdd`, `research`, `prototype`, `code-review` | Model-invoked; one discipline, callable by wrappers and by the model |
| Shared vocabulary | `codebase-design`, `domain-modeling`, `writing-for-agents` | Model-invoked; all reference, no steps; the single home for terms several skills need |
| Setup | `setup-matt-pocock-skills` | User-invoked; run once per repo |
| Router | `ask-matt` | User-invoked; maps every user-reachable skill and the flows between them |

**When to split a skill** ([`writing-for-agents/SKILL.md`][wfa], [`SKILL-MECHANICS.md`][mechanics]): by *sequence*, when later visible steps tempt the agent to rush the current one; by *invocation*, when a part needs its own trigger word or another skill must reach it. Each new model-invoked skill costs an always-loaded description, so the independent reach has to be worth it. New skills are otherwise resisted: "If the behaviour composes from existing skills, it does not get a new one" ([`SCOPE.md`][scope]).

**Router.** `ask-matt` exists because user-invoked skills have no description in the model's context, so the human is the index; past a certain count a router skill carries that load. It can only recommend, never fire them ([`SKILL-MECHANICS.md`][mechanics]).

## 2. SKILL.md conventions

**Frontmatter.** Two required keys, `name` and `description`; CI parses every `SKILL.md` and fails on either missing ([`scripts/check-frontmatter.mjs`][check-fm]). Optional keys seen: `disable-model-invocation: true` (16 skills), `argument-hint` (`teach`, `handoff`), `metadata.credits` (`pr`). Values containing `": "` are quoted. `name` equals the folder name.

**Description wording depends on invocation** ([`.agents/invocation.md`][invocation]):

- User-invoked: human-facing one-liner, trigger lists stripped. Example, `teach`: "Teach the user a new skill or concept, within this workspace."
- Model-invoked: what it is, then "Use when ..." with one trigger per distinct case. Example, `tdd`: "Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests."

The description is treated as a *context pointer*: front-load the leading word, one trigger per branch, cut identity the body already carries ([`writing-for-agents/SKILL.md`][wfa]).

**Length.** The 27 promoted `SKILL.md` files run from 7 to 170 lines, 1,858 lines in total (mean about 69, median 71), counted with `wc -l` at this commit. The longest are `pr` (170), `teach` (140), `diagnosing-bugs` (138), `wayfinder` (128) and the setup skill (120).

**Body.** Two content types, *steps* and *reference*. Every step ends on a checkable completion criterion. Stated positively instead of by prohibition. Repeated *leading words* (`frontier`, `tracer bullet`, `seam`) anchor behaviour in few tokens. Each meaning has a single source of truth ([`writing-for-agents/SKILL.md`][wfa]).

**Supporting reference files.** Material only some branches need is moved to a sibling file in the skill's folder and linked with a relative link plus a one-line statement of when to read it. Observed kinds:

- Output formats: `domain-modeling/GLOSSARY-FORMAT.md`, `ADR-FORMAT.md`; `teach/MISSION-FORMAT.md`, `LEARNING-RECORD-FORMAT.md`, `RESOURCES-FORMAT.md`, `GLOSSARY-FORMAT.md`.
- Branch bodies: `prototype/LOGIC.md` and `UI.md`, chosen by which question is being answered ([`prototype/SKILL.md`][prototype]).
- Seed templates the skill copies out: the setup skill's `issue-tracker-*.md`, `triage-labels.md`, `domain.md`.
- Scripts and templates: `wizard/template.sh`, `diagnosing-bugs/scripts/hitl-loop.template.sh`.

Sibling files are named in upper case (`ADR-FORMAT.md`) or lower case (`tests.md`); there is no single rule. The test for moving material out is branching: "inline what every branch needs, and push behind a pointer what only some branches reach" ([`writing-for-agents/SKILL.md`][wfa]).

**Per-skill extras.** Every skill also has `agents/openai.yaml` (Codex picker metadata and the Codex half of the user-invoked flag) ([`.agents/invocation.md`][invocation]).

## 3. How the setup skill configures the rest

Source: [`setup-matt-pocock-skills/SKILL.md`][setup].

**What it is.** User-invoked, "Run once before first use of the other engineering skills". "A prompt-driven skill, not a deterministic script. Explore, present what you found, confirm with the user, then write."

**Process.**

1. **Explore** the repo: git remote, existing `CLAUDE.md` / `AGENTS.md`, `GLOSSARY.md`, `docs/adr/`, prior `docs/agents/` output, `.scratch/`, whether `triage` is installed, monorepo signals.
2. **Present and ask**, one section at a time, leading with the recommended answer. A section is skipped when exploration already settled it.
   - A. Issue tracker: GitHub, GitLab, local markdown, or "other" described in a paragraph.
   - B. Triage labels: one question, "keep the defaults?". Skipped if `triage` is not installed.
   - C. Domain docs: single-context written without asking; multi-context offered only on monorepo signals.
3. **Confirm**: show drafts of everything it will write; the user may edit.
4. **Write.**
5. **Done**: say which skills now read these files, and that the files can be edited by hand; re-running is only for switching tracker or starting over.

**What it writes, and where.** Everything goes into the *user's project repo*, not into the skills:

| Written | Content |
| --- | --- |
| `## Agent skills` block in `CLAUDE.md` (or `AGENTS.md`, whichever exists) | Three sub-headings, each a one-line summary plus "See `docs/agents/<file>.md`". Updated in place on re-run. |
| `docs/agents/issue-tracker.md` | Copied from the matching seed template |
| `docs/agents/triage-labels.md` | Only if `triage` is installed |
| `docs/agents/domain.md` | Consumer rules for the glossary and ADRs |
| Tracker labels | `gh label create` for any configured label the tracker lacks |

It does **not** create `GLOSSARY.md` or any ADR; those are created lazily by `domain-modeling` when a term or decision is actually resolved ([`setup.../domain.md`][setup-domain]).

**The tracker doc is an adapter.** [`issue-tracker-github.md`][tracker-gh] lists concrete commands per operation, then binds the abstract verbs the skills use: "When a skill says "publish to the issue tracker"" then create a GitHub issue; "When a skill says "fetch the relevant ticket"" then read it as shown. Skills stay tracker-neutral and say only "publish to the issue tracker". The local template binds the same verbs to files under `.scratch/` ([`issue-tracker-local.md`][tracker-local]). A third section, "Wayfinding operations", gives `wayfinder` its tracker-specific moves.

**The labels doc is a mapping table.** Five canonical role names in one column, the repo's actual label strings in the other. Skills speak in canonical names ([`triage-labels.md`][labels]).

**Backends are deliberately few.** Three seed templates only; anything else is free prose under "Other", because each backend hard-codes a CLI shape that has to be kept correct ([`.out-of-scope/mainstream-issue-trackers-only.md`][oos-trackers]).

**No verify mode.** To check a setup, re-run the skill and ask it to verify ([`.out-of-scope/setup-skill-verify-mode.md`][oos-verify]).

## 4. How skills share standing context

Three layers, from always-loaded to on-demand.

**Layer 1: the `## Agent skills` block in `CLAUDE.md` / `AGENTS.md`.** One line per topic plus a path. **(inference)** This is how config reaches every skill without each skill reading a file: the harness loads `CLAUDE.md` / `AGENTS.md` into every session, which is why dependent skills say the config "should have been provided to you" instead of "read `docs/agents/...`". The files confirm the wording and the write target; they do not state the mechanism in one sentence.

**Layer 2: `docs/agents/*.md`.** The detail behind each pointer, read when a skill needs to act on the tracker or apply a label.

**Layer 3: the project's own domain docs.** `GLOSSARY.md` at the repo root and ADRs in `docs/adr/NNNN-slug.md`.

- Reading them is passive and cheap: a one-line prose pointer in the consuming skill, for example `tdd`: "read `GLOSSARY.md` (if it exists) so test names and interface vocabulary match the project's domain language" ([`tdd/SKILL.md`][tdd]). If they are missing, "proceed silently" ([`setup.../domain.md`][setup-domain]).
- Writing them is the `domain-modeling` skill only: update the glossary inline the moment a term is resolved; offer an ADR only when the decision is hard to reverse, surprising without context, and a real trade-off ([`domain-modeling/SKILL.md`][dm], [`ADR-FORMAT.md`][adr-format]).
- Glossary format: `**Term**:` definition of one or two sentences, `_Avoid_:` synonyms; no implementation detail ([`GLOSSARY-FORMAT.md`][glossary-format]). The training repo's `GLOSSARY.md` already follows it.

**Hard and soft dependencies** ([ADR 0001][adr1]). Skills that produce *wrong* output without the config carry an explicit one-liner: "... should have been provided to you. If not, tell the user to run `/setup-matt-pocock-skills`." Skills that are merely less sharp without it mention the glossary and ADRs in loose prose and carry no setup pointer. The ADR names `to-tickets`, `to-spec`, `triage` as hard; at this commit the pointer also appears in `code-review`, `implement-spec` and `wayfinder` (grep of the promoted skills), so the list has grown past the ADR text.

**Shared reference between skills.** "Shared reference docs live inside the skill that owns them; other skills reach that material by calling the Skill tool with it, not by linking across folders" ([`.agents/invocation.md`][invocation]). Reference that two user-invoked skills both need lives in a plain file outside the skill system ([`SKILL-MECHANICS.md`][mechanics]).

**A second pattern: the stateful workspace (`teach`).** `teach` needs no setup skill. It treats the current directory as a workspace and keeps all state there: `MISSION.md` (why the person is learning), `learning-records/0001-<slug>.md` (numbered records that drive what comes next, "loosely equivalent to architectural decision records"), `reference/`, `lessons/`, `RESOURCES.md`, `NOTES.md` (stated preferences). If `MISSION.md` is empty its first job is to question the user. Format files for each artifact live in the skill folder; workspace paths resolve from where the skill was run ([`teach/SKILL.md`][teach]). This is the closest upstream analogue to a suite that coaches one person over many sessions.

## 5. How skills call each other

Source: [`.agents/invocation.md`][invocation].

- A dependency is an explicit operative instruction that names the tool: `Call the Skill tool with "grilling"`. Not a `/name` mention, and not a link into another skill's folder.
- One skill per call: "Call the Skill tool twice, for "grilling" and "domain-modeling"".
- Only model-invoked skills can be called. "A user-invoked skill may invoke model-invoked skills, but it can never reach another user-invoked skill."
- When a precondition is a user-invoked skill (setup), the instruction is addressed to the human: "tell the user to run `/setup-matt-pocock-skills`".
- Consequence, visible in the files: logic that more than one entry point needs is extracted into a model-invoked primitive, and the user-invoked skills become thin wrappers. `grill-me` is `Call the Skill tool with "grilling"`; `grill-with-docs` is the same plus `domain-modeling`; `triage`, `wayfinder` and `improve-codebase-architecture` call both mid-process.
- Subagents: a skill that dispatches one says to start it with a fresh context window ([`CLAUDE.md`][claude-md]); used for parallel work (`code-review`'s two axes, `wayfinder`'s research tickets) and to keep bulky reading out of the main context (`research`).
- Handing work between sessions is done with documents, not calls: `handoff` writes a file that names "which skills the next agent should call the Skill tool for".

Observed in this session, on Claude Code with plugin 1.3.1: exactly the 11 model-invoked skills are listed to the model, namespaced as `mattpocock-skills:<name>`; the 16 user-invoked ones are absent from the model's list.

## 6. Packaging and installation

- **Manifest.** [`.claude-plugin/plugin.json`][plugin-json] has `name`, `version`, `description`, `author`, `repository`, `license`, `keywords`, and `skills`: an array of explicit skill-directory paths. Listing paths one by one is what lets a bucketed repo ship only the promoted set ([ADR 0002][adr2]).
- **Marketplace.** [`.claude-plugin/marketplace.json`][marketplace] makes the repo its own single-plugin marketplace (`"source": "./"`). Claude Code's official marketplace lists the plugin separately and pins a commit sha; the repo's own marketplace file is kept as the route for other harnesses and for direct installs ([ADR 0002][adr2]).
- **Install routes** ([`.agents/install-block.md`][install]): Claude Code `claude plugin install mattpocock-skills@claude-plugins-official`; Codex and Copilot add the repo as a marketplace then install; Gemini installs one bucket path at a time; everything else uses `npx skills@latest add mattpocock/skills`, which copies editable files. The plugin and skills.sh routes are exclusive.
- **Versioning.** Managed installs update only when `version` in `plugin.json` changes; a release script copies it from `package.json`; changes are recorded as changesets ([`.agents/install-block.md`][install], [ADR 0002][adr2]).
- **Local development.** `scripts/link-skills.sh` symlinks every skill outside `misc/` and `deprecated/` into `~/.claude/skills` and `~/.agents/skills`, so a `git pull` updates them ([`link-skills.sh`][link]).
- **Repo-level docs for maintainers.** `CLAUDE.md` holds the repo's rules; `.agents/` holds the conventions it points to (invocation, install wording, docs template) and the repo's own ADRs; `GLOSSARY.md` holds the suite's own terms; `SCOPE.md` and `.out-of-scope/` record what is rejected. The suite uses its own conventions on itself.

## 7. Transfer table

Terms on the training side follow the training repo's `GLOSSARY.md`.

| # | Pocock pattern | Training-suite analogue | Verdict | Reason |
| --- | --- | --- | --- | --- |
| 1 | Small skills, split by invocation and by sequence | One skill per coaching job: session review, week plan, month plan, plan update, setup | Transfers | Same rule applies: split where a job needs its own trigger or where later steps would make the agent rush the current one. |
| 2 | User-invoked vs model-invoked, with description wording to match | Entry points the athlete types are user-invoked; shared disciplines are model-invoked | Transfers | It is a harness mechanism, not an engineering one. It also decides what can call what (row 9). |
| 3 | Thin user-invoked wrapper over a model-invoked primitive (`grill-me` over `grilling`) | If a session review must be able to trigger a plan update, the plan-update logic has to be model-invoked, or sit in a shared model-invoked skill with thin wrappers | Transfers | A user-invoked skill can never be called by another skill. This forces the shape wherever two skills share a step. |
| 4 | Shared-vocabulary skill, all reference (`codebase-design`) | One model-invoked skill holding the coaching rules and their vocabulary (zones, load, progression), called by the review and planning skills | Transfers | Gives the coaching method a single source of truth. Costs one always-loaded description. |
| 5 | Sibling reference files behind one-line pointers; split by branch (`prototype/LOGIC.md` vs `UI.md`) | Format files for plans and session reviews beside the skill that writes them; sport mode as a branch (triathlon vs single-sport reference files) | Transfers | Branching is the upstream test for moving material out, and sport mode is exactly such a branch. |
| 6 | Setup skill: explore, present with recommended answers, confirm, write; skip what exploration settled | Athlete setup that creates the athlete profile and the source doc; skips swim and bike questions in a run-only sport mode | Transfers with changes | The process transfers whole. What changes: it writes to the private training data location, not the public skills repo, and what it captures (thresholds, availability, goals) changes over time where tracker config does not. Upstream expects hand edits and a re-run only to switch backend; the profile needs a real keep-current path, which the map still lists as unspecified. |
| 7 | `## Agent skills` block in the project's `CLAUDE.md` / `AGENTS.md`: one line per topic plus a path | The same block in the `CLAUDE.md` of the private training data directory, pointing at the athlete profile, the activity source doc and the plan layout | Transfers with changes | Works only if the skills are run from that directory, since that is the file the harness loads. Upstream can assume this (the project repo); the training suite must state it. |
| 8 | `docs/agents/issue-tracker.md`: concrete commands, then "when a skill says X, do Y" | Activity source doc: "when a skill says fetch the activity / fetch wellness data / do the calendar sync", with the intervals.icu and Garmin specifics | Transfers with changes | The adapter idea transfers exactly and keeps the skills source-neutral. Upstream picks one backend from several seed templates; the training suite has one fixed arrangement with a primary and a secondary source, so one template, and it must also say which source owns which data. |
| 9 | Skill-to-skill calls: `Call the Skill tool with "name"`, one per call, model-invoked targets only; user-invoked preconditions addressed to the human | Same wording in the training skills | Transfers | Harness-level convention with a stated reason (higher hit rate than a `/name` mention). |
| 10 | Hard vs soft dependency on setup (ADR 0001) | Every coaching skill is hard-dependent on the athlete profile and carries the one-line pointer to the setup skill | Transfers with changes | The rule transfers; the split mostly collapses, because a review or plan without zones and availability is wrong, not merely fuzzy. |
| 11 | "Proceed silently" when glossary or ADRs are missing; create files lazily | Lazy creation for plan and review folders; not for the athlete profile | Transfers with changes | Lazy creation suits artifacts that accumulate. A missing profile must stop the skill (row 10). What to do when activity data is missing is a separate, still-open question on the map. |
| 12 | `GLOSSARY.md` in the project repo, read by every skill, written only by `domain-modeling` | The suite's `GLOSSARY.md` | Transfers with changes | Already in use for designing the suite. But upstream's glossary lives where the skills run. The training glossary lives in the public skills repo, which is not the working directory at coaching time, so the skills will not see it there. The vocabulary has to reach runtime another way: inside the shared coaching skill (row 4), or seeded into the private directory by setup. |
| 13 | ADRs: `docs/adr/NNNN-slug.md`, one paragraph, only when hard to reverse, surprising, and a real trade-off | (a) Design decisions about the suite, in the skills repo. (b) Standing coaching decisions about the athlete, in private training data | (a) Transfers. (b) Transfers with changes | (a) is the same use. (b) is closer to `teach`'s numbered learning records than to ADRs: records that later sessions read to decide what comes next. The three-part test for when to write one still fits. |
| 14 | `teach`'s stateful workspace: mission file, numbered records, notes file for preferences, formats owned by the skill | Private training data layout: athlete profile (goals play the mission's role), plans at three resolutions, session reviews, a notes file for stated preferences | Transfers | The strongest structural analogue upstream: one person, many sessions, state in files in the working directory, each new session computed from the records. |
| 15 | `triage-labels.md`: canonical role names mapped to local label strings | No direct analogue | Does not transfer | There is no state machine of labels in the training domain. The underlying idea (skills speak canonical names, one table maps them to the external system's strings) could be reused inside the activity source doc for sport and zone names if intervals.icu and Garmin name them differently. |
| 16 | Router skill (`ask-matt`) | None for now | Does not transfer | It exists to index 16 user-invoked skills. A handful of entry points does not need one. |
| 17 | Bucket folders with promoted and non-promoted sets | A flat `skills/` folder | Does not transfer | Buckets exist to curate a large public catalogue and to keep drafts out of the plugin. A flat layout is also what single-path harnesses need. |
| 18 | `.claude-plugin/plugin.json` with an explicit `skills` array, plus `marketplace.json` making the repo its own marketplace | The same two files in the training skills repo | Transfers | It is the documented way to install a repo's skills as one unit, and public repo plus private data is exactly the split it supports. |
| 19 | Official-marketplace listing, multi-harness install block, `agents/openai.yaml`, changesets and release workflow, `docs/` pages, `SCOPE.md` and `.out-of-scope/` | None | Does not transfer | All of it serves many users, several harnesses and outside contributors. One athlete on one harness needs none of it. `openai.yaml` would matter only if Codex is used. |
| 20 | Fresh-context subagents for bulky reading and parallel work | Fetching and summarising raw activity data in a subagent | Transfers with changes | The convention is sound, but whether activity payloads are large enough to need it depends on what the activity sources return, which other tickets answer. |
| 21 | Writing rules from `writing-for-agents`: completion criterion per step, leading words, positive phrasing, single source of truth, no restating what the environment already says | Same rules for the training skills | Transfers | Domain-independent. The skill itself can be called when the training skills are written. |

### What the table adds up to

- Take the *mechanics* whole: invocation split, description wording, Skill-tool calls, sibling reference files, plugin manifest, writing rules.
- Take the *setup pattern* with one structural change: its output, and the `CLAUDE.md` block that points to it, live in the private training data directory, and the skills are run from there.
- For *standing state*, model on `teach` more than on the engineering skills: the engineering skills keep state in a tracker and a codebase, `teach` keeps it in files about one person.
- Leave the *catalogue machinery* behind: buckets, router, docs pages, multi-harness distribution, scope policing.

## Not verified

- The mechanism in section 4, layer 1 (harness loads `CLAUDE.md`, so the block reaches every skill) is inferred from the wording and the write target, not stated outright in one place.
- How a bare name in `Call the Skill tool with "grilling"` resolves to the namespaced `mattpocock-skills:grilling` under a plugin install. The namespaced listing was observed; the resolution was not tested.
- Install commands were read, not run. In particular, the exact Claude Code commands for installing from a personal repo's own `marketplace.json` are described in ADR 0002 as "`marketplace add` then `install`" without the full command line.
- Behaviour on harnesses other than Claude Code (Codex, Copilot, Gemini) is as the repo's own docs report it.
- The published docs site (`aihero.dev`) and the official marketplace listing were not read; only the repo was.

[root]: https://github.com/mattpocock/skills/tree/abeeaf95660ba9e8b7c753eb38f441ca707a8823
[stub]: https://github.com/ctaxnagomi/agent-kd-skill/blob/54f683102875076913305d6a39b653cb92e635b7/skills/custom/setup-matt-pocock-skills/SKILL.md
[claude-md]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/CLAUDE.md
[scope]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/SCOPE.md
[plugin-json]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/.claude-plugin/plugin.json
[marketplace]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/.claude-plugin/marketplace.json
[invocation]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/.agents/invocation.md
[install]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/.agents/install-block.md
[adr1]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/.agents/adr/0001-explicit-setup-pointer-only-for-hard-dependencies.md
[adr2]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/.agents/adr/0002-ship-as-a-claude-code-plugin.md
[oos-verify]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/.out-of-scope/setup-skill-verify-mode.md
[oos-trackers]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/.out-of-scope/mainstream-issue-trackers-only.md
[check-fm]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/scripts/check-frontmatter.mjs
[link]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/scripts/link-skills.sh
[eng-readme]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/engineering/README.md
[setup]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/engineering/setup-matt-pocock-skills/SKILL.md
[setup-domain]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/engineering/setup-matt-pocock-skills/domain.md
[tracker-gh]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/engineering/setup-matt-pocock-skills/issue-tracker-github.md
[tracker-local]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/engineering/setup-matt-pocock-skills/issue-tracker-local.md
[labels]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/engineering/setup-matt-pocock-skills/triage-labels.md
[dm]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/engineering/domain-modeling/SKILL.md
[adr-format]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/engineering/domain-modeling/ADR-FORMAT.md
[glossary-format]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/engineering/domain-modeling/GLOSSARY-FORMAT.md
[tdd]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/engineering/tdd/SKILL.md
[prototype]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/engineering/prototype/SKILL.md
[teach]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/productivity/teach/SKILL.md
[wfa]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/productivity/writing-for-agents/SKILL.md
[mechanics]: https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/productivity/writing-for-agents/SKILL-MECHANICS.md

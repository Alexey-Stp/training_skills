# OpenClaw skills: format, and running one suite in OpenClaw and Claude Code

Research for [issue #16](https://github.com/Alexey-Stp/training_skills/issues/16). Researched 2026-11-19.

Sources are primary only: the OpenClaw docs (`docs.openclaw.ai`), the OpenClaw source (`github.com/openclaw/openclaw`, `main`), the Agent Skills specification (`agentskills.io`), the Claude Code docs (`code.claude.com`), and a read-only look at the athlete's local OpenClaw install (version `2026.9.8`). Only the structure of the local install is described here; none of its content is reproduced.

Confidence markers used below:

- **[doc]** stated in official documentation (link given).
- **[src]** read in the OpenClaw source.
- **[local]** observed in the local install or its CLI help.
- **[inferred]** follows from documented facts but is not stated outright.
- **[unverified]** not confirmed by any source; needs a test.

Caveat that applies throughout: the docs describe the current OpenClaw release, while the local install is `2026.9.8`. Anything marked [doc] may differ slightly on the installed version until it is updated.

## Short answer

- OpenClaw and Claude Code both implement the Agent Skills format: a folder holding a `SKILL.md` with YAML frontmatter (`name`, `description`) and a Markdown body. A skill written to the common subset runs unchanged in both.
- The two frontmatter keys the suite most needs beyond the basics, `user-invocable` and `disable-model-invocation`, are spelled the same and mean the same in both runtimes.
- OpenClaw can install a Claude Code plugin directory directly as a "Claude bundle" and load its `skills/` as ordinary OpenClaw skills. So one repo laid out as a Claude Code plugin is installable in both.
- Standing context differs and is the real portability risk: OpenClaw injects workspace files (`AGENTS.md`, `SOUL.md`, `USER.md`, ...) into the prompt, Claude Code injects `CLAUDE.md` or `AGENTS.md` from the working directory. Skills should depend on neither and read the index file in `training/` themselves.
- Recommendation: one `skills/` tree in this repo, restricted to the common subset, plus a Claude Code plugin manifest. Install it in OpenClaw as a linked bundle (or through `skills.load.extraDirs`) and in Claude Code as a plugin. Skip ClawHub.

## 1. How OpenClaw defines a skill

### File format

- A skill is a directory containing `SKILL.md`: YAML frontmatter plus a Markdown body. `name` and `description` are the minimum fields. [doc: [Skills](https://docs.openclaw.ai/tools/skills)]
- The skill name and its slash command come from the `name` field, falling back to the directory name. [doc: Skills]
- Authoring guidance: `name` in lowercase letters, digits and hyphens, matching the directory; `description` on one line, under 160 characters. [doc: [Creating skills](https://docs.openclaw.ai/tools/creating-skills)]
- `{baseDir}` in the body refers to the skill's own folder, for pointing at bundled scripts. [doc: Skills, Creating skills]
- Supporting files sit beside `SKILL.md`. The local skills use `scripts/` and `references/` subfolders, as the Agent Skills spec suggests. [local]

### Frontmatter keys

| Key | Default | Effect |
|---|---|---|
| `name` | directory name | Skill name and slash command |
| `description` | none | Shown to the model and in command discovery |
| `user-invocable` | `true` | Exposes the skill as a slash command |
| `disable-model-invocation` | `false` | Keeps the skill out of the model's normal prompt; still usable as a slash command |
| `command-dispatch` | none | `tool` sends the slash command straight to a tool, with no model turn |
| `command-tool` | none | The tool to call when `command-dispatch: tool` |
| `command-arg-mode` | `raw` | How arguments are forwarded to that tool |
| `homepage` | none | Link shown in the Skills UI |
| `metadata` | none | Holds the `openclaw` block, see below |

Source: [doc: Skills].

### Gating with `metadata.openclaw`

A skill with no `metadata.openclaw` block is eligible unless disabled. With the block, these fields decide whether the skill is offered at all [doc: Skills]:

- `requires.bins`: every listed binary must be on `PATH`.
- `requires.anyBins`: at least one must be on `PATH`.
- `requires.env`: every variable must be set in the process or supplied through config.
- `requires.config`: every listed `openclaw.json` path must be truthy.
- `os`: hard platform filter (`darwin`, `linux`, `win32`).
- `always`: include the skill and skip the `requires.*` checks (`os` still applies).
- `primaryEnv`: the variable that `skills.entries.<name>.apiKey` fills.
- `skillKey`, `emoji`, `homepage`, `install`: config key override, UI details and installer specs.

Notes:

- The legacy `metadata.clawdbot` block is no longer read by the runtime. [doc: Skills]
- OpenClaw parses the frontmatter as YAML first, then flattens a nested `metadata` block to JSON. The authoring example writes `metadata` as single-line JSON. [doc: Skills, Creating skills] Whether a multi-line YAML `metadata.openclaw` block works on `2026.9.8` is [unverified].
- `openclaw skills check` reports which skills are ready, visible or missing requirements. [doc: Skills] [local: CLI help]
- None of the five skills in the local workspace uses `metadata` or any key other than `name` and `description`. [local]

### Install locations and precedence

Highest wins when a name appears twice [doc: Skills]:

1. `<workspace>/skills` (per-agent)
2. `<workspace>/.agents/skills`
3. `~/.agents/skills`
4. `<state-dir>/skills` (shared "managed" skills, `~/.openclaw/skills` by default)
5. Workshop skills (agent-written)
6. Bundled skills shipped with OpenClaw
7. `skills.load.extraDirs` and plugin skills (lowest)

Other loading rules [doc: Skills]:

- Discovery finds any `SKILL.md` up to 6 levels below a root; grouping folders are allowed.
- A skill root's real path must stay inside the configured root. Symlinks pointing outside need `skills.load.allowSymlinkTargets`.
- `skills.load.watch` defaults to `true`: edits are picked up, and existing sessions see changed skills on their next turn.
- `agents.defaults.skills` and `agents.entries.*.skills` are optional allowlists; unset means unrestricted.
- `skills.entries.<key>.enabled: false` disables one skill.

The local install matches this: the athlete's own skills live in `workspace/skills/<name>/` and show as source `openclaw-workspace` in `openclaw skills list`; plugin-provided skills show as `openclaw-extra`. [local]

### Installing

Commands, from [doc: Skills] and confirmed against `openclaw skills install --help` [local]:

- `openclaw skills install @owner/<slug>`: from ClawHub into the workspace `skills/` folder.
- `openclaw skills install git:owner/repo@ref`: from git.
- `openclaw skills install ./path --as <slug>`: from a local directory.
- `--global` installs into the shared managed directory instead of the workspace.
- Git and local installs need `SKILL.md` at the source root. [doc: Skills] So a repo holding several skills cannot be installed with one `git:` reference; each skill folder is installed separately. [inferred]

### ClawHub

- ClawHub is the public registry. A published skill is a folder with `SKILL.md`; the bundle limit is 50 MB. [doc: [Skill format](https://docs.openclaw.ai/clawhub/skill-format)]
- Publish with `clawhub skill publish ./my-skill --slug ... --owner ...`. New skills start at `1.0.0`; later changes auto-publish a patch version. A reusable GitHub workflow publishes every folder under `skills/`. [doc: [Publishing](https://docs.openclaw.ai/clawhub/publishing)]
- Every published skill is licensed MIT-0, with no per-skill override. [doc: Skill format]
- ClawHub's scanner compares the code with the declared environment variables (`requires.env`, `primaryEnv`, `envVars`) and flags undeclared ones. [doc: Skill format]
- Releases stay hidden until security checks pass. [doc: Publishing]
- Whether a skill can be published privately is not stated. [unverified]

## 2. How skills reach the model and get invoked

### Listing

- Eligible skills are rendered into the system prompt as a compact `<available_skills>` XML block giving each skill's name, description and file location. [doc: Skills, [System prompt](https://docs.openclaw.ai/concepts/system-prompt)]
- The model is told to scan that block and, on a clear match, read the `SKILL.md` at the listed location (or call `skills_read`) before acting. It loads at most one skill up front. [src: `src/agents/system-prompt-skills.ts`]
- The body is therefore loaded on demand, not up front. Cost per listed skill is about 97 characters plus the name, description and location. [doc: Skills]
- `skills.limits.maxSkillsPromptChars` caps the block; when it is hit, descriptions are shortened and then dropped. Descriptions are compacted to at most 220 characters under context pressure. [doc: Skills] [src: `src/skills/loading/skill-contract.ts`]
- Eligible skills are snapshotted at session start and refreshed on change. [doc: Skills]

### Slash commands

- `/skill <name> [input]` always works. A skill also registers as `/<name>` directly. [doc: [Slash commands](https://docs.openclaw.ai/tools/slash-commands)]
- Command names are sanitized to `a-z0-9_`, at most 32 characters; collisions get a numeric suffix. A skill whose name clashes with a built-in command gets a suffixed name. [doc: Slash commands]
- Lookup treats spaces, underscores and hyphens alike, so `/skill week_review` finds a skill named `week-review`. [src: `src/skills/discovery/chat-command-invocation.ts`]
- A `$skill-name` reference inside a message also selects a skill. [doc: Slash commands] [src: same file]
- By default the command becomes a normal model turn with the skill attached as an explicit selection (name plus path to its `SKILL.md`); text after the command name is passed on as the user's input. [src: same file] The exact wording the model sees for that selection was not traced. [unverified]
- `command-dispatch: tool` skips the model entirely. [doc: Slash commands]

### Chat channels (Telegram)

- A plain chat message is an ordinary agent turn, so the model picks a skill from `<available_skills>` by its description. No per-channel skill wiring is needed. [inferred from doc: System prompt, Skills]
- `commands.nativeSkills` (default `"auto"`) registers skill commands natively; "auto" is on for Telegram and Discord, off for Slack. Per-channel override: `channels.<provider>.commands.nativeSkills`. [doc: Slash commands]
- Telegram's command menu is registered at startup with `setMyCommands`. Names must be `a-z`, `0-9`, `_`, 1 to 32 characters. When the menu overflows, per-skill entries are dropped and replaced by the generic `/skill`; dropped commands still work when typed. [doc: [Telegram message behavior](https://docs.openclaw.ai/channels/telegram/messaging)]
- Consequence for naming: keep skill names at 32 characters or fewer and distinct after hyphens become underscores. [inferred]

## 3. How standing context reaches a skill

OpenClaw does not hand context to a skill. Context is injected into the session's system prompt, and the skill body is read into that same session.

- Injected workspace files: `AGENTS.md`, `SOUL.md`, `IDENTITY.md`, `USER.md`, `MEMORY.md` when present, and `BOOTSTRAP.md` on a brand-new workspace. [doc: System prompt]
- Caps: `agents.defaults.bootstrapMaxChars` 20000 per file and `bootstrapTotalMaxChars` 60000 in total; truncated files get a notice telling the model to read them directly. `USER.md` has its own 4,000-character budget. [doc: System prompt, [Agent workspace](https://docs.openclaw.ai/concepts/agent-workspace)]
- `MEMORY.md` loads only in the main, private session, not in shared or group contexts. [doc: Agent workspace]
- Daily notes in `memory/YYYY-MM-DD.md` are not injected. The model reads them on demand with `memory_search` and `memory_get`. [doc: System prompt]
- Sub-agent sessions get `AGENTS.md` only. [doc: System prompt]
- The workspace is the default working directory for file tools but not a sandbox; absolute paths reach the rest of the host unless sandboxing is on. [doc: Agent workspace]
- Config, credentials, sessions and managed skills live outside the workspace under `~/.openclaw/`. [doc: Agent workspace]

Structural observations from the local install [local]:

- The workspace holds `AGENTS.md`, `SOUL.md`, `IDENTITY.md`, `USER.md`, a `memory/` folder of dated notes, `skills/`, and the `training/` folder. There is no separate `TOOLS.md`; its content has been folded into `AGENTS.md`.
- `AGENTS.md` is about 17,700 characters, close to the 20,000-character per-file cap. `USER.md` is slightly over the 4,000-character budget, so it may already be truncated.
- `AGENTS.md` carries domain rules (activity naming, review flow, tool notes) alongside generic operating instructions. Coaching rules kept there are invisible to Claude Code unless it is pointed at that file.
- The workspace is a git repository.

Consequences for the suite:

- A skill cannot assume `AGENTS.md` or `USER.md` content is present: it is absent in Claude Code, reduced in sub-agents, and dropped in light-context scheduled runs.
- Each skill should start by reading the index file in `training/` (the decision in issue #8) and whatever that index points to.
- Coaching rules belong in the skills (shared, model-invoked primitives), not in `AGENTS.md`, which has little headroom left.

## 4. Scheduled runs

OpenClaw's scheduler is called Automations; `openclaw cron` is an alias for `openclaw automations`. [doc: [Automations](https://docs.openclaw.ai/automation/cron-jobs)] [local: CLI help]

- Jobs run inside the Gateway process, which must be running. Definitions and history persist in OpenClaw's SQLite state. [doc: [How automations work](https://docs.openclaw.ai/automation/cron-jobs/how-it-works)]
- Schedules: `--at` (one-shot), `--every` (interval), `--cron` (5- or 6-field expression) with `--tz <IANA zone>`. Without `--tz` a cron expression uses the Gateway host's timezone. [doc: [Schedules](https://docs.openclaw.ai/automation/cron-jobs/schedules)]
- Payloads: `--system-event` (a turn in the main session), `--message` (a model-backed agent turn), `--command` (shell, no model), `--script`. [doc: [Payloads](https://docs.openclaw.ai/automation/cron-jobs/payloads)]
- Session styles: `main`, `isolated` (a fresh `cron:<jobId>` session each run), `current`, and `session:<id>` (persistent named session). [doc: Payloads]
- `--light-context` skips workspace bootstrap file injection. [doc: Payloads] So a normal isolated run does receive `AGENTS.md` and the other bootstrap files. [inferred]
- `--tools` restricts the tools available to the run; `--model` and `--thinking` override per job. [doc: Payloads]
- Delivery: `--announce --channel telegram --to <chat id>`, with `<chat id>:topic:<n>` for a forum topic; `--no-deliver` suppresses delivery; a reply of `NO_REPLY` suppresses the announcement without failing the run. [doc: [Delivery](https://docs.openclaw.ai/automation/cron-jobs/delivery)]
- `HEARTBEAT.md` is no longer read by the runtime; heartbeat tasks migrate into ordinary jobs through `openclaw doctor --fix`. [doc: Schedules] The local CLI prints an upgrade tip recommending that command, so the local automation storage may still be in a legacy form. [local]

How a scheduled run triggers a skill:

- A scheduled agent turn is a model turn, so the skills list applies and the model can pick a skill named or described in `--message`. [inferred] The docs do not say this outright.
- Whether a `--message` beginning with `/skill <name>` or `/<name>` is expanded the way a chat message is, was not confirmed; the expansion code sits in the chat reply path. [unverified] Until tested, write the message in plain language and name the skill, for example "Run the `<skill-name>` skill for today".
- A scheduled run has no human present, so a skill used this way must not stop to ask questions. It should decide from data or report what is missing. [inferred]

Illustrative job (flags are documented; the combination is not copied from the docs):

```bash
openclaw automations add \
  --name "Morning session check" \
  --cron "0 7 * * *" --tz <IANA zone> \
  --session isolated \
  --message "Run the <skill-name> skill for today and report the result." \
  --announce --channel telegram --to "<chat id>"
```

## 5. Secrets and environment

- `skills.entries.<key>.env` and `skills.entries.<key>.apiKey` in `openclaw.json` are applied to the process environment for the duration of an agent run, then restored. `apiKey` fills the skill's `primaryEnv` and may be a plaintext string or a SecretRef. [doc: Skills, [Config: MCP, skills, plugins](https://docs.openclaw.ai/gateway/config-extensions)]
- That injection reaches the host process only, not a sandbox. [doc: Skills]
- General environment sources: the parent process, `.env` in the working directory, `~/.openclaw/.env`, `env.vars` in config, and optional login-shell import. [doc: [Environment variables](https://docs.openclaw.ai/gateway/configuration/environment-variables)]
- The docs do not state that these variables are inherited by commands the agent runs with its exec tool, although per-run injection into `process.env` implies it. [inferred]
- `requires.env` hides a skill when a variable is missing. [doc: Skills]

Fit with issue #8 (keys in per-service files in the home directory):

- Both runtimes can read the same key files, so no secret needs to live in `openclaw.json` or in Claude Code settings.
- Do not gate the suite's skills with `requires.env`: with file-based keys the variables are unset and the skills would silently disappear from OpenClaw.
- A skill should name the key file's location through the index file, never contain a key. The workspace docs give the same advice: keep secrets out of the workspace. [doc: Agent workspace]

## 6. Side by side with Claude Code

| Aspect | OpenClaw | Claude Code |
|---|---|---|
| Skill unit | Folder with `SKILL.md`, YAML frontmatter, Markdown body | Same |
| Required frontmatter | `name`, `description` | None strictly; `description` recommended; `name` defaults to the directory |
| Unknown frontmatter keys | Not stated [unverified]; `metadata` is the designated extension point | Ignored without error |
| `user-invocable` | Default `true`; `false` removes the slash command | Default `true`; `false` hides it from the `/` menu |
| `disable-model-invocation` | `true` keeps it out of the model's prompt | `true` stops Claude loading it automatically |
| Gating | `metadata.openclaw.requires.*`, `os`, `always` | None; `paths` limits automatic activation by file glob |
| Runtime-only keys | `command-dispatch`, `command-tool`, `command-arg-mode`, `homepage` | `allowed-tools`, `disallowed-tools`, `model`, `effort`, `context`, `agent`, `hooks`, `paths`, `arguments`, `argument-hint`, `when_to_use`, `shell` |
| Skill folder variable | `{baseDir}` | `${CLAUDE_SKILL_DIR}` |
| Argument substitution | None for skills; input follows the command as text | `$ARGUMENTS`, `$0`, named arguments |
| Shell preprocessing | None | `` !`cmd` `` runs before the skill is sent |
| Personal location | `<workspace>/skills`, `~/.openclaw/skills` | `~/.claude/skills/<name>/` |
| Project location | `<workspace>/.agents/skills` | `.claude/skills/<name>/` |
| Packaged form | Plugin or bundle; ClawHub skill | Plugin with `skills/`, namespaced `/plugin:skill` |
| Listing to the model | `<available_skills>` block: name, description, location | Descriptions always in context; listing truncated at 1,536 characters per skill |
| Loading the body | Model reads `SKILL.md` on a match | Loaded when invoked |
| User invocation | `/name`, `/skill name`, `$name`, native Telegram commands | `/name` or `/plugin:name` |
| Standing context | `AGENTS.md`, `SOUL.md`, `IDENTITY.md`, `USER.md`, `MEMORY.md` from the workspace | `CLAUDE.md` files; `AGENTS.md` when no `CLAUDE.md` exists (v2.1.277+) |
| Scheduling | Automations in the Gateway; delivers to chat | Desktop local tasks (app open, machine awake), cloud tasks (fresh clone, no local files), `/loop` in a session |
| Secrets | `skills.entries.*.env` / `apiKey`, SecretRefs | `env` in settings; plugin `userConfig` (sensitive values are not substituted into skill text) |
| Chat channels | Built in (Telegram and others) | Channels through an MCP server plugin |

Sources for the Claude Code column: [Skills](https://code.claude.com/docs/en/skills), [Plugin manifest reference](https://code.claude.com/docs/en/plugins-reference), [Memory](https://code.claude.com/docs/en/memory), [Desktop scheduled tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks). OpenClaw column: the pages cited in sections 1 to 5.

### The shared standard

- Claude Code states that its skills follow the Agent Skills open standard and that it accepts but ignores standard fields it does not act on, such as `metadata`. [doc: Claude Code Skills]
- The standard requires `name` (1 to 64 characters, lowercase letters, digits and hyphens, matching the directory) and `description` (up to 1,024 characters), and suggests `scripts/`, `references/` and `assets/` with paths written relative to the skill root. [doc: [Agent Skills specification](https://agentskills.io/specification)]
- The standard defines `metadata` as a map of string keys to string values. OpenClaw's nested `metadata.openclaw` object goes beyond that. Claude Code ignores it either way, but a strict validator such as `skills-ref validate` may reject it. [inferred]
- ClawHub's own format page refers to "portable Agent Skills" and the same naming rule. [doc: ClawHub Skill format]

### OpenClaw already bridges to Claude Code

- OpenClaw installs Claude Code plugins as "Claude bundles". Detection is by `.claude-plugin/plugin.json` or by the default plugin layout (`skills/`, `commands/`, ...). The bundle's skill roots "load as normal OpenClaw skills". [doc: [Plugin bundles](https://docs.openclaw.ai/plugins/bundles)]
- Install with `openclaw plugins install ./my-bundle`, or from a Claude marketplace with `openclaw plugins install <plugin> --marketplace <source>`. `-l, --link` links a local path instead of copying. [doc: Plugin bundles] [local: CLI help]
- Limits of bundles: `hooks/hooks.json` is detected but not executed; only supported MCP, LSP and settings content is mapped. [doc: Plugin bundles]
- Plugin skills sit at the lowest precedence, alongside `extraDirs`. [doc: Skills] The bundles page does not say whether bundle skill names are prefixed or how they are gated. [unverified]
- `openclaw migrate claude` copies Claude Code skills that contain a `SKILL.md` into the workspace skills folder and appends `CLAUDE.md` into `AGENTS.md`. [doc: [Migrating from Claude](https://docs.openclaw.ai/install/migrating-claude)]
- When OpenClaw runs on its `claude-cli` backend it passes eligible skills to Claude Code as a temporary plugin through `--plugin-dir`. [doc: Skills]

These three facts show the formats are treated as interchangeable by OpenClaw itself.

## 7. Shipping one suite to both

### The common subset

A `SKILL.md` that both runtimes run unchanged:

- Frontmatter limited to `name`, `description`, and where needed `user-invocable` and `disable-model-invocation`.
- `name` lowercase with hyphens, equal to the folder name, 32 characters or fewer, unique after hyphens become underscores (Telegram and OpenClaw command rules).
- `description` on one line. Put the trigger words in the first 160 characters, because OpenClaw recommends that length and compacts to 220.
- File references written relative to the skill folder (`scripts/x.py`, `references/y.md`). Both runtimes tell the model where the skill lives: OpenClaw lists the location, Claude Code states the skill's base directory on load. Avoid both `{baseDir}` and `${CLAUDE_SKILL_DIR}`. Whether OpenClaw's model reliably resolves a relative path against the listed location in every session type is [unverified]; the Agent Skills spec prescribes this form.
- Instructions in runtime-neutral words ("read the file", "run the command") rather than tool names such as `exec` or `Bash`.
- No Claude-only mechanics: `` !`cmd` `` preprocessing, `$ARGUMENTS`, `context: fork`, `allowed-tools`, `hooks`.
- No OpenClaw-only mechanics: `command-dispatch`, `requires.env` gating.
- No reliance on standing context. First step of every skill: read the index file in `training/`.
- No reliance on asking the user, for skills that scheduled runs will trigger.

This maps onto the split decided in issue #6: user-invoked skills keep the defaults; shared coaching primitives set `user-invocable: false` so they stay out of both command menus but remain model-invocable.

### Options

**A. Shared `SKILL.md` files, one tree.** The repo holds `skills/<name>/SKILL.md` written to the common subset. Each runtime is pointed at the same files.
- For: one source of truth; no build step; matches the Agent Skills standard and the Matt Pocock layout.
- Against: the common subset rules out per-runtime conveniences; discipline is needed to keep runtime-specific wording out.

**B. Per-runtime adapter document.** Skills stay neutral, and a small adapter per runtime carries what differs: where the data folder is, how to send a message, how scheduling works.
- For: keeps runtime detail out of every skill; easy to extend.
- Against: one more file to load per run; an adapter delivered as standing context (`AGENTS.md`, `CLAUDE.md`) is missing in sub-agents and light-context runs. Delivered as a model-invoked primitive skill or through the `training/` index it avoids that.
- The index file from issue #8 already plays most of this role for data location.

**C. Symlink or copy install.** Install by linking or copying each skill folder into `workspace/skills/` and `~/.claude/skills/`.
- For: highest precedence in OpenClaw; unprefixed `/name` commands in Claude Code.
- Against: OpenClaw rejects symlinks that resolve outside the skills root unless `skills.load.allowSymlinkTargets` lists the target; symlinks on Windows need extra privileges; copies drift from the repo.
- A cleaner OpenClaw variant with no links: add the clone's `skills/` folder to `skills.load.extraDirs`. A `git pull` then updates the suite. It loads at the lowest precedence.

**D. Claude Code plugin plus ClawHub.** Ship a Claude Code plugin (`.claude-plugin/plugin.json`, optionally `marketplace.json`) and publish each skill to ClawHub.
- Plugin for: versioned install and update in Claude Code; the same directory installs in OpenClaw as a Claude bundle.
- Plugin against: skills are namespaced `/plugin-name:skill-name` in Claude Code.
- ClawHub for: `openclaw skills install @owner/slug` and updates into the workspace folder.
- ClawHub against: forces an MIT-0 licence, publishes one skill at a time, adds scanning and a registry account, and serves discovery by other people, which the map puts out of scope.

### Recommendation

Combine A with the plugin half of D, and use the `training/` index as the adapter (B).

1. Lay the repo out as a Claude Code plugin whose skills are the common-subset `skills/<name>/SKILL.md` tree: `.claude-plugin/plugin.json` at the root, plus `.claude-plugin/marketplace.json` so the repo is its own marketplace.
2. OpenClaw (priority): clone the repo and install it as a linked Claude bundle, `openclaw plugins install --link <clone path>`. If the bundle route misbehaves on the installed version, fall back to `skills.load.extraDirs` pointing at `<clone>/skills`. Both leave the repo as the single copy.
3. Claude Code: add the repo as a marketplace and install the plugin, or run with `--plugin-dir <clone path>` during development. Start Claude Code with the OpenClaw workspace as the working directory so `training/` resolves the same way.
4. Keep runtime differences out of the skills. Data location and key-file locations come from the `training/` index (issue #8). Scheduling and delivery are configured in OpenClaw's Automations, outside the skills.
5. Do not publish to ClawHub. Revisit only if the suite is ever offered to other people.

Points to settle when the suite is built:

- Precedence. Bundle and `extraDirs` skills load at the lowest precedence, so an existing workspace skill with the same name wins. New skill names must not collide with the athlete's current workspace skills or with bundled skills, or the old workspace skills must be retired.
- Claude Code instructions. With the workspace as working directory and no `CLAUDE.md` there, Claude Code reads the workspace `AGENTS.md`, which is written for the OpenClaw agent. A small `CLAUDE.md` in the workspace that points at the `training/` index prevents that; OpenClaw does not treat `CLAUDE.md` as a bootstrap file. [inferred from doc: Memory, System prompt]
- Command names. In Claude Code the commands are `/plugin-name:skill-name`; in OpenClaw `/skill_name`. A short plugin name keeps the first form usable.

## Unverified items to test

1. That `openclaw plugins install --link` on a Claude-plugin-shaped repo exposes its skills on version `2026.9.8` on Windows, and whether their names gain a prefix.
2. That a scheduled `--message` starting with `/skill <name>` is expanded like a chat command.
3. That a default isolated scheduled run receives the bootstrap files and the skills list (inferred from the `--light-context` description only).
4. That OpenClaw tolerates frontmatter keys it does not know. The suite avoids them, so this matters only if Claude-only keys are added later.
5. That a multi-line YAML `metadata.openclaw` block parses on the installed version. The suite does not need gating, so this is low priority.
6. That the model in OpenClaw resolves skill-relative paths correctly without `{baseDir}`.
7. The exact text the model receives when a skill is selected by slash command.
8. Whether ClawHub supports private skills.

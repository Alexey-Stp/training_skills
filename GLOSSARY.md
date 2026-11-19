# Training Skills

Agent skills that coach a single athlete: reviewing completed training and planning what comes next.

## Language

**Athlete**:
The one person the skills coach.
_Avoid_: User, client

**Sport mode**:
Which sports a plan covers. Triathlon (swim, bike and run in one combined plan) is the default; a single-sport mode such as run-only is the alternative.

**Focus**:
The sport given priority inside a plan: it carries the hard sessions and the progression while the other sports are held at maintenance. Separate from sport mode.
_Avoid_: Emphasis, block type

**Planned session**:
One workout the plan prescribes for a specific day.
_Avoid_: Workout, training (as a noun for one unit)

**Activity**:
One recorded, completed workout as it arrives from the activity source.
_Avoid_: Session (when it has been done), ride/run (as the generic term)

**Session review**:
The assessment of one activity, against its planned session where one exists.

**Day plan / Week plan / Month plan**:
The plan at three resolutions. A month plan sets the shape of its weeks, a week plan sets its days, a day plan holds that day's planned sessions.
_Avoid_: Schedule, program

**Plan update**:
A change to an existing plan in response to what actually happened or a change in the athlete's circumstances.

**Athlete profile**:
The standing facts about the athlete that every skill reads: zones, thresholds, availability, goals, limitations.

**Activity source**:
The system activities are read from. intervals.icu is the primary activity source; Garmin is the secondary one, consulted for data intervals.icu lacks.

**Calendar sync**:
Publishing approved planned sessions to intervals.icu: the whole upcoming week when it is approved, and single sessions after a plan update.

**Private training data**:
The athlete profile, athlete rules, plans and reviews. Kept outside the public skills repo.

**Data folder**:
The one place private training data lives, shared by every runtime the skills run in.

**Data index**:
The file in the data folder that tells a skill where each kind of private training data and each key file is.

**Daily check**:
The morning answer to "what is today's session and am I ready for it", ending in a readiness verdict.
_Avoid_: Morning briefing, readiness report

**Readiness verdict**:
The daily check's conclusion about today's planned session: go, modify or skip.

**Week review**:
The assessment of a finished week: what was done against what the week plan prescribed.

**Season plan**:
The athlete-maintained plan above the month plan: goals, phases and key dates for the season.

**Coaching rules**:
The general best-practice defaults every planning and review skill applies.

**Athlete rules**:
The athlete's own rules. They are private training data and override coaching rules where the two differ.

**Analysis layer**:
The athlete's private scripts that turn raw activity data into the figures a skill reasons about.

**Approval**:
The athlete's explicit acceptance of a draft plan or plan update. Nothing is published by calendar sync before it.

**Subjective log**:
The athlete's own scores for a day (effort, feel, soreness, pain, illness), kept in that day's day plan.
_Avoid_: Diary, wellness log

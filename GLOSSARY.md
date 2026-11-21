# Training Skills

Agent skills that coach a single athlete: reviewing completed training and planning what comes next.

## Language

**Athlete**:
The one person the skills coach.
_Avoid_: User, client

**Sport mode**:
Which sports a plan covers. Triathlon (swim, bike and run in one combined plan) is the default; a single-sport mode such as run-only is the alternative.

**Focus**:
The sport given priority inside a plan: it carries the progression and the hard sessions while the other sports are held at maintenance, which share one short hard set a week. Separate from sport mode.
_Avoid_: Emphasis, block type

**Planned session**:
One workout the plan prescribes for a specific day.
_Avoid_: Workout, training (as a noun for one unit)

**Key session**:
A planned session named in its week's row of the month plan.

**Hard session**:
A planned session or activity with enough fast work to count against the weekly cap; the figures are in the coaching rules. A hard swim is counted apart.

**Brick**:
A ride and a run planned back to back: two planned sessions that count once.

**Race priority**:
A, B or C on a target race. It sets what is planned before and after the race.

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
The standing facts about the athlete that every skill reads: goals, thresholds (kept as dated anchors), availability, limitations, equipment. Zones are read from intervals.icu, not kept here.

**Anchor**:
A dated, measured value in the athlete profile that targets are worked out from, such as a tested bike power, a run pace or a maximum heart rate.

**Out of date**:
Said of a planned session whose figures were worked out from an anchor value that a newer tested value has replaced, when the newer one gives other figures.

**Anchor note**:
The daily check's line about a session's anchors: that the session is out of date, or that its plan does not record them.

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
The plan above the month plans: the phases, and a week role for every week, counted back from the target races. Drafted by a skill and approved by the athlete. Goals and target races live in the athlete profile.

**Week role**:
What a week is for: load, easy, taper, race or recovery. The season plan sets it and the month plan carries it.
_Avoid_: Deload. An athlete may say "hard week" for a load week; a load week is not made of hard sessions.

**Coaching rules**:
The general best-practice defaults every planning and review skill applies.

**Athlete rules**:
The athlete's own rules. They are private training data and override coaching rules where the two differ.

**Analysis layer**:
The athlete's private scripts that turn raw activity data into the figures a skill reasons about.

**Approval**:
The athlete's explicit acceptance of something a skill proposes to write: a draft plan, a plan update, or a change to the athlete profile or athlete rules. Nothing is published by calendar sync before it.

**Subjective log**:
The athlete's own scores for a day (effort, feel, soreness, pain, illness), kept in that day's day plan.
_Avoid_: Diary, wellness log

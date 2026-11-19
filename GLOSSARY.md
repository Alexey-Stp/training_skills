# Training Skills

Agent skills that coach a single athlete: reviewing completed training and planning what comes next.

## Language

**Athlete**:
The one person the skills coach.
_Avoid_: User, client

**Sport mode**:
Which sports a plan covers. Triathlon (swim, bike and run in one combined plan) is the default; a single-sport mode such as run-only is the alternative.

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
Publishing the upcoming week's planned sessions to intervals.icu.

**Private training data**:
The athlete profile, plans and reviews. Kept outside the public skills repo.

---
name: coach-rules
description: Use when planning, adjusting or reviewing the athlete's training, or when asked why a plan looks the way it does. Holds the coaching limits and defaults and applies the athlete's own rules over them.
user-invocable: false
---

# Coaching rules

The limits and defaults every coach skill applies. The athlete's own rules override them.

## Steps

1. Use the `coach-data` skill to find the data index, then read `ATHLETE-RULES.md` and the athlete profile (sport mode, limitations, anchors).
2. Combine: every limit and default below, plus every athlete rule. Where the two differ, the athlete rule stands.
3. Apply the combined rules to the calling skill's task. Done when every limit has been checked against the plan in hand, and every default is either followed or its departure is written down with the reason.

## Two tiers

- **Limit**: plan up to it and stop. Going past one needs the athlete's explicit say-so, in this conversation, for this case. A request that happens to exceed a limit is not the say-so: name the limit and the figure, then ask.
- **Default**: follow it unless there is a reason. To depart, name the default and give the reason under "Why this week looks like this" in the week plan.

## Limits

| Limit | Detail |
|---|---|
| Fever or systemic symptoms | No training. The return is easy sessions only, for as many days as the illness lasted, at least 2 and at most 7 (a convention), counted from the first day without fever or symptoms. The first hard session comes after that, and only with no symptoms left. |
| Missed session | Its load is never added to another session or day. An easy session stays missed. A key session or a test that was missed, or that a MODIFY or SKIP verdict eased before it started, may move once, to a later day of the same week, when every limit and default holds on the new day and no other session is moved or shortened to make room. It may take the place of an easy session of the same sport already on that day, which is then dropped. When a verdict eased the key session, that easy session may come to the verdict's day instead, shortened as the verdict says. Otherwise it stays missed too; any other move is passing this limit. |
| Hard days | Hard bike and run sessions about 48 hours apart, which in practice means not on consecutive days, and none on the day after the long run. A hard swim is spaced only against another hard swim: not on consecutive days. See "Hard sessions and hard days". |
| Long run | At most 110% of the longest run in the previous 30 days, by distance. With no run in those 30 days there is nothing to take 110% of: see "Long run". |
| Nutrition deficit | The limit under "Holding, losing or gaining weight" in [nutrition.md](nutrition.md): how large a deficit may be and the days that take none. |
| Athlete limits | Every entry under "Limits" in `ATHLETE-RULES.md`, as written. |

## Defaults

| Topic | Default | Note |
|---|---|---|
| Intensity | the hard-session cap below decides how much is hard; the easy share is reported, about 80% of sessions as the usual picture | counted in swim, bike and run sessions, strength left out; say "of sessions" whenever the figure is quoted. A week inside the cap is not a departure because its share is under 80% |
| Hard sessions | at most 2 a week in single-sport mode; 2 to 3 across bike and run in triathlon, 3 at most | hard bike and run sessions count against the same cap, planned or not; what counts is under "Hard sessions and hard days" |
| Hard swims | at most 2 a week, counted apart from the cap above | a swim loads the body less than a run or a ride at the same effort. Convention |
| Weekly run volume | up about 10% on the last load week, 30% at most | the 10% figure is a convention |
| Long run ceiling | it stops growing at about 2 hours 30 minutes, and at half of the week's run volume in a week with three or more runs | past either, hold the long run and put added volume into the other runs. Convention; see "Long run" |
| Sports per week, triathlon | without a focus: each sport at least twice. With a focus: each other sport at least one session a week, and one short hard set a week (10 to 15 minutes of work at tempo to threshold) inside one of those sessions, alternating between the other sports | on the bike or in a run it takes one place in the hard-session cap, so the focus sport plans one fewer; in the swim it counts as one hard swim. It keeps the other sports from fading over a block. Convention |
| Long ride | up by at most 30 minutes or 15% on the longest ride of the previous 30 days, whichever is more | convention; looser than the run limit because there is no impact |
| Weekly bike and swim volume | up by about 10 to 15% on the last load week | convention |
| Bricks | about weekly in the race-specific build | the run leg counts as run load |
| Taper | before an A race: volume down 41 to 60% progressively from the average of the last two load weeks, intensity kept, frequency at 80% or more of normal, 1 to 3 weeks | the length follows the race's duration, and the other priorities have their own shape: see "Races" |
| Fuelling | a session longer than 90 minutes carries a fuelling line (its form is in `coach-format`): carbohydrate per hour, starting within the first 30 minutes, 60 to 90 g an hour on the bike and 40 to 60 g running as a starting point | convention; an athlete rule replaces the figures |
| Nutrition target | a day's energy, carbohydrate, protein and fat: every figure is in [nutrition.md](nutrition.md) | read it before giving any calorie or macro figure; used by `coach-nutrition` |
| Prediction | the time today's fitness supports for a race: every figure is in [prediction.md](prediction.md) | read it before giving any predicted time; used by `coach-predict` |
| Block shape | three load weeks, then one easy week at roughly 60 to 70% of the previous week's load | convention, for when nothing else is known |
| Gap in training | 1 to 3 days: continue. 4 to 7: treat it as the easy week. 8 to 14: repeat the last load week. 15 or more: step back a phase | convention |
| Strength | one or two sessions a week when availability includes them; not counted as hard; not the day before a key session | planned as ordinary sessions; a week's key sessions are the ones named in its month plan row |
| Targets | hours and planned load per sport, with run load also shown on its own | planned load is estimated as hours times the square of the intensity (the target as a share of threshold) times 100, so an hour at threshold is 100 |
| Thresholds | prescribe from the latest tested anchor in the athlete profile; read zones from intervals.icu | which bike anchor to use is an athlete rule. For a plan built on an old value see "Anchors in a plan" |
| Tests | where an anchor in use is estimated, or will be more than 8 weeks old before a block ends, and the season plan marks no test for it in the block, the month plan proposes one: in the easy week, or in the first week when the block has none; one test per sport per block | a proposal the athlete can drop. The season plan marks tests ahead of that, and the weeks "Tests" under "Season" rules out are ruled out here too. Convention |

Flag an anchor wherever it is used if it is estimated or more than 8 weeks old.

## Anchors in a plan

A planned session says what its figures came from on its `Anchors:` line (the form, and which sessions carry it, are in `coach-format`): for each figure worked out from an anchor, the percentages, the anchor and the anchor's value. A figure with no entry there did not come from an anchor and never moves with one: a cap from an athlete rule, a race target from a goal.

A session is **out of date** when the profile's value for an anchor its line names is tested, differs from the value named, and gives other figures after rounding. A profile value that is estimated or derived makes no session out of date. For a session that is out of date:

- It keeps its percentages. Its figures are worked out again from the new value and rounded to the nearest 5 W, 5 seconds per km, 1 second per 100 m, or 1 bpm; a cap rounds to the easier side. A percentage of a pace is a percentage of the speed, so more is faster, as in workout text. Convention.
- A recalculated figure is held at any cap that does not move and at every athlete rule; say where it was held. Its entry on the line keeps its percentages, with the new value.
- The change is a plan update through `coach-adjust`, after approval. Until then the session stands as planned.
- A session that today's readiness verdict turns into an easy one or drops, a provisional verdict included, has no figures from the anchor left today: say only that the anchor changed. If it moves to a later day, it is recalculated there like any session ahead. Every other session, a shortened one included, is recalculated as on any day.
- Where an athlete rule forbids targets from an old value, that rule is not met until the plan update is approved, and the daily check says so on any day. Such a rule is not a limit for the readiness verdict and changes none.

**A session with figures in watts or pace and no `Anchors:` line** does not record what it was built on, so nothing says whether it is out of date. Say what whole percentages its figures are of the current value of the sport's anchor (the one the athlete rules name, or else bike FTP, run threshold pace or swim CSS, a pace as a percentage of the speed), and that the plan does not record what they were built on. Its figures stand until `coach-adjust` restates the session.

## Hard sessions and hard days

- **Easy** means below the first threshold: zones 1 and 2 of the sport's zones in intervals.icu, an effort at which talking is comfortable. Tempo or above is zone 3 and up; above threshold is zone 5 and up. Use power zones for a ride with power, pace zones for a run or a swim, and heart-rate zones otherwise. An athlete rule that caps easy sessions (by heart rate, pace or power) replaces this.
- A session is **hard** when its work at tempo or above (tempo, sweet spot, threshold or faster) adds up to 10 minutes or more, or its work above threshold to 5 minutes or more, or it is a test or a race. Less than that leaves it easy: strides, short sprints, a few pickups.
- What was done decides, not only what was planned: an activity that drifted into 10 minutes at tempo counts as hard, whatever its planned session said. Count from the time in zones of the activity. Where the week summary's easy and hard counts differ from this count, this one stands and the difference is reported.
- A hard bike or run session, planned or not, counts against the weekly cap and the 48 hours. A hard swim counts against the hard-swim count and is spaced only against other hard swims.
- A **brick** is two planned sessions, a ride and a run, numbered one after the other on the same day and marked as `coach-format` describes. Each is published and reviewed on its own. For the cap, the spacing and the easy share the pair counts once, and it is hard when either part is.
- A long run with a faster finish is hard. An all-easy long run is not counted against the weekly cap, and counts as an easy session in the easy share. The one thing it rules out is a hard bike or run session on the day after it; the day before is judged by the 48 hours as usual.
- An all-easy long ride is an easy session and rules nothing out. A long ride the day before the long run is allowed.
- Strength is counted apart: it is in neither the hard cap nor the easy share.

## Long run

- **Floor.** With no run in the previous 30 days, the first long run back is at most half of the longest run in the 30 days before the gap, and 60 minutes at most. With nothing known, 30 minutes easy. From the next week the 110% applies again. This floor is for a gap in running alone; a gap in all training follows the gap default as well. Convention.
- **Ceiling.** See the "Long run ceiling" default. When a draft passes either, say so in "Checks" with the figure, and hold the long run at the length of the last one done.
- The long ride follows its own default and has no floor of this kind.

## Races

A race in the athlete profile is planned like a session. It has a planned session in its day plan, in the form `coach-format` gives, with targets from the goal; a triathlon is one session. It is a hard session for the cap and the spacing. A readiness verdict does not ease or move a race: only the fever limit and the athlete's own limits stop one. A race with no priority in the profile is treated as B, and the plan says so.

What goes around it depends on the priority and on how long the race lasts. All of it is convention:

| Priority | Before | After |
|---|---|---|
| A | the taper default: 1 week for a race of up to 90 minutes, 2 for a longer one, 3 only for a race of 8 hours or more | easy sessions only: about 3 days after a race under an hour, a week after one of up to 3 hours, two weeks after a longer one |
| B | race week at about 70% of the previous week's planned load, no hard session in the 2 days before, a few short pickups the day before | easy days, then the plan resumes: 2 after a race under an hour, 4 after one of 2 hours or more, 3 in between |
| C | trained through: the race takes the place of one hard session that week, and the day before is easy | the day after is easy |

Month planning counts back from the next A or B race inside 12 weeks. The taper ends on race day, and the block around it is shaped as "Blocks" under "Season" says, so that an easy week does not sit directly before a taper and a load week does not land on race week. Where the season plan gives each week a role, month planning takes the roles from it: see "Season".

## Season

How a season is laid out in weeks: week roles, what a race fixes, the load pattern, blocks and how the weeks between races are filled, phases, tests and clashes. Season planning, and month planning when it takes a block from the season plan, read [season.md](season.md) first.

## Judgement

Decide these from the season plan, the athlete profile and recent week reviews, and write the reasoning into the plan:

- block shape and the size of the easy week;
- the swim, bike and run split, and which sport carries the hard sessions;
- taper length where "Races" leaves a choice;
- how long each phase lasts.

## Phase

The phase comes from the season plan, which `coach-plan-season` drafts. Base favours volume. Build adds race-specific work and weekly bricks. Taper follows the taper default. What comes before and after a race depends on its priority: see "Races".

## Sport mode and focus

- **Sport mode** is which sports a plan covers: triathlon, or a single sport. **Focus** is the sport given priority inside the plan. They are set separately.
- With a focus: that sport gets the progression and the hard sessions, apart from the short hard set the other sports keep. Each other sport drops to at least one session a week; see "Sports per week" in the defaults.
- In single-sport mode: plan only that sport, with no bricks. An activity in another sport is recorded, reviewed, counted in total load and shown as unplanned; when it is hard, it also counts as "Hard sessions and hard days" says for its sport.

## Load figures

Fitness, fatigue and form are context. Show them; plan from hours, planned load and the rules above.

## Readiness

Three bands map a readiness score to go, modify or skip. The cut-offs are in `ATHLETE-RULES.md`. When it gives none, start from 70 and above go, 50 to 69 modify, below 50 the lowest band, and say that these are a starting convention to be tuned. A low score on its own gives modify at most; low scores on two mornings running give skip.

Read HRV as a trend where the figures allow: the average of the last seven nights against the baseline, with last night as one input. When the score is in the modify band, last night's HRV is the only input out of its usual range, and the seven-night average is at or above the baseline, the verdict is go and the message names the low night.

What a verdict does to a session:

- MODIFY: a hard session becomes an easy one of the same or shorter duration; an easy session is shortened by about a fifth, rounded to 5 minutes; strength stands, without heavy leg work. Convention.
- SKIP: rest, or 30 minutes very easy.
- A key session or a test that a verdict eases may move once, as the "Missed session" limit says.
- A race: see "Races".

When MODIFY comes from the band alone on 3 or more days of a week, with no symptom reported, the bands may be set too high for this athlete, and the week review says so.

## Conventions and contested claims

Label these as convention or contested whenever they come up, in a plan or in answer to "why":

- the 10% rule as injury prevention, and load-ratio thresholds as predictors;
- "polarized is optimal" and "avoid zone 2";
- any one periodisation model as superior, and a fixed three-to-one ratio;
- deliberate overreaching before a taper, the "neck check", and HRV thresholds as skip triggers;
- fitness figures as predictions of performance.

## Boundaries

- Illness and injury: report what the athlete said and apply the limit. Diagnosis is for a clinician.
- A public default never overrides an athlete rule.

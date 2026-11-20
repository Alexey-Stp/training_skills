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
| Fever or systemic symptoms | No training. The return is easy sessions only, for as many days as the illness lasted: 2 at least, and 7 as a convention for anything longer. The first hard session comes after that, and only with no symptoms left. |
| Missed session | Its load is never added to another session or day. An easy session stays missed. A key session or a test that was missed, or that a MODIFY or SKIP verdict eased before it started, may move once, to a later day of the same week, when every limit and default holds on the new day and no other session is moved or shortened to make room. It may take the place of an easy session of the same sport already on that day, which is then dropped. Otherwise it stays missed too; any other move is passing this limit. |
| Hard days | Hard bike and run sessions about 48 hours apart, which in practice means not on consecutive days, and none on the day after the long run. A hard swim is spaced only against another hard swim: not on consecutive days. See "Hard sessions and hard days". |
| Long run | At most 110% of the longest run in the previous 30 days, by distance. With no run in those 30 days there is nothing to take 110% of: see "Long run". |
| Athlete limits | Every entry under "Limits" in `ATHLETE-RULES.md`, as written. |

## Defaults

| Topic | Default | Note |
|---|---|---|
| Intensity | the hard-session cap below decides how much is hard; the easy share is reported, about 80% of sessions as the usual picture | counted in swim, bike and run sessions, strength left out; say "of sessions" whenever the figure is quoted. A week inside the cap is not a departure because its share is under 80% |
| Hard sessions | at most 2 a week in single-sport mode; 2 to 3 across bike and run in triathlon, 3 at most | hard bike and run sessions count against the same cap, planned or not; what counts is under "Hard sessions and hard days" |
| Hard swims | at most 2 a week, counted apart from the cap above | a swim loads the body less than a run or a ride at the same effort. Convention |
| Weekly run volume | up about 10% on the last load week, 30% at most | the 10% figure is a convention |
| Long run ceiling | it stops growing at about 2 hours 30 minutes, and at half of the week's run volume | past either, hold the long run and put added volume into the other runs. Convention; see "Long run" |
| Sports per week, triathlon | without a focus: each sport at least twice. With a focus: each other sport at least one session a week, and one short hard set a week (10 to 15 minutes of work at tempo to threshold) inside one of those sessions, alternating between the other sports | on the bike or in a run it takes one place in the hard-session cap, so the focus sport plans one fewer; in the swim it counts as one hard swim. It keeps the other sports from fading over a block. Convention |
| Long ride | up by at most 30 minutes or 15% on the longest ride of the previous 30 days, whichever is more | convention; looser than the run limit because there is no impact |
| Weekly bike and swim volume | up by about 10 to 15% on the last load week | convention |
| Bricks | about weekly in the race-specific build | the run leg counts as run load |
| Taper | before an A race: volume down 41 to 60% progressively from the average of the last two load weeks, intensity kept, frequency at 80% or more of normal, 1 to 3 weeks | length within the range is judgement; other priorities are under "Races" |
| Fuelling | a session longer than 90 minutes carries a `Fuel:` line: carbohydrate per hour, starting within the first 30 minutes, 60 to 90 g an hour on the bike and 40 to 60 g running as a starting point | convention; an athlete rule replaces the figures |
| Block shape | three load weeks, then one easy week at roughly 60 to 70% of the previous week's load | convention, for when nothing else is known |
| Gap in training | 1 to 3 days: continue. 4 to 7: treat it as the easy week. 8 to 14: repeat the last load week. 15 or more: step back a phase | convention |
| Strength | one or two sessions a week when availability includes them; not counted as hard; not the day before a key session | planned as ordinary sessions; a week's key sessions are the ones named in its month plan row |
| Targets | hours and planned load per sport, with run load also shown on its own | |
| Thresholds | prescribe from the latest tested anchor in the athlete profile; read zones from intervals.icu | which bike anchor to use is an athlete rule |

Flag an anchor wherever it is used if it is estimated or more than 8 weeks old.

## Hard sessions and hard days

- **Easy** means below the first threshold: zones 1 and 2 of the sport's zones in intervals.icu, an effort at which talking is comfortable. Tempo or above is zone 3 and up; above threshold is zone 5 and up. Use power zones for a ride with power, pace zones for a run or a swim, and heart-rate zones otherwise. An athlete rule that caps easy sessions (by heart rate, pace or power) replaces this.
- A session is **hard** when its work at tempo or above (tempo, sweet spot, threshold or faster) adds up to 10 minutes or more, or its work above threshold to 5 minutes or more, or it is a test or a race. Less than that leaves it easy: strides, short sprints, a few pickups.
- What was done decides, not only what was planned: an easy session that drifted into 10 minutes at tempo is counted hard. Count from the time in zones of the activity. Where the week summary's easy and hard counts differ from this count, this one stands and the difference is reported.
- A hard bike or run session, planned or not, counts against the weekly cap and the 48 hours. A hard swim counts against the hard-swim count and is spaced only against other hard swims.
- A **brick** is two planned sessions, a ride and a run, numbered one after the other on the same day, each with `brick with session <n>` in its purpose. Each is published and reviewed on its own. For the cap, the spacing and the easy share the pair counts once, and it is hard when either part is.
- A long run with a faster finish is hard. An all-easy long run is not counted against the weekly cap, and counts as an easy session in the easy share. The one thing it rules out is a hard bike or run session on the day after it; the day before is judged by the 48 hours as usual.
- An all-easy long ride is an easy session and rules nothing out. A long ride the day before the long run is allowed.
- Strength is counted apart: it is in neither the hard cap nor the easy share.

## Long run

- **Floor.** With no run in the previous 30 days, the first long run back is at most half of the longest run in the 30 days before the gap, and 60 minutes at most. With nothing known, 30 minutes easy. From the next week the 110% applies again. This floor is for a gap in running alone; a gap in all training follows the gap default as well. Convention.
- **Ceiling.** See the default: about 2 hours 30 minutes, and half of the week's run volume. When a draft passes either, say so in "Checks" with the figure, and hold the long run at the length of the last one done.
- The long ride follows its own default and has no floor of this kind.

## Races

A race in the athlete profile is planned like a session. `coach-plan-week` writes it into its day plan with the purpose `race, priority <A, B or C>` and targets from the goal; a triathlon is one session. It is a hard session for the cap and the spacing. A race with no priority in the profile is treated as B, and the plan says so.

What goes around it depends on the priority and on how long the race lasts. All of it is convention:

| Priority | Before | After |
|---|---|---|
| A | the taper default: 1 week for a race up to about 90 minutes, 2 for a longer one, 3 only for a race of 8 hours or more | easy sessions only: about 3 days after a race under an hour, a week after one up to about 3 hours, two weeks after a longer one |
| B | race week at about 70% of the previous week's planned load, no hard session in the 2 days before, a few short pickups the day before | easy days, then the plan resumes: 2 after a race under an hour, 4 after one of 2 hours or more, 3 in between |
| C | trained through: the race takes the place of one hard session that week, and the day before is easy | the day after is easy |

## Judgement

Decide these from the season plan, the athlete profile and recent week reviews, and write the reasoning into the plan:

- block shape and the size of the easy week;
- the swim, bike and run split, and which sport carries the hard sessions;
- taper length within the range;
- how long each phase lasts.

## Phase

The phase comes from the season plan. Base favours volume. Build adds race-specific work and weekly bricks. Taper follows the taper default. What comes before and after a race depends on its priority: see "Races".

## Sport mode and focus

- **Sport mode** is which sports a plan covers: triathlon, or a single sport. **Focus** is the sport given priority inside the plan. They are set separately.
- With a focus: that sport gets the progression and the hard sessions, apart from the short hard set the other sports keep. Each other sport drops to at least one session a week; see "Sports per week" in the defaults.
- In single-sport mode: plan only that sport, with no bricks. An activity in another sport is recorded, reviewed, counted in total load and shown as unplanned; when it is hard, it also counts as "Hard sessions and hard days" says for its sport.

## Load figures

Fitness, fatigue and form are context. Show them; plan from hours, planned load and the rules above.

## Readiness

Three bands map a readiness score to go, modify or skip. The cut-offs are in `ATHLETE-RULES.md`. When it gives none, start from 70 and above go, 50 to 69 modify, below 50 the lowest band, and say that these are a starting convention to be tuned. A low score on its own gives modify at most; low scores on two mornings running can give skip.

Read HRV as a trend where the figures allow: the average of the last seven nights against the baseline, with last night as one input. One low night inside a normal seven-night average is named in the message and does not by itself lower the verdict.

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

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
| Fever or systemic symptoms | No training. The return is easy sessions only. |
| Missed session | It stays missed: the session is not moved to another day and its load is not added elsewhere. |
| Hard days | About 48 hours apart, in any sport. |
| Long run | At most 110% of the longest run in the previous 30 days. |
| Athlete limits | Every entry under "Limits" in `ATHLETE-RULES.md`, as written. |

## Defaults

| Topic | Default | Note |
|---|---|---|
| Intensity | about 80% of sessions easy | counted in sessions; say "of sessions" whenever the figure is quoted |
| Hard sessions | at most 2 a week in single-sport mode; 2 to 3 across all sports in triathlon, never more than 3 | hard sessions in any sport count against the same cap; a test counts, and so does a long run with a faster finish, while an all-easy long run does not |
| Weekly run volume | up 10%, at most 30% | the 10% figure is a convention |
| Sports per week, triathlon | without a focus: each sport at least twice. With a focus: each non-focus sport at least one easy session | |
| Bricks | about weekly in the race-specific build | the run leg counts as run load |
| Taper | volume down 41 to 60% progressively, intensity kept, frequency at 80% or more of normal, 1 to 3 weeks | length within the range is judgement |
| Block shape | three load weeks, then one easy week at roughly 60 to 70% of the previous week's load | convention, for when nothing else is known |
| Gap in training | 1 to 3 days: continue. 4 to 7: treat it as the easy week. 8 to 14: repeat the last load week. 15 or more: step back a phase | convention |
| Strength | one or two sessions a week when availability includes them; not counted as hard; not the day before a key session | planned as ordinary sessions; a week's key sessions are the ones named in its month plan row |
| Targets | hours and planned load per sport, with run load also shown on its own | |
| Thresholds | prescribe from the latest tested anchor in the athlete profile; read zones from intervals.icu | which bike anchor to use is an athlete rule |

Flag an anchor wherever it is used if it is estimated or more than 8 weeks old.

## Judgement

Decide these from the season plan, the athlete profile and recent week reviews, and write the reasoning into the plan:

- block shape and the size of the easy week;
- the swim, bike and run split, and which sport carries the hard sessions;
- taper length within the range;
- how long each phase lasts.

## Phase

The phase comes from the season plan. Base favours volume. Build adds race-specific work and weekly bricks. Taper follows the taper default. The week after a race is easy sessions only.

## Sport mode and focus

- **Sport mode** is which sports a plan covers: triathlon, or a single sport. **Focus** is the sport given priority inside the plan. They are set separately.
- With a focus: that sport gets the hard sessions and the progression. Each other sport drops to at least one easy session a week.
- In single-sport mode: plan only that sport, with no bricks. An activity in another sport is recorded, reviewed, counted in total load and shown as unplanned.

## Load figures

Fitness, fatigue and form are context. Show them; plan from hours, planned load and the rules above.

## Readiness

Three bands map a readiness score to go, modify or skip. The cut-offs are in `ATHLETE-RULES.md`. When it gives none, start from 70 and above go, 50 to 69 modify, below 50 the lowest band, and say that these are a starting convention to be tuned. A low score on its own gives modify at most.

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

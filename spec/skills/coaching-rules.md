# Coaching rules (shared skill)

The skill's name is not decided; see the open points in the [README](../README.md).

## Purpose

Hold the general best-practice defaults every planning and review skill applies, and load the athlete's own rules, which override them.

## Triggers

Called by other skills only: `coach-today`, `coach-review-session`, `coach-review-week`, `coach-plan-week`, `coach-plan-month`, `coach-adjust`. Also the source for answering "why" questions in conversation.

## Reads

- `ATHLETE-RULES.md`, found through the data index.
- The athlete profile, for sport mode, limitations and anchors.

## Writes

Nothing.

## Steps

1. Load the rules below.
2. Load the athlete rules. Where the two differ, the athlete rule wins.
3. Hand the calling skill the combined rules, each marked as a limit or a default.

### Two tiers

From [coaching method][t11].

- **Limits** are never planned past without the athlete's explicit say-so.
- **Defaults** may be departed from, but the skill must name the default and give the reason in the week plan's reasoning.

### Limits

From [coaching method][t11] and [best-practice coaching][t5].

| Limit | Applies |
|---|---|
| Fever or systemic symptoms: no training. Return with easy sessions only. | every mode |
| Missed sessions are never made up. | every mode |
| No hard days back to back (about 48 hours apart). | every mode |
| No single run over 110% of the longest run in the previous 30 days. | every mode |

Plus every entry under "Limits" in the athlete rules.

### Defaults

From [coaching method][t11], [best-practice coaching][t5] and [sport mode][t12].

| Topic | Default | Note |
|---|---|---|
| Intensity | about 80% of sessions easy | counted in sessions; state the unit whenever it is quoted |
| Hard sessions | at most 2 a week in single-sport mode; 2 to 3 across all three sports in triathlon | hard sessions in any sport count against the same cap |
| Weekly run volume | up 10% by default, never more than 30% | the 10% figure is a convention |
| Triathlon | every sport at least twice a week | at least one easy session a week for each non-focus sport when a focus is set |
| Bricks | about weekly in the race-specific build | the run leg counts as run load |
| Taper | volume down 41 to 60% progressively, intensity kept, frequency at 80% or more of normal, 1 to 3 weeks | length within the range is judgement |
| Block shape | three load weeks, then one easy week at roughly 60 to 70% of the previous week's load | convention, used when nothing else is known |
| Gap in training | 1 to 3 days: continue; 4 to 7: treat as the easy week; 8 to 14: repeat the last load week; 15 or more: step back a phase | convention |
| Strength | one or two sessions a week when availability includes them; not counted as hard; not the day before a key session | planned as ordinary sessions |
| Targets | hours and planned load per sport; run load also tracked on its own | |
| Thresholds | prescribe from the athlete profile's anchors, with zones read from intervals.icu | which bike anchor is an athlete rule |

### Judgement

From [coaching method][t11].

Decided from the season plan, the athlete profile and recent week reviews, with the reasoning written into the plan:

- block shape and the size of the easy week;
- the swim, bike and run split, and which sport carries the hard sessions;
- taper length within the range;
- how long each phase lasts.

### Phase

The phase comes from the season plan. What shifts: base favours volume; build adds race-specific work and weekly bricks; taper follows the numbers above; the week after a race is easy-only.

### Sport mode and focus

From [sport mode][t12].

- Sport mode is which sports a plan covers: triathlon or a single sport. Focus is the sport given priority inside the plan.
- With a focus: that sport gets the hard sessions and the progression; the others drop to at least one easy session a week each.
- In single-sport mode: only that sport is planned; no bricks and no "every sport every week" rule.

### Load figures

From [coaching method][t11]. The load state (fitness, fatigue and form) is shown as context. It is never a target and never the sole reason for a plan update.

### Readiness

From [today skill][t20]. Three bands map a score to go, modify or skip; cut-offs come from the athlete rules. A low score alone gives at most modify.

### Not to be presented as fact

From [best-practice coaching][t5]. Keep these out, or label them as convention or contested:

- the 10% rule as injury prevention; load-ratio thresholds as predictors;
- "polarized is optimal" or "avoid zone 2";
- the superiority of any one periodisation model, or a fixed three-to-one ratio;
- deliberate overreaching before a taper; the "neck check"; HRV thresholds as skip triggers;
- fitness figures as predictions of performance.

## Reply shape

None. It answers the calling skill, not the athlete.

## Must never

- Diagnose illness or injury.
- Present a convention or a contested claim as evidence.
- Let a public default override an athlete rule.

## Source tickets

[Coaching method][t11], [best-practice coaching][t5], [sport mode][t12], [today skill][t20], [replace, absorb or coexist][t18], [skill list][t7].

[t5]: https://github.com/Alexey-Stp/training_skills/issues/5
[t7]: https://github.com/Alexey-Stp/training_skills/issues/7
[t11]: https://github.com/Alexey-Stp/training_skills/issues/11
[t12]: https://github.com/Alexey-Stp/training_skills/issues/12
[t18]: https://github.com/Alexey-Stp/training_skills/issues/18
[t20]: https://github.com/Alexey-Stp/training_skills/issues/20

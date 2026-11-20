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
| Missed session | Its load is never added to another session or day. An easy session stays missed. A key session or a test may move once, to a later day of the same week, when every limit and default holds on the new day and no other session is moved or shortened to make room. It may take the place of an easy session of the same sport already on that day, which is then dropped. Otherwise it stays missed too; any other move is passing this limit. |
| Hard days | About 48 hours apart in any sport, which in practice means not on consecutive days, and none on the day after the long run. See "Hard sessions and hard days". |
| Long run | At most 110% of the longest run in the previous 30 days. |
| Athlete limits | Every entry under "Limits" in `ATHLETE-RULES.md`, as written. |

## Defaults

| Topic | Default | Note |
|---|---|---|
| Intensity | the hard-session cap below decides how much is hard; the easy share is reported, about 80% of sessions as the usual picture | counted in swim, bike and run sessions, strength left out; say "of sessions" whenever the figure is quoted. A week inside the cap is not a departure because its share is under 80% |
| Hard sessions | at most 2 a week in single-sport mode; 2 to 3 across all sports in triathlon, 3 at most | hard sessions in any sport count against the same cap, planned or not; what counts is under "Hard sessions and hard days" |
| Weekly run volume | up 10%, at most 30% | the 10% figure is a convention |
| Sports per week, triathlon | without a focus: each sport at least twice. With a focus: each other sport at least one session a week, and one short hard set a week (10 to 15 minutes of work at tempo to threshold) inside one of those sessions, alternating between the other sports | the short hard set takes one place in the hard-session cap, so the focus sport plans one fewer; it keeps the other sports from fading over a block. Convention |
| Long ride | up by at most 30 minutes or 15% on the longest ride of the previous 30 days, whichever is more | convention; looser than the run limit because there is no impact |
| Weekly bike and swim volume | up by about 10 to 15% on the last load week | convention |
| Bricks | about weekly in the race-specific build | the run leg counts as run load |
| Taper | volume down 41 to 60% progressively, intensity kept, frequency at 80% or more of normal, 1 to 3 weeks | length within the range is judgement |
| Block shape | three load weeks, then one easy week at roughly 60 to 70% of the previous week's load | convention, for when nothing else is known |
| Gap in training | 1 to 3 days: continue. 4 to 7: treat it as the easy week. 8 to 14: repeat the last load week. 15 or more: step back a phase | convention |
| Strength | one or two sessions a week when availability includes them; not counted as hard; not the day before a key session | planned as ordinary sessions; a week's key sessions are the ones named in its month plan row |
| Targets | hours and planned load per sport, with run load also shown on its own | |
| Thresholds | prescribe from the latest tested anchor in the athlete profile; read zones from intervals.icu | which bike anchor to use is an athlete rule |

Flag an anchor wherever it is used if it is estimated or more than 8 weeks old.

## Hard sessions and hard days

- A session is **hard** when it holds sustained work at tempo or above (tempo, sweet spot, threshold or faster), a test or a race. Planned or unplanned, it counts against the weekly cap and the 48 hours.
- A few strides or short sprints inside an easy session, up to about 3 minutes of work in all, leave it easy.
- A long run with a faster finish is hard. An all-easy long run is not counted against the weekly cap, and counts as an easy session in the easy share. The one thing it rules out is a hard session on the day after it; the day before is judged by the 48 hours as usual.
- An all-easy long ride is an easy session and rules nothing out. A long ride the day before the long run is allowed.
- Strength is counted apart: it is in neither the hard cap nor the easy share.

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
- With a focus: that sport gets the progression and the hard sessions, apart from the short hard set the other sports keep. Each other sport drops to at least one session a week; see "Sports per week" in the defaults.
- In single-sport mode: plan only that sport, with no bricks. An activity in another sport is recorded, reviewed, counted in total load and shown as unplanned; when it is hard, it also counts against the hard-session cap and the 48 hours.

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

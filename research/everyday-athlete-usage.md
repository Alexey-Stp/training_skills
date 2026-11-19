# Everyday athlete usage: what an athlete asks a coach day to day

Research for ticket #4 (part of map #1). Researched 2026-11-19.

**Question.** What are the recurring day-to-day interactions between an athlete and a coach or coaching tool, how do existing AI coaching products and published agent skills structure them, and how often does each realistically occur?

**How to read this.** Three evidence grades are used throughout:

- **[S] Sourced**: stated in a first-party source that was read directly (repo file, vendor page, coach article). Links are given.
- **[W] Weakly sourced**: seen only through a search-result summary, a press release, marketing copy, or a single individual's practice.
- **[O] Opinion**: my inference. All frequency numbers in the ranked list are [O] unless marked otherwise; no source publishes usage counts per interaction. They are derived from the cadence each source attaches to an interaction ("each morning", "after every workout", "end of each week") and from a triathlete doing roughly 6 to 10 sessions a week.

## 1. Answer: ranked list of recurring interactions

Ranked by how often the athlete triggers it. "Times per year" assumes a year-round triathlete with 2 to 4 races.

| # | Interaction | Typical ask | Realistic frequency [O] | Input it needs | Output the athlete expects |
|---|---|---|---|---|---|
| 1 | **Daily session and readiness check** ("today" / "tomorrow") | "What's for tomorrow?", "What's on tap for today?", "Should I train today?" | Daily, 5 to 7 per week (about 300 per year) | The day's planned sessions; last night's wellness (sleep, HRV, resting HR); current load (fitness, fatigue, form); the last 1 to 3 days of training; optionally weather | One verdict first (go / modify / skip), then the session with targets and duration, and a contingency. Short enough for a phone. Never a question back |
| 2 | **Post-session review** | "Review my training", "How did my ride go?", "Did I hit my targets?" | Per key session, 3 to 6 per week; realistically asked for 2 to 4 and skipped for easy sessions | The completed activity (and intervals), the matching planned session, the athlete's RPE / feel / comment | Planned versus actual, whether the session served its purpose, one thing to change, and what is next |
| 3 | **Subjective log** | "RPE 7, left knee 3/10, slept badly" | Daily to per session, 4 to 7 per week, but usually folded into 1 or 2 rather than asked on its own | One free-text sentence | Confirmation of what was recorded and where. No analysis unless a flag trips |
| 4 | **Adjust the upcoming days** | "I missed a session", "I feel tired", "I'm travelling Thursday", "Can I swap Saturday and Sunday?" | 1 to 2 per week (50 to 100 per year) | The reason; the affected calendar window; adjacent hard sessions; recent load and wellness | An exact before / after of the changed days with a one-line rationale, a confirmation step, then the write. Missed work is not stacked onto the next day |
| 5 | **Weekly review and next-week plan** | "How was my week?", "Plan next week" | Once per week (about 50 per year). The single most consistently scheduled ritual | The week's activities against the plan; load change; wellness trend; a subjective week rating; next week's availability | Done / planned totals per sport, compliance, load trend, flags, then next week's sessions day by day, synced to the calendar |
| 6 | **Explain / ask "why"** | "Why VO2max intervals now?", "What's the difference between FTP and critical power?" | 1 to 3 per week, bursty | The decision or concept in question; the data that drove the decision | A short explanation that separates evidence, coaching convention and guess |
| 7 | **Status / progress check** | "Am I overreaching?", "How's my fitness trend?", "Am I on track for the race?" | Every 1 to 4 weeks (15 to 40 per year) | 4 to 6+ weeks of load, wellness trends, the goal and its date | A verdict against the goal, the dated evidence behind it, and the least restrictive corrective action |
| 8 | **Monthly / block review and next-block plan** | "How did the block go?", "Plan the next four weeks" | Every 3 to 4 weeks (12 to 15 per year) | The block's weeks, threshold changes, goal and phase, upcoming constraints | Block summary, what worked, next block's weekly structure and targets |
| 9 | **Threshold and zone update** | "Update my FTP", "My zones feel wrong" | Every 4 to 8 weeks (6 to 12 per year) | A test result or recent best efforts | New thresholds and zones, and which planned targets change |
| 10 | **Illness or injury** | "I'm sick", "My Achilles hurts" | 2 to 6 episodes per year, each spanning several days of follow-up | Symptoms, start date, affected sport | Rest or modified plan, a clear referral threshold, a return-to-training ramp, and a re-plan of the affected days |
| 11 | **Race preparation and race debrief** | "Race plan for Sunday", "How did my race go?" | Per race, 2 to 6 per year, clustered in race week and the week after | Race details and course, current fitness, tested fueling; afterwards the race file and the athlete's account | Taper and race-week sessions, pacing and fueling plan; afterwards plan versus actual and lessons carried forward |
| 12 | **Build or rebuild the plan** | "Get me a plan", "Build me a 12-week plan for a 70.3" | 1 to 3 per year for a full plan, plus a rebuild after any long interruption | Goal race and date, current thresholds, weekly availability, history, constraints | A phased plan (macro view first, then weeks), confirmed before it is written |
| 13 | **Setup and profile upkeep** | First run; "I changed jobs, I can only train mornings now" | Setup once; profile edits a few times per year | Stable private context: goals, constraints, health history, equipment, preferences | A profile the other interactions read. Edits shown and approved before saving |
| 14 | **Side topics**: fueling for a session, gear, strength | "How should I fuel a four-hour ride?" | Occasional, monthly or less | Session or race details | A specific recommendation |

### What the ranking implies

- **Three interactions carry almost all the volume**: the daily check (1), the post-session review (2) and the weekly review-plus-plan (5). They match the athlete's own three examples ("what's for tomorrow", "review my training", "get me a plan" at week resolution). Everything else is either occasional or a variation on them. [O]
- **"Get me a plan" hides three different frequencies**: next week (weekly), next block (monthly), whole plan (1 to 3 per year). Existing tools that expose a single `build` command take the horizon as an argument. [S, section 3]
- **"Review my training" hides three too**: one session, one week, one block or season. Tools split these more often than they split planning. [S, section 3]
- **"I missed a session" and "I feel tired" are the same interaction** in every tool that names it: adjust upcoming days for a stated reason. [S, section 3]
- **Tomorrow versus today.** Every tool surveyed names the daily command "today" and assumes a morning check. None has a "tomorrow" command. The closest is Section 11's post-workout report, which ends with a "Tomorrow" block listing every planned session. An evening-before lookup cannot use overnight wellness, so it is a plan read, not a readiness verdict. [S for the tools; O for the consequence]

## 2. Evidence: what coaches and platforms say athletes communicate

### Human coaching practice

- TrainingPeaks coach Jeff Lukich lists what the athlete should feed the coach: workouts uploaded "frequently" with post-workout comments; health metrics (weight, sleep, hydration); specific subjective feedback rather than "Felt great"; missed or shortened sessions; and race results "right away", with a debrief call after key events. Missed sessions for work or family can usually be passed over, but illness or a developing injury means the coach "will want to address that and change your schedule". [S] [Communicating With Your Coach Through TrainingPeaks](https://www.trainingpeaks.com/blog/the-importance-of-communicating-with-your-coach)
- Daniel Matheny asks for a brief comment and RPE after each session, written immediately: how it felt, what influenced it, what surprised the athlete, what to change. [S] [The Importance of Post-Workout Comments](https://www.trainingpeaks.com/coach-blog/the-importance-of-post-workout-comments/)
- Dr. Jesse Riley notes that real athletes vary: "Some are consistent with each workout, while others may not leave feedback for a week or more", and describes a monthly call or video check-in covering barriers and upcoming life stress. [S] [Coach-Athlete Communication and Seeing Beyond the Metrics](https://www.trainingpeaks.com/coach-blog/coach-athlete-communication-metrics/). This is the basis for ranking the subjective log high in ideal frequency but discounting it in practice.
- Commercial coaching tiers commonly sell exactly these cadences: plans delivered weekly or monthly, a set number of schedule adjustments per month (for example 1 on a low tier, 4 on a higher one), and a monthly or weekly call. [W] Search-result summaries of individual coach pricing pages and the TrainingPeaks Coach Match page; not an industry standard and not read page by page.
- I found no published guidance from a coaching body (USA Triathlon, British Triathlon, UK Coaching) that gives interaction frequencies. Not verified either way; see section 5.

### Adaptive-plan products

- **TrainerRoad.** Calendar annotations split into Training Adjustments (Time Off, Injury, Illness, Travel), which trigger a plan adaptation when they overlap scheduled workouts, and Notes, which do not. Skipping a workout also triggers an adaptation with no extra input, and gives the same result as annotating in advance. More than 14 consecutive days off is the stated point at which to consider re-testing. [S] [Calendar Annotations](https://support.trainerroad.com/hc/en-us/articles/4404676155035-Calendar-Annotations). The plan responds "every day" to schedule changes, and after a missed workout the system "analyzes your recent training performance". [S] [How plans adapt to interruptions and time off](https://www.trainerroad.com/blog/how-trainerroads-personalized-training-plans-adapt-to-interruptions-and-time-off/). A short survey after each workout feeds adaptation. [W] search summary of the Adaptive Training Overview article; the article itself did not load.
- **Athletica.** The AI coach "gives richer feedback after every workout, comparing what you did with what was planned", taking RPE, a feeling score, free-text comments and morning HRV / resting HR as input. [S] [Enhanced Session Feedback](https://athletica.ai/athleticas-ai-coach-just-got-smarter-introducing-enhanced-session-feedback/). Its published example questions are a direct sample of everyday asks: "Should I take a rest day?", "Am I overreaching?", "Did I hit my targets in yesterday's run?", "What changed in my training plan since I missed a session yesterday?", "How is my fitness trend this month?", "What's the difference between FTP and Critical Power?". [S] [Meet Your New 24/7 Training Partner](https://athletica.ai/blog/meet-your-new-24-7-training-partner-athletica-ai-coach)
- **Humango.** Through chat the athlete can "schedule a day off, increase or reduce the intensity of workouts, report an injury or sickness" and ask questions. [W] press release, 2023-12-05: [Endurance Sportswire](https://www.endurancesportswire.com/revolutionizing-athletic-training-humango-unveils-the-enhanced-hugo-with-chatgpt-integration/)
- **Garmin.** Daily Suggested Workouts are "recommended based on your previous activities", adjust to an upcoming race, and can be started or dismissed. [S] [Garmin manual: Daily Suggested Workouts](https://www8.garmin.com/manuals/webhelp/GUID-D3621248-CC5B-4F04-B004-6F6FD9FDFEB0/EN-US/GUID-AFECC098-0B34-4913-9944-66E8DAF64039.html). The Morning Report bundles sleep, HRV status, training readiness and the day's workout into one wake-up screen. [W] third-party reviews only.

**Pattern across products** [O]: each of them automates the same four moments, namely a daily "what now" with a readiness signal, feedback after each session, an adjustment when life intervenes, and a periodic look at the trend. The differences are in whether the athlete asks (chat) or the product pushes (notification).

## 3. Evidence: how existing AI coach tools split interactions into commands

Projects read directly on GitHub on 2026-11-19. Star counts are from that day and are small in most cases; treat adoption as unproven.

| Project | Shape | Commands or named workflows |
|---|---|---|
| [rlacombe/switchback-running](https://github.com/rlacombe/switchback-running) (11 stars; ultrarunning; intervals.icu) | 12 skills, one task each | `today`, `review`, `week`, `adjust`, `build`, `race`, `nutrition`, `check`, `archive`, `briefing`, `why`, `setup` |
| [mmornati/ai-running-coach](https://github.com/mmornati/ai-running-coach) (29 stars; trail running; Garmin / intervals.icu) | 5 agents plus 30 skills; a few short commands on top | `/today`, `/week`, `/why`, `/race`, `/log`, `/inspection`, `/shoes`, `/update-coach` |
| [CrankAddict/section-11](https://github.com/CrankAddict/section-11) (168 stars; cycling-led; intervals.icu) | One skill plus a protocol document; interactions are named report types | Pre-workout, post-workout, 7-day, 28-day, Season, Weather reports; plus daily and weekly unattended "heartbeat" checks |
| [chuazj/cycling-fitness-coach](https://github.com/chuazj/cycling-fitness-coach) (3 stars; intervals.icu) | One skill with a trigger-to-workflow dispatch table | Activity Analysis, Weekly Summary, Weekly Review, Create Plan, Mid-Week Check-In, Training Advice, Race Peaking, workout generation |
| [psca/coach](https://github.com/psca/coach) (0 stars; triathlon; intervals.icu) | One agent plus four prompt templates | `readiness-check`, `weekly-review`, `week-builder`, `session-designer` |
| [HenrikBrehm/triathlon-coach-skill](https://github.com/HenrikBrehm/triathlon-coach-skill) (2 stars; triathlon) | One skill, one eight-step workflow | A single report ending in a next-session and block recommendation |
| [ricardtg/endurance-coach-plugin](https://github.com/ricardtg/endurance-coach-plugin) (0 stars; running plus strength; Garmin) | Orchestrator skill plus plan-builder skills | Morning report, "done with my run / gym", weekly recap, race analysis; plan building delegated to separate skills |
| [maroffo/cadenza](https://github.com/maroffo/cadenza) (1 star; pre-MVP; intervals.icu; Telegram) | Service with scheduled jobs | Scheduled 09:00 morning check with a go / modify / skip verdict; free chat. Source files named `debrief` and `summary` suggest a post-session debrief and a summary, not read in detail |
| [hhopke/intervals-icu-mcp](https://github.com/hhopke/intervals-icu-mcp) (127 stars) and its ancestor [eddmann/intervals-icu-mcp](https://github.com/eddmann/intervals-icu-mcp) (40 stars) | MCP server: data tools plus prompt templates | `analyze-recent-training`, `activity-deep-dive`, `recovery-check`, `training-plan-review`, `plan-training-week`, `performance-analysis`, `generate_workout` |

### The same interaction under different names

| Interaction (section 1) | switchback | ai-running-coach | section-11 | cycling-fitness-coach | psca/coach | intervals-icu-mcp prompts |
|---|---|---|---|---|---|---|
| 1 Daily check | `today` | `/today` | Pre-workout report | Mid-Week Check-In; Training Advice ("should I train today") | `readiness-check` | `recovery-check` |
| 2 Post-session review | `review` | (session analysis skill) | Post-workout report | Activity Analysis | none | `activity-deep-dive` |
| 3 Subjective log | part of `review` | `/log` | none | none | typed into the readiness template | wellness update tool |
| 4 Adjust | `adjust` | (coach agent) | none named | part of Weekly Review | none | none |
| 5 Weekly review + plan | `week`, then `build next week` | `/week` (status only) | 7-day report | Weekly Summary / Weekly Review | `weekly-review`, `week-builder` | `training-plan-review`, `plan-training-week` |
| 6 Why | `why` | `/why` | "ask why" | rule: explain the why | built into every answer | none |
| 7 Status check | `check` | (dashboard) | 28-day report | Training Advice | none | `analyze-recent-training` |
| 8 Block review | `check` / `build` | none named | 28-day and Season reports | Create Plan | none | none |
| 11 Race | `race` | `/race` | none named | Race Peaking | none | none |
| 12 Build plan | `build` | (coach agent) | Training Plan Protocol | Create Plan | `week-builder` | `plan-training-week` |
| 13 Setup | `setup` | coach-setup | Setup assistant | setup reference | profile template | `verify_setup` |

Empty cells mean no dedicated command was found in the files read, not that the tool cannot do it in free chat.

### Design choices worth copying or avoiding

- **Convergent core vocabulary.** Two independently built suites landed on `today`, `week`, `why`, `race`; "review" and "build / plan" recur everywhere. [S]
- **Read-only daily commands, guarded writes.** ai-running-coach's `/today` and `/week` are declared thin wrappers that add "no new coaching logic", never write a plan file and never ask a question. switchback's `adjust` and `build` show an exact before / after and write only on explicit confirmation, then read the result back. [S] [`/today` source](https://github.com/mmornati/ai-running-coach/blob/main/config/gemini/commands/today.toml), [`adjust` source](https://github.com/rlacombe/switchback-running/blob/main/skills/adjust/SKILL.md)
- **Verdict first.** The daily output leads with go / modify / skip in section-11's pre-workout report, in cadenza (computed in code, not by the model) and in ai-running-coach ("one-line verdict first"). [S] [section-11 reports](https://github.com/CrankAddict/section-11/blob/main/examples/reports/README.md), [cadenza README](https://github.com/maroffo/cadenza/blob/main/README.md)
- **Weekly review and weekly planning are one ritual in two halves.** psca/coach says to run the review "at the end of each week (Sunday evening or Monday morning)" for "next-week planning guidance"; cycling-fitness-coach distinguishes a stats-only Weekly Summary from a Weekly Review that also updates plan state, and notes athletes use the same words for both. [S] [psca weekly-review](https://github.com/psca/coach/blob/main/prompts/analysis/weekly-review.md), [cycling-fitness-coach SKILL.md](https://github.com/chuazj/cycling-fitness-coach/blob/master/SKILL.md)
- **Review horizons are separate outputs.** section-11 has distinct post-workout, 7-day, 28-day and Season reports. [S]
- **A decision log makes "why" cheap.** ai-running-coach's `/why` reads a logged decision and "never invents a rationale absent from the log". [S] [`/why` source](https://github.com/mmornati/ai-running-coach/blob/main/config/gemini/commands/why.toml)
- **Push versus pull.** cadenza and section-11's heartbeat run the daily and weekly checks unattended; the skill suites wait to be asked. [S] [cadenza README](https://github.com/maroffo/cadenza/blob/main/README.md), [heartbeat template](https://github.com/CrankAddict/section-11/blob/main/examples/agentic/openclaw/HEARTBEAT_TEMPLATE.md)
- **One big skill versus many.** section-11, HenrikBrehm and cycling-fitness-coach keep one skill and dispatch internally; switchback gives each task its own skill and keeps shared rules in one separate document. [S] Which works better is not shown by any source. [O]
- **Illness and injury have no dedicated command anywhere.** They arrive through `adjust` or free chat and are handled by safety rules that override everything else (HenrikBrehm: no training recommendation with fever; cadenza: physio referral if pain has not improved by day 5 to 7). [S] [HenrikBrehm SKILL.md](https://github.com/HenrikBrehm/triathlon-coach-skill/blob/main/skills/triathlon-coach/SKILL.md), [cadenza system prompt](https://github.com/maroffo/cadenza/blob/main/docs/spec/coach-system-prompt-v1.md)

## 4. What this suggests for the skill list (opinion, for ticket #7)

All [O]. Not a decision.

- The interactions that would earn their own entry point by frequency are: next session (today / tomorrow), session review, week review plus next-week plan, adjust, and plan build (block and season). Status check, race, why and setup are real but rare; whether each is a skill or a mode of another is open.
- The subjective log has high ideal frequency and low real compliance; it is safer as a step inside the daily check and the session review than as a command the athlete must remember.
- A "tomorrow" lookup is the athlete's own phrasing and is missing from every surveyed tool. It should be a plain plan read, with the readiness verdict left to the morning.
- Month-resolution plan files (map #1) match the block review and block plan interaction (8), which most surveyed tools leave unnamed.

## 5. Not verified

- **Frequencies.** No source publishes how often athletes actually use each interaction. Every number in section 1 is an estimate from stated cadences.
- **Coaching bodies.** No guidance from USA Triathlon, British Triathlon or UK Coaching on athlete-coach contact frequency was found; I did not search their member-only material.
- **TrainerRoad post-workout survey** and **Garmin Morning Report** details come from search summaries and reviews, not first-party pages read in full. Garmin Coach's handling of missed workouts was found only in user forum posts and is not used above.
- **Humango** capabilities come from a 2023 press release, not current product documentation.
- **Coaching price tiers** come from search summaries of individual coaches' pages.
- **AI Endurance MCP server**: its listing page returned HTTP 403 and was not read.
- **intervals.icu** itself (the athlete's primary source) was not surveyed as a product; only third-party tools built on its API were.
- The GitHub projects were read at the README, skill and command level. I did not run any of them, and most have few stars, so "how existing tools split commands" describes their design, not proven usage.
- ai-running-coach's documentation is in French; command descriptions were read from the English `description` fields of its generated command files.

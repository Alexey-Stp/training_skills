# Garmin as secondary source: what it adds and how to reach it

Research for issue #3. Checked on 2026-11-19. Nothing here was tested against a real account: no login was made, so every statement about payload contents comes from documentation, published schemas or source code, not from observed responses.

Confidence labels: **[verified]** = read in a first-party source (Garmin, intervals.icu, or the project's own repository). **[reported]** = stated by an identifiable person on a forum or in a third-party README, not confirmed first-hand. **[unverified]** = could not be confirmed.

## Short answer

1. Garmin holds four groups of data that intervals.icu does not carry: Body Battery, sleep stages and other sleep detail, HRV context (status, baseline, 7-day average), and Garmin's own computed training metrics (Training Readiness, recovery time, Training Status, acute load, Training Effect, stamina).
2. Since 21 October 2026 there is an official, free route for one person: the **Garmin Connect Personal API**. A key is created in Garmin Connect settings, with no application or approval. It covers sleep, HRV, Body Battery, stress, daily summaries, VO2 max, activity lists and the original activity file. It does **not** cover Training Readiness, Training Status, recovery time or load.
3. Those remaining metrics are only reachable through unofficial libraries that sign in with the Garmin password (python-garminconnect and tools built on it), or by reading them off the watch or app by hand.
4. A second finding matters more to the map than the ticket asked: intervals.icu expects to stop returning Garmin-sourced activity data through its own API. That weakens the standing decision "intervals.icu is primary" for any athlete whose activities arrive via the Garmin sync. See [Risk to the primary source](#risk-to-the-primary-source).

## What intervals.icu carries from Garmin

### Wellness

The intervals.icu wellness record has these fields (API schema `Wellness`, 47 properties) **[verified]**:

`weight, restingHR, hrv, hrvSDNN, sleepSecs, sleepScore, sleepQuality, avgSleepingHR, spO2, respiration, steps, floorsClimbed, vo2max, readiness, stress, hydration, hydrationVolume, kcalConsumed, carbohydrates, protein, fatTotal, bodyFat, abdomen, systolic, diastolic, bloodGlucose, lactate, baevskySI, menstrualPhase, soreness, fatigue, mood, motivation, injury, comments` plus load fields (`ctl, atl, rampRate`).

Source: <https://intervals.icu/api/v1/docs> (OpenAPI document).

What that means for the Garmin items in the ticket:

| Garmin data | In intervals.icu? | Basis |
| --- | --- | --- |
| Sleep duration, sleep score | Yes, synced from Garmin. Score is also mapped to a 1-4 quality value. | **[verified]** developer post, 2022-03-12: <https://forum.intervals.icu/t/8778> |
| Sleep stages (deep, light, REM, awake) | No field exists. Garmin sends stage durations to intervals.icu (they appear in the developer's logs), but the wellness record has nowhere to keep them. | **[verified]** schema; log excerpt in <https://forum.intervals.icu/t/42348/2> |
| Sleeping HR, SpO2, respiration | Fields exist. Whether the Garmin sync fills them every night is **[unverified]**; a third-party tool claims the official sync does not deliver night SpO2, respiration or sleeping HR. | schema; **[reported]** <https://github.com/futureweb/garmin-intervals-bridge> |
| HRV | One overnight value (`hrv`, plus `hrvSDNN`). No HRV status, no baseline band, no 7-day average, no 5-minute high. | **[verified]** schema |
| Resting HR, steps, floors, weight, VO2 max | Yes. Floors was added 2026-10-05. | **[verified]** <https://forum.intervals.icu/t/132739> |
| Body Battery | No native field. The developer said in 2021 it is not supported and in 2023 that he could not get a usable number from Garmin's partner API. One user in 2024 reported seeing it on a chart; that is **[unverified]** and contradicts the schema. | **[verified]** <https://forum.intervals.icu/t/4179/5>, <https://forum.intervals.icu/t/36154/2>; schema |
| Training Readiness | No. `readiness` is a generic field filled by hand or by other apps. Garmin's partner API does not offer readiness. Users were still entering it by hand in 2024. | **[verified]** developer post 2022-06-17 <https://forum.intervals.icu/t/14534/4>; **[reported]** later state |
| Stress | A `stress` field exists but it is the athlete's subjective rating. Garmin's all-day stress score is not synced, as far as could be determined. | **[unverified]** |
| Training Status, recovery time, acute load, load focus | No. | **[verified]** absent from schema |

Sync reliability is uneven: there are 2026 bug reports of partial Garmin wellness sync (sleep score arriving, resting HR, HRV and steps missing) with no developer reply visible. **[reported]** <https://forum.intervals.icu/t/130093>

### Activities: swim detail and running dynamics

intervals.icu parses the activity file, so data recorded by the device does arrive **[verified, from the API schema]**:

- Swim: `lengths`, `pool_length`, `average_stride`, and per-interval data.
- Running dynamics: `average_stance_time` (ground contact time), `average_vertical_oscillation`, `average_vertical_ratio`, `average_step_length`, `average_stance_time_percent`, `average_stance_time_balance`, also per interval.

Per-length stroke type and SWOLF as named fields were not found in the schema. Whether they are available as streams or interval data is **[unverified]**.

What does not arrive is Garmin's computed, proprietary layer. Garmin removes undocumented messages and fields from the files it sends to partners:

- The intervals.icu developer, 2026-11-10: "the fit files Garmin gives us via their API are not exactly the same as the ones in the GDPR file". **[verified]** <https://forum.intervals.icu/t/133512/9>
- A statement attributed to Garmin says undocumented messages and fields are removed before files go to third-party platforms. **[reported]**, relayed by a forum user: <https://forums.garmin.com/developer/fit-sdk/f/discussion/432872/discrepancies-between-fit-files-from-garmin-connect-and-api-api-downgraded>
- Fields users report as stripped: VO2 max, recovery time, Training Effect, performance condition, stamina, sweat loss, lactate threshold. **[reported]** same thread and <https://github.com/futureweb/garmin-intervals-bridge>

So swim lengths and running dynamics are not a reason to reach for Garmin. Training Effect, recovery time and stamina are.

## Risk to the primary source

This was not asked in the ticket, but it changes what "secondary" has to cover.

- Garmin's partner agreement bars a partner from passing Garmin-sourced data on to other services. The intervals.icu developer was told on 2026-10-14 that this requirement is "not new". **[verified]** <https://forum.intervals.icu/t/609/829>
- Asked what the intervals.icu API would stop returning, the developer answered (2026-10-12, labelled as speculation): complete activities, FIT files, streams and wellness, "probably all of those", including history, for "anything that came in via the Garmin API". Data from other brands is unaffected. Files the athlete uploads are, in his understanding, unaffected. **[verified]** <https://forum.intervals.icu/t/609/816>
- 2026-10-22: Garmin activities in the intervals.icu API are "likely" to become stubs like Strava ones, hopefully keeping the Garmin activity ID so people can match against their own Garmin connection. **[verified]** <https://forum.intervals.icu/t/609/870>, <https://forum.intervals.icu/t/609/878>
- 2026-10-24: apps "need to get your own connection to Garmin to get activity data"; wellness and workout upload are undecided. **[verified]** <https://forum.intervals.icu/t/609/883>
- 2026-10-26: "none of this has been finalised yet". No later update was found as of 2026-11-18. No date is set. **[verified]** <https://forum.intervals.icu/t/609/890>
- Whether the restriction applies to an athlete reading their own data with their own intervals.icu API key, as opposed to a third-party app, was asked in the thread and not answered. **[unverified]**

Consequence: if the athlete's activities reach intervals.icu through the Garmin sync, an agent reading the intervals.icu API may soon get stubs for them. Two ways around it are discussed in that thread: read activity detail from Garmin directly (Personal API), or put activities into intervals.icu as the athlete's own uploads so they are not "Garmin API" data.

## Access routes for one individual

### 1. Garmin Connect Personal API (official)

All **[verified]** from Garmin unless marked.

- **What it is:** access to one's own Garmin Connect data, for "individual Garmin users who want programmatic access to their own data", "not intended for commercial applications serving multiple end users". <https://developer.garmin.com/gc-developer-program/personal/personal-faq/>
- **Launch:** 21 October 2026, as part of the relaunched developer program. <https://forum.intervals.icu/t/609/845>; Garmin's official client repository was created 2026-10-20.
- **Setup:** sign in to Garmin Connect web, open the Personal API Key page, create a key, accept the terms, choose an expiry of 30, 90, 180 days or one year. The key is shown once. Exchange it for an access token with one POST request; the token lasts 24 hours and there are no refresh tokens, so the tool asks again with the key. Garmin emails a reminder about a week before the key expires. <https://developer.garmin.com/gc-developer-program/personal/personal-api/>
- **Cost:** free. <https://forum.intervals.icu/t/609/845>
- **Delivery:** pull only, read only. <https://developer.garmin.com/gc-developer-program/overview/>
- **Official client:** `garmin/connect-personal-api-python` (Apache-2.0, Python 3.12+, a `gc-personal` command line that prints JSON). <https://github.com/garmin/connect-personal-api-python>

Endpoints in Garmin's published Swagger document (28 paths, read from the documentation page on 2026-11-19, <https://developer.garmin.com/gc-developer-program/personal/swagger-docs/>):

| Data | Endpoint | Range limit per request |
| --- | --- | --- |
| Sleep for one night (includes stage durations) | `/sleep-service/sleep/dailySleep` | one date |
| Sleep summaries | `/sleep-service/sleep/dailySleepSummariesByDate` | 31 days |
| HRV for one night: night average, 5-minute high, 7-day average, baseline, status | `/hrv-service/hrv/{date}` | one date |
| HRV summaries | `/hrv-service/hrv/daily/{from}/{to}` | not stated |
| Body Battery daily reports | `/wellness-service/wellness/bodyBattery/reports/daily` | 31 days |
| Stress, daily | `/usersummary-service/stats/stress/daily/...` | 28 days |
| Steps, daily | `/usersummary-service/stats/steps/daily/...` | 28 days |
| Daily summaries (resting HR and others) | `/usersummary-service/v2/dailysummaries` | 1 year |
| Heart rate through the day | `/wellness-service/wellness/dailyHeartRate` | one date |
| SpO2 | `/wellness-service/wellness/daily/spo2acclimation/{date}` | one date |
| VO2 max, daily | `/metrics-service/metrics/maxmet/daily/...` | not stated |
| Heart rate zones | `/biometric-service/heartRateZones/v2` | n/a |
| Weight, hydration, food logs, fitness age, menstrual cycle | various | 31 to 364 days |
| Activity search, activity summary, activity workouts, activity types | `/activitylist-service/...`, `/activity-service/activity/{id}` | paged |
| Activity file "in its original format" (ZIP) | `/download-service/files/activity/{id}` | one activity |

Not in the Swagger document: **Training Readiness, Training Status, recovery time, acute or chronic load, endurance score, hill score, race predictions, sleep skin temperature**. Confirmed by the absence of any such path or field name in the document, and by the python-garminconnect maintainer's assessment ("the data is very limited", about 35 data points against 300+). <https://github.com/cyberjunky/python-garminconnect/issues/476>

The activity summary schema does include swim fields (strokes, lengths, pool length, SWOLF), running dynamics (ground contact time, vertical oscillation, stride length) and Training Effect. **[verified]** as schema field names only; actual payloads not observed.

- **Original file:** a forum user reports the file downloaded with a personal key is identical to the manual download from Garmin Connect and contains all Garmin-specific fields. **[reported]** <https://forum.intervals.icu/t/609/863>. Garmin's Swagger text says "original format", which is consistent.
- **Rate limits:** none published. The Swagger document defines a 429 response. **[unverified]** what the limits are.
- **Terms:** the key terms are shown at key creation, behind login, so they were not read first-hand. As quoted by a forum user, the key "may be used only by you in connection with applications, services, or tools that you develop or operate for your own use" and may not be shared with a third party. **[reported]** <https://forum.intervals.icu/t/609/864>. A locally run agent skill reading the athlete's own data fits that wording; pasting the key into a hosted third-party service is the doubtful case. Whether the terms restrict passing the retrieved data to an AI model provider is **[unverified]**.
- **Reliability:** official and documented, but four weeks old. The landing page had placeholder text on launch day **[reported]** <https://forum.intervals.icu/t/609/849>, and the official client is still adding endpoints.
- **Maintenance cost:** renew the key at least once a year. No MFA, no password stored.

### 2. Garmin Connect Developer Program, business tiers (official)

- Starter: for "organizations building apps"; request form; Activity, Health, Training, Courses and Women's Health APIs; push only, no historical data, limited user capacity. Enterprise adds pull, history and support. **[verified]** <https://developer.garmin.com/gc-developer-program/overview/>
- Push delivery needs a publicly reachable server to receive data. It is aimed at multi-user products, and it is the route that delivers filtered files. Not a fit for one athlete now that the Personal API exists.
- The Training API (pushing planned workouts to the watch) is in the business tiers only, not in the Personal API. intervals.icu already pushes planned workouts to Garmin, so the skills do not need it.
- New applications were reportedly paused from May 2026 until the relaunch. **[reported]**, secondary press only.

### 3. Unofficial libraries (sign in with the Garmin password)

- **python-garminconnect** (`cyberjunky/python-garminconnect`): active, release 0.3.20 on 2026-10-23, Python 3.12+. Describes itself as "an unofficial client for Garmin's web services". Signs in with email and password (MFA prompt supported) using the mobile app's sign-in flow, then stores tokens in `~/.garminconnect/garmin_tokens.json`; its README warns the refresh token "can provide persistent account access". Covers everything in the app, including `get_training_readiness`, `get_training_status`, `get_body_battery`, `get_hrv_data`, `get_sleep_data`, and original-file download. Also has write methods that can change account data. **[verified]** <https://github.com/cyberjunky/python-garminconnect>
- **garth** (`matin/garth`): "deprecated and no longer maintained". Garmin changed its sign-in flow; "New logins will not work". Do not build on it. **[verified]** <https://github.com/matin/garth>
- **Reliability:** poor in 2026. From 17 March 2026 fresh logins returned HTTP 429 for many users worldwide for about seven weeks, with partial recovery in May and mixed reports after. Existing tokens often kept working; cloud and CI addresses were hit hardest. **[reported]** by many users in <https://github.com/matin/garth/issues/217>. A 429 on first sign-in was reported again in October 2026: <https://github.com/cyberjunky/python-garminconnect/issues/453>
- **Terms risk:** these use private, undocumented endpoints with the account password. A third-party README states that Garmin's Terms of Use prohibit automated access, that the consequence in the terms is account suspension, and that no such suspension is known for the long-standing open-source clients. **[reported]** <https://github.com/futureweb/garmin-intervals-bridge>. The Terms of Use text itself could not be retrieved, so the clause is **[unverified]**: <https://www.garmin.com/en-US/legal/terms-of-use/>. A library contributor expects Garmin may act more strictly now that an official route exists (opinion). <https://github.com/cyberjunky/python-garminconnect/issues/476>
- **Setup cost:** `pip install`, one interactive sign-in with MFA, then a token file to protect. Expect to repeat the sign-in when Garmin changes something.

### 4. Manual export from Garmin Connect

- **Per activity:** export the original file (FIT), or TCX, GPX, or a splits CSV, from the activity page. **Activities list:** an "Export CSV" button gives one summary row per activity for the rows loaded on screen. **[reported]** from Garmin forum users and third-party guides; Garmin's own help article returned an access error and was not read: <https://forums.garmin.com/apps-software/mobile-apps-web/f/garmin-connect-web/348626/what-s-the-easiest-way-to-export-the-activities-data-to-excel-in-a-tabular-way>
- This CSV is most likely the "table from Garmin" the athlete mentioned. It holds activity summaries only. It contains no sleep, HRV, Body Battery or readiness. **[reported]**
- **Full account export:** requested at Garmin's account data management page (sign-in required, so not read first-hand). Garmin emails a link to a ZIP holding original activity files and wellness data as JSON. Reported waiting time ranges from 48 hours to 30 days; it is all-or-nothing with no date filter. **[reported]** <https://takeoutday.org/guides/how-to-export-garmin-connect-data>
- **Cost and fit:** no setup, no terms risk, fully manual. Suitable for a one-time history backfill or occasional check, not for daily advice. Wellness has no manual CSV export other than report pages in Garmin Connect **[unverified]**.

### 5. MCP servers

MCP servers are wrappers around route 1 or route 3; they inherit that route's coverage, reliability and terms position.

- **On the Personal API:** many appeared within four weeks of launch, for example `Mason-Levyy/garmin-personal-mcp` (75 stars) and `indaco/garmin-personal-mcp` (42 stars), both read-only. All are new, single-author projects. None were code-reviewed for this research. **[verified]** that they exist and what they claim: <https://github.com/Mason-Levyy/garmin-personal-mcp>, <https://github.com/indaco/garmin-personal-mcp>
- **On python-garminconnect:** `Taxuspt/garmin_mcp` (about 1,500 stars), 155 tools including training readiness and status, with tool profiles to cut the list down; a one-time `garmin-mcp-auth` sign-in stores tokens it says last about six months; includes write tools. **[verified]** <https://github.com/Taxuspt/garmin_mcp>
- **garmin-intervals-bridge** (`futureweb/garmin-intervals-bridge`, MIT, 41 stars, first released October 2026): not an MCP server but relevant. It copies Garmin data into intervals.icu, using the Personal API key, the password sign-in, or both: original FIT files as the athlete's own uploads, and wellness values into native fields plus custom `Garmin...` fields. This would keep intervals.icu as the single place the skills read. It is a continuously running service by one author. **[verified]** that it exists and what it claims; behaviour not tested. <https://github.com/futureweb/garmin-intervals-bridge>

## Comparison

| Route | Covers readiness / status / recovery time | Covers sleep, HRV, Body Battery | Setup | Reliability | Terms risk |
| --- | --- | --- | --- | --- | --- |
| Personal API | No | Yes | Minutes; renew key yearly | Official; new, limits unpublished | None for own-use tools |
| Business API | No (not offered to partners) | Partly, filtered | Application plus a server | Official | None, but not meant for individuals |
| python-garminconnect | Yes | Yes | Sign-in with password and MFA; token file | Broke for weeks in 2026 | Private endpoints; account-level risk, unquantified |
| Manual export | Only by reading the app | Only via full account export | None | Stable | None |
| MCP server | Same as the route underneath | Same | Same plus MCP config | Same plus a young wrapper | Same |

## Implications for the spec

- Define "Garmin secondary data" as the Personal API set: sleep with stages, HRV with status and baseline, Body Battery, stress, resting HR. Reading it needs only the official client or plain HTTP calls with a key held outside the public repo.
- Treat Training Readiness, Training Status and recovery time as optional inputs. They need the unofficial route or manual entry. A sensible default is for the skills to work without them and accept them if the athlete supplies them (typed in, or written into intervals.icu's `readiness` field).
- Plan for intervals.icu returning stubs for Garmin-synced activities. The spec should say where activity detail comes from in that case: the Personal API activity endpoints and original file, or athlete-owned uploads into intervals.icu.
- Much of the wellness basics (sleep duration and score, one HRV value, resting HR, weight, VO2 max) is already in intervals.icu wellness, so a first version could read wellness from intervals.icu alone and add Garmin only for Body Battery, sleep stages and HRV status. This depends on the unresolved question of whether wellness stays readable through the intervals.icu API.

## Not verified

- Personal API rate limits, and actual response contents (schemas read, no calls made).
- The full Personal API key terms (behind login); only a forum quotation was seen. Whether they limit sending retrieved data to an AI provider.
- Garmin's Terms of Use clause on automated access (page text could not be retrieved).
- Whether Training Readiness can be reached through the Personal API by an undocumented path. The published document has none.
- Whether intervals.icu will block Garmin-sourced data for an athlete's own API key, whether wellness is included, and when. Not finalised as of the last developer post found (2026-10-26).
- Exactly which Garmin wellness values the intervals.icu sync fills today (night SpO2, respiration, sleeping HR, Garmin stress, Body Battery). Schema and forum evidence conflict in places.
- Garmin's own help pages for CSV export and account export (access error; details come from forum users and third-party guides).
- Whether intervals.icu exposes per-length stroke type and SWOLF.
- Which watch the athlete owns. HRV status, Training Readiness and running dynamics depend on the model.

# intervals.icu API: what can be read and written

Research for issue #2. Sources fetched 2026-11-19. No API call was made with credentials; everything below comes from the published OpenAPI spec and forum posts, so response shapes are as documented, not as observed.

Confidence labels: **[spec]** = the OpenAPI document; **[dev]** = forum post by the intervals.icu developer (`david`) or staff; **[community]** = forum post by someone else (lower trust); **UNVERIFIED** = not established from a primary source.

## Sources

| Tag | Source |
|---|---|
| S1 | OpenAPI spec, `https://intervals.icu/api/v1/docs` (OpenAPI 3.0.1, "Intervals.icu API v1.0.0"); rendered at `https://intervals.icu/api-docs.html` |
| S2 | Forum, david, "API access to Intervals.icu" (first post, last edited 2026-10-14): https://forum.intervals.icu/t/api-access-to-intervals-icu/609 |
| S3 | Forum, david, "Intervals.icu API Integration Cookbook" (last edited 2026-06-05): https://forum.intervals.icu/t/intervals-icu-api-integration-cookbook/80090 |
| S4 | Forum, david, "Uploading planned workouts to Intervals.icu": https://forum.intervals.icu/t/uploading-planned-workouts-to-intervals-icu/63624 |
| S5 | Forum, david, "Downloading planned workouts from the API": https://forum.intervals.icu/t/downloading-planned-workouts-from-the-api/93737 |
| S6 | Forum, david, "Upload planned workouts to Garmin Connect" (posts #1, #140, #181): https://forum.intervals.icu/t/upload-planned-workouts-to-garmin-connect/1521 |
| S7 | Forum, david, "API access" thread posts #752-#883 (Oct 2026, Garmin terms): https://forum.intervals.icu/t/api-access-to-intervals-icu/609/752 |
| S8 | Forum, david, "Intervals.icu API Terms and Conditions" (effective 2025-10-23): https://forum.intervals.icu/t/intervals-icu-api-terms-and-conditions/114087 |
| S9 | Forum, "Workout Builder Syntax Quick Guide" (R2Tom, forum guide, closed reference topic): https://forum.intervals.icu/t/workout-builder-syntax-quick-guide/123701 |
| S10 | Forum, "Events created via API with workout_doc ..." (2026-09): https://forum.intervals.icu/t/132326 |
| S11 | Forum, "Swim Workout pace values in min/km rather than min/100m" (david #7, #9; eva #22): https://forum.intervals.icu/t/44319 |
| S12 | Forum, david, "Planned Walk transfers to Garmin as Custom / Workout" #2: https://forum.intervals.icu/t/54574 |
| S13 | Forum, "Bug: pool swim rest steps exported to Garmin as distance": https://forum.intervals.icu/t/132897 |
| S14 | Forum, "Possible bug on latitude/longitude STREAM" (david #2, app4g #3 quoting the data-model docs): https://forum.intervals.icu/t/32420 |

## Headline

1. Reading and writing everything the spec needs is supported with a personal API key: activities, intervals, streams, wellness, fitness/fatigue, zones, and calendar events with structured workouts.
2. **Risk, live as of Oct 2026:** the developer expects to have to block Garmin-sourced data in the API (activities, streams, FIT files, wellness, including historical), returning stubs as is already done for Strava. No date is set and nothing is final. This directly affects the standing decision "intervals.icu is the primary activity source" if the athlete's activities arrive via the Garmin Connect link. See "Garmin data restriction" below.
3. Planned workouts written through the API reach a Garmin device via intervals.icu's own Garmin Connect link (a settings toggle, not an API call), limited to the next 7 days. Bike and run are solid; pool-swim structured workouts have open, acknowledged bugs.

## Authentication for one athlete

- Personal use: HTTP Basic auth, username the literal string `API_KEY`, password the API key generated under "Developer Settings" near the bottom of `/settings`. [S1 securitySchemes, S2]
- OAuth + bearer token is for apps "intended to be used by more than one person"; not needed here. [S2] OAuth scopes mentioned in the guides: `ACTIVITY:READ/WRITE`, `WELLNESS:READ/WRITE`, `CALENDAR:READ/WRITE`, `SETTINGS`. [S3, S4, S5, S1] Scopes do not apply to API-key calls (UNVERIFIED that an API key has full access to every endpoint; implied by S2/S3 examples).
- Athlete id `0` in any path means "the athlete this key belongs to", so no athlete id has to be stored. [S2, S3]
- The key grants full access to the account's data; it can be cleared or regenerated in settings. [S2]
- `external_id` upsert/delete on events is matched only against events created by the same OAuth application [S1, S4], so with an API key use the event `id`, or `uid` with `upsertOnUid` (UNVERIFIED whether `external_id` upsert works at all for API-key callers).
- Terms: API use implies agreeing to the API Terms and Conditions; any lawful use is licensed, Garmin-derived data shown in an application needs Garmin attribution. [S8]

## Limits

All from S2 (developer's post):

- API-key callers: **5000 requests/day** (resets midnight UTC) and **2500 per rolling 15 minutes**.
- Additionally 10 calls/second per IP (no headers returned for this one).
- Headers on every response: `X-RateLimit-Limit: <15m>,<daily>` and `X-RateLimit-Remaining: <15m>,<daily>`. Over-limit gives HTTP 429 with `Retry-After` seconds.
- Cloudflare may challenge or block some client libraries' default user agents (e.g. Python-urllib); set a browser-like User-Agent.
- **Strava-sourced activities are not available** through the API: list/get return "an empty stub object". [S1, S2] Activity webhooks likewise. So the athlete's activities must reach intervals.icu from a non-Strava source.

## Reading

Base URL `https://intervals.icu`. All from S1 unless noted.

### Activities

- `GET /api/v1/athlete/{id}/activities?oldest=&newest=` (oldest required; local ISO-8601 date or datetime; `limit`, `fields` optional; descending date). Also `activities.csv`, `/activities/search`, `/activities/{ids}`.
- `GET /api/v1/activity/{id}` (`intervals=true` to include intervals); `GET /api/v1/activity/{id}/intervals`.
- Files: `/activity/{id}/file` (original, gzip), `/activity/{id}/fit-file` (intervals.icu-generated), `/gpx-file`. [S1, S3]
- The `fields` query parameter trims responses and drops nulls on most list endpoints, useful for keeping agent context small.
- Activity summary fields (subset of ~180 in the `Activity` schema):
  - Common: `id`, `start_date_local`, `type`, `name`, `moving_time`, `elapsed_time`, `distance`, `average_speed`, `average_heartrate`, `max_heartrate`, `calories`, `icu_training_load`, `icu_intensity`, `trimp`, `icu_rpe`, `feel`, `session_rpe`, `source`, `paired_event_id` (link to the planned workout), `compliance`, `icu_atl`, `icu_ctl` (fitness/fatigue at that activity), `icu_hr_zone_times`, `decoupling`, `polarization_index`, `interval_summary`, `stream_types`.
  - Bike: `icu_average_watts`, `icu_weighted_avg_watts`, `icu_ftp`, `icu_joules`, `icu_variability_index`, `icu_efficiency_factor`, `icu_power_hr`, `average_cadence`, `icu_zone_times` (power), `icu_rolling_ftp`, `icu_pm_ftp` (eFTP modelling), `trainer`, `power_load`.
  - Run: `pace`, `gap`, `threshold_pace`, `pace_zone_times`, `gap_zone_times`, `average_cadence`, `average_stride`, running dynamics (`average_stance_time`, `average_vertical_oscillation`, `average_vertical_ratio`, ...), `total_elevation_gain`, `pace_load`.
  - Swim: `pool_length`, `lengths`, `pace`, `pace_zone_times`, `pace_load_type` (`SWIM`/`RUN`), `pace_load`. Activity `type` distinguishes `Swim` and `OpenWaterSwim`. Per-length or stroke-level detail (stroke type, SWOLF) is not in the schema: UNVERIFIED / probably absent.
- `source` enum: `STRAVA, UPLOAD, MANUAL, GARMIN_CONNECT, OAUTH_CLIENT, DROPBOX, POLAR, SUUNTO, COROS, WAHOO, ZWIFT, ZEPP, CONCEPT2, HUAWEI`, which tells the skills how each activity arrived.
- Interval fields (`Interval` schema): `type` (`WORK`/`RECOVERY`), `label`, `moving_time`, `distance`, `average_watts`, `weighted_average_watts`, `average_heartrate`, `average_speed`, `gap`, `average_cadence`, `zone`, `intensity`, `training_load`, `decoupling`, and more.
- Derived per-activity endpoints: power/pace/HR curves, histograms, `best-efforts`, `time-at-hr`, `power-vs-hr`, `hr-load-model`, `weather-summary`, `segments`, `map`.
- Athlete-level curves: `/athlete/{id}/power-curves`, `/pace-curves`, `/hr-curves`, `/power-hr-curve`, `/mmp-model`.

### Streams

- `GET /api/v1/activity/{id}/streams{ext}` with `types=` (comma list) and `includeDefaults`; `.csv` for CSV. Returns `ActivityStream` objects: `type`, `name`, `data`, `data2` (longitude for `latlng` [S14]), `anomalies`.
- Quirk: the endpoint returns `fixed_watts` as `watts`; if `raw_watts` is requested or `types` is omitted the original `watts` is renamed `raw_watts`.
- Stream type names are not enumerated in the spec. The data-model docs, as quoted in S14 by a community member (2023), list: `time, watts, cadence, heartrate, distance, altitude, latlng, velocity_smooth, moving, grade_smooth, temp, torque, fixed_watts, fixed_heartrate, raw_watts, raw_heartrate, left_right_balance, smo2, thb, smo2_2, thb_2, dfa_a1, epoc, hrv, ga_velocity, fixed_altitude, corrupt_time, core_temperature, skin_temperature, stride_length, w_bal, respiration, watts_alt, watts_alt_acc`. Treat as indicative; each activity's own `stream_types` field is the authoritative list of what it has. Which streams a pool swim carries is UNVERIFIED.

### Wellness, fitness and fatigue

- `GET /api/v1/athlete/{id}/wellness?oldest=&newest=` (also `.csv`), `GET /api/v1/athlete/{id}/wellness/{date}`. One record per local day, `id` = ISO date.
- Fitness/fatigue live on the wellness record: `ctl` (fitness), `atl` (fatigue), `rampRate`, `ctlLoad`, `atlLoad`, plus `sportInfo[]` with per-sport `eftp`, `wPrime`, `pMax`. Form (ctl minus atl) is not a field in the schema, so compute it (UNVERIFIED that no endpoint returns it directly).
- Recovery signals on the same record: `restingHR`, `hrv` (rMSSD), `hrvSDNN`, `sleepSecs`, `sleepScore`, `sleepQuality`, `avgSleepingHR`, `readiness`, `spO2`, `respiration`, `weight`, `bodyFat`, `vo2max`, `steps`, and subjective scales `soreness`, `fatigue`, `stress`, `mood`, `motivation`, `injury`, `hydration`, plus `comments`. Which are populated depends on the athlete's connected devices and manual entry (UNVERIFIED for this athlete). Scale ranges for the subjective integers are not in the spec.
- Wellness is writable too: `PUT /athlete/{id}/wellness/{date}` and `PUT /athlete/{id}/wellness-bulk` (only supplied fields change; metric units). [S1, S3]
- Planned and completed load: events and activities both carry `icu_training_load`, `icu_atl`, `icu_ctl`, so future calendar events give projected fitness/fatigue. `GET /athlete/{id}/fitness-model-events` lists events that alter the model. `GET /athlete/{id}/athlete-summary` gives summary data for a date range (response detail not examined).

### Zones and thresholds

- `GET /api/v1/athlete/{athleteId}/sport-settings` (list) or `/sport-settings/{id}` where id may be an activity type such as `Run` or `Ride`. `GET /api/v1/athlete/{id}` returns the athlete with `sportSettings` included.
- Per settings group (`types[]` says which sports it covers): `ftp`, `indoor_ftp`, `w_prime`, `p_max`, `power_zones`, `power_zone_names`, `sweet_spot_min/max`, `lthr`, `max_hr`, `hr_zones`, `hr_zone_names`, `hr_load_type`, `threshold_pace` (metres/second per S5's `WorkoutDoc` comment), `pace_units` (`SECS_100M, SECS_100Y, MINS_KM, MINS_MILE, SECS_500M, ...`), `pace_zones`, `pace_zone_names`, `pace_load_type`, `load_order`, `warmup_time`, `cooldown_time`.
- Units of the zone arrays (percent of threshold vs absolute) are not stated in the spec: UNVERIFIED; confirm on first real read.
- Each activity also snapshots the zones in force at the time (`icu_power_zones`, `icu_hr_zones`, `pace_zones`, `icu_ftp`, `lthr`, `threshold_pace`).
- Settings are writable (`PUT` on the same paths), so a skill could update FTP/threshold pace. The `SPORT_SETTINGS_UPDATED` webhook exists but webhooks belong to OAuth apps. [S3]

### Calendar (planned side)

- `GET /api/v1/athlete/{id}/events?oldest=&newest=&category=WORKOUT` (defaults: today, plus 6 days). Options: `resolve=true` converts %-based targets to watts/bpm/m/s; `ext=zwo|mrc|erg|fit` attaches a converted file; `fields`. [S1, S5]
- Each planned workout carries `description` (the native text) and `workout_doc` (parsed steps: `duration`, `distance`, `reps`, `power`/`hr`/`pace`/`cadence` values with `units`, `warmup`, `cooldown`, `ramp`, nested `steps`). [S5]

## Writing planned workouts

### Endpoints [S1, S4]

- `POST /api/v1/athlete/{id}/events` creates one event; `POST /api/v1/athlete/{id}/events/bulk` creates many (`upsert=true` matches on `external_id`, OAuth apps only; `upsertOnUid` matches on `uid`).
- `PUT /api/v1/athlete/{id}/events/{eventId}` updates; `DELETE .../events/{eventId}` deletes; `PUT .../events/bulk-delete` deletes by id list; `DELETE /athlete/{id}/events?oldest=&newest=&category=` deletes a date range by category.
- Body is an `EventEx`. Fields that matter: `category` (`WORKOUT, RACE_A, RACE_B, RACE_C, NOTE, PLAN, HOLIDAY, SICK, INJURED, TARGET, ...`), `start_date_local` (`YYYY-MM-DDTHH:MM:SS`), `type` (sport: `Ride`, `Run`, `Swim`, `OpenWaterSwim`, `VirtualRide`, `TrailRun`, `WeightTraining`, ...), `name`, `description`, `moving_time`, `distance`, `icu_training_load`, `indoor`, `target` (`AUTO, POWER, HR, PACE`), `tags`, `color`, `external_id`.
- So races, notes, sick/injured days and weekly targets (`category=TARGET` with `load_target`, `time_target`, `distance_target`) can be written as well as workouts.
- `POST /athlete/{id}/events/{eventId}/mark-done` creates a manual activity matching a planned workout.
- A workout library also exists (`/athlete/{id}/workouts`, `/folders`, plans), separate from the calendar; not needed for syncing a week.

### Structured workouts

- Supported input forms: native intervals.icu workout text in `description`, or a `zwo`/`mrc`/`erg`/`fit` file via `file_contents` / `file_contents_base64` + `filename`. [S1, S4]
- **Use the `description` text.** Sending a `workout_doc` JSON directly is not the supported contract: a 2026 report showed such events exporting with zero steps on one path, and the forum helper's answer was "You should use the description field." [S10, community + forum staff helper; the developer did not post in that thread]
- Text syntax (S9, a community-maintained guide; the developer's own reference is the long "Workout builder" thread https://forum.intervals.icu/t/workout-builder/1163, not read in full):
  - One step per line starting with `-`: `- [duration or distance] [target] [cadence]`, text before the duration becomes the on-device cue.
  - Time `10m`, `30s`, `1h2m30s`; distance `500mtr`, `2km`, `1mi`. `m` is minutes; metres must be `mtr`.
  - Power: `75%`, `95-105%`, `220w`, `Z2`. HR: `70% HR`, `95% LTHR`, `Z2 HR`. Pace: `78-82% Pace`, `Z2 Pace`, `5:00/km Pace`, `2:00/100m Pace`.
  - Ramps `10m ramp 50%-75%`; repeats as a `5x` line (or `Main Set 5x` header) with a blank line before and after; nested repeats not supported.
- Pace targets require the athlete's threshold pace to be set for that sport, otherwise the exported step has no target (and no load is computed). Check sport settings before syncing. [S10]

### Reaching a Garmin device

- Mechanism: the athlete links Garmin Connect in intervals.icu `/settings` and ticks "Upload planned workouts"; intervals.icu then pushes planned workouts to Garmin Connect and they appear on the device at its next sync. Filters there choose which workouts (indoor/outdoor, sport). Changes on the intervals.icu calendar are re-pushed automatically. [S6 #1, #178] There is no API endpoint that triggers or confirms the push; the `Event.push_errors` field exists in the schema [S1] and may report failures (UNVERIFIED).
- **Only the next 7 days** of planned workouts are uploaded "to Garmin (and other integrations)". [S6 #140, #181] This matches the plan to sync only the upcoming week.
- Events created through the API appear to be pushed like UI-created ones (S10 reports API-created events arriving on a watch), but no developer statement says so explicitly: UNVERIFIED, test with one workout.
- Garmin's workout API has only these sports: `RUNNING, CYCLING, LAP_SWIMMING, STRENGTH_TRAINING, CARDIO_TRAINING, GENERIC, YOGA, PILATES`. [S12] So open-water swim has no structured-workout target on Garmin (a 2024 community report shows it arriving as a generic workout: https://forum.intervals.icu/t/71394).
- `powerRange`, `hrRange`, `paceRange` parameters and the "Garmin box in /settings" define how fixed targets are widened into ranges for devices. [S1]
- Swim caveats, all open as of Nov 2026:
  - Pool-swim pace targets show on the watch as min/km instead of min/100m; reported since 2023, a 2023 fix attempt was reverted, staff confirmed in Aug 2026 it is in the backlog. [S11]
  - Timed rest steps in pool workouts are exported as distance (1 s = 1 m), inflating total distance. [S13, community report 2026-10, no developer reply seen]
  - Community workaround: write swim sets as repeat blocks with the instruction in quoted cue text and `intensity=rest` rests, relying on text rather than pace targets. [S11 #14, community]
- Run caveat: a 2026 report of pace-range steps arriving as notes was answered by a forum helper as invalid workout syntax, which suggests syntax errors degrade silently into plain text. Validate by reading the event back and checking `workout_doc.steps`. [https://forum.intervals.icu/t/130465]
- Whether workout upload to Garmin is affected by the new Garmin terms: the developer said on 2026-10-24 "Not sure what is going to happen with wellness data and uploading workouts yet." [S7 #883]

## Garmin data restriction (Oct 2026, unresolved)

Timeline from the developer's posts [S2, S7]:

- 2026-10-09: Garmin's developer terms changed; "It is likely that we will have to block access to Garmin data via the API soon."
- 2026-10-12 (explicitly speculative): the restriction would probably cover whole Garmin-origin activities, fields, FIT files, streams and wellness; "This will likely apply to historical data, anything that came in via the Garmin API"; it "only applies to data received from the Garmin API", so manually uploaded FIT files are "likely ok"; data from Suunto, COROS, Polar, Oura etc. stays accessible; no timeline.
- 2026-10-14: the terms are tied to the reopening of the Garmin Connect Developer Program; "there will be an easier path for individuals and apps to access data from Garmin devices."
- 2026-10-21: the new Garmin program went live; "All Garmin Connect users can now access a free personal API key directly from Garmin Connect."
- 2026-10-22: asked whether Garmin data in the intervals.icu API will become like Strava's (no details), "Unfortunately that is likely to be the case. We hope to be able to return a stub with the Garmin ID"; Garmin will help with ID matching.
- 2026-10-24: apps using intervals.icu as a bridge "need to get your own connection to Garmin to get activity data".
- As of the last post read (2026-10-24) no cut-off date had been announced and it was not stated whether the block already applies, nor whether personal API-key use is treated differently from OAuth apps (on 2026-10-09 the developer said personal use was part of the discussion). UNVERIFIED on both points.

Consequences for the spec:

- Aggregates computed by intervals.icu (training load, `ctl`/`atl`, zone times) for Garmin-origin activities: whether they stay readable is unanswered (raised by a community member, no reply).
- Options to keep intervals.icu as the readable primary source if the block lands: get activity files into intervals.icu by a route other than its Garmin API link (file upload via `POST /athlete/{id}/activities`, which the developer considers likely unaffected), or read Garmin-origin detail directly from Garmin with the new personal API key. Both are for a later ticket to decide.
- Re-check the thread before the spec is finalised: https://forum.intervals.icu/t/api-access-to-intervals-icu/609

## Not verified

- Anything about live behaviour: no request was made with credentials.
- Whether an API key can call every endpoint, and whether `external_id` upsert works without an OAuth app.
- Units of `power_zones` / `hr_zones` / `pace_zones` arrays; scale ranges of subjective wellness fields.
- Which streams and which wellness fields this athlete's data actually contains; swim per-length detail.
- That API-created events are pushed to Garmin exactly like UI-created ones, and what `push_errors` contains.
- The final shape and date of the Garmin data restriction, and its effect on wellness and on workout upload.
- The workout text syntax beyond the community quick guide (the developer's full "Workout builder" thread was not read).

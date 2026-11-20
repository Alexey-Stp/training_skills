# When intervals.icu returns an empty stub

intervals.icu may stop serving the detail of Garmin-recorded activities. It stays the primary activity source; these steps apply only to an activity that actually comes back empty.

## Steps

1. Tell the calling skill and the athlete that the activity is an empty stub. A session review waits until real data is in hand.
2. **First fallback.** Get the original activity file from Garmin and upload it to intervals.icu as the athlete's own file. Load, fitness figures and pairing with the planned session then keep working. This upload is the one write this skill makes to intervals.icu besides the optional rename.
3. **Second fallback.** If the upload is not possible, ask the analysis layer's "analysis of one activity" command to work from the Garmin file directly.
4. **Wellness.** If sleep, HRV or resting heart rate stop arriving in intervals.icu, read them from Garmin.

Done when the activity has real figures, or the athlete has been told plainly that none could be obtained.

## Garmin

- Route: the official Garmin Connect Personal API key. It is read-only and lasts up to a year, then has to be replaced.
- It serves sleep with stages, HRV with status and baseline, Body Battery, stress, and the original activity file.
- It has no Training Readiness or Training Status figure, which is why `device_readiness` is optional.
- Already in intervals.icu through the Garmin sync: sleep duration and score, one overnight HRV value, resting heart rate, weight.

## Left unsolved

If planned sessions stop reaching the watch, the day plan still holds the session. Tell the athlete to load it by hand.

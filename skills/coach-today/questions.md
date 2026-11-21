# Questions after the daily check

Part of `coach-today`. Read when the athlete asks about a verdict that was already logged today, asks for today's session again, or asks about a target.

## Asked about the verdict

When the athlete asks why, questions the verdict, or asks for today's session again after a verdict was logged:

1. **Refresh and compare.** Refresh, then compare the inputs with the ones logged.
2. **Explain it, when asked why.** Asked only for today's session again, give the logged verdict and the session once more. Asked why: give the score, the band it fell in, and the rule or safeguard that decided, with the figures, and what that rule does to the session. Where the band alone decided, say so.
3. **The verdict stands** unless one of these two holds:
   - **Something new.** A symptom, a pain score, an activity, or an input that arrived or changed at its source since the verdict was logged and before the session started. Name it, run the steps of the daily check again and give the new verdict. A good feeling is logged under "How I felt" and is not something new.
   - **A mistake in applying the rules.** The wrong band (the bands as they stood when the verdict was logged), a safeguard or the HRV trend rule left out, a duration more than 10 minutes from what the MODIFY rule gives, a key session with no move offered. Say what was wrong, give what the rules give, and log it as a correction.
   Whether the rule itself suits the athlete is neither: that view changes no verdict.
4. **Log a new or corrected verdict** as `coach-format` says for a later verdict. With neither, write nothing but what the athlete said about how they feel.
5. **End with where things stand:** the verdict; what the day plan holds for the session now, where a change approved today stands over the verdict's duration; and, unless a fever, a return day after illness or an athlete limit decided, that training as planned is the athlete's own decision. A change to the plan goes through `coach-adjust`.

Three cases:

- **"Should I do it anyway":** the answer is the verdict, then step 5 of this list.
- **Another message disagrees:** the verdict logged in the day plan is the one in force.
- **Asked to move a band:** the bands are the athlete's rules, and `coach-setup` changes them after approval: offer it in one line. Today's logged verdict is unchanged.

With nothing new and no mistake, say that nothing new has arrived.

Done when the athlete has the answer, and the day plan holds a later verdict only if something new or a mistake was named.

## Asked about a target

When the athlete asks what a target is, how it was worked out, or whether they may go above or below it:

1. **Answer whole, in one message:**
   - the target and caps as the day plan holds them;
   - from the session's `Anchors:` line: the percentages, the anchor and the value it names;
   - the profile's value for that anchor now, with its test date;
   - whether the session is out of date, as "Anchors in a plan" in `coach-rules` defines it.
2. **Out of date:** give, in that same message, what those rules give for the session, and offer `coach-adjust`.
3. **No `Anchors:` line:** say what "Anchors in a plan" in `coach-rules` gives for such a session, and offer `coach-adjust`, which restates it.
4. **Above or below the range:** the target and the caps stand as the day plan holds them. Say that in one line; for a session that is out of date, add that the recalculated figures apply once the plan update is approved.
5. **A retest the profile does not hold** ("I tested again, it is higher"): offer `coach-setup` to record it. Until it is recorded the figures stand.

Being asked again ("are you sure?") is not a reason to give another figure: give the same figures in one line. A figure given earlier that is not what the day plan or these rules give is corrected once, and named as a correction; where the logged anchor note was wrong, it is rewritten. A follow-up question gets what it asks, not the whole answer again.

Done when the athlete has the whole answer in one message and the day plan holds the same figures as before.

# The Raw-Value Ratchet — SCAFFOLD (Layer B2)

> A guard that **only ever tightens.** Copy the pattern where you need to drive a bad pattern to zero and keep it there. Optional — adopt it for a specific value you're trying to eliminate, not preemptively.

## The idea

Some rules are "no new violations, and the old ones shrink over time." A raw-value ratchet enforces exactly that with a test or lint rule plus an **allowlist that may only get shorter, never longer**:

- A check fails if a forbidden pattern appears anywhere **except** files on the allowlist.
- New code therefore *cannot* introduce the pattern — it's not on the allowlist, so the check catches it.
- The allowlist is the finite list of pre-existing offenders. Every time one is cleaned up, it's removed. **Adding a file to the allowlist is forbidden** — that's the ratchet: it turns only one way.

The result: the bad pattern trends monotonically to zero, and the day the allowlist is empty you can delete it and the check becomes absolute.

## When to use it

- Migrating off a raw value toward a token/wrapper (e.g. raw colors → semantic tokens; raw strings → typed constants).
- Forbidding a character/API/import that escaped into the codebase and you want gone.
- Any "we agreed to stop doing X; enforce that new code doesn't, while we clean up the old."

## What to fill

```
Forbidden pattern:  <<the regex / rule — the thing that must not appear in new code>>
Allowlist:          <<the finite list of pre-existing files still containing it>>
Check:              <<a test or lint rule that fails on the pattern outside the allowlist>>
The one law:        the allowlist only SHRINKS. A PR that adds a file to it is wrong
                    on its face — fix the code instead.
```

## Its own trap

A ratchet only catches what its pattern describes. `<<SLOT: note any blind spot — e.g. a color ratchet that inspects class names cannot see an inline style value. Record the blind spot so nobody assumes the ratchet is total.>>`

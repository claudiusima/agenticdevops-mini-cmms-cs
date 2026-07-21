# <<PROJECT_NAME>> — Bug Log  *(TEMPLATE)*

> Active and fixed bugs, **plus the traps log.** Consult before touching any previously-buggy area — patterns that caused a bug once tend to recur.

## Bug entries

Each bug gets an entry **before** its fix task runs; flip it to Fixed only **after** verification.

**Entry format:**
```
### <<BUG_ID>> — <<one-line symptom>>   [Active | Fixed <<date>>]

**Reported:** <<how it surfaced>>
**Root cause:** <<the actual cause, once known — not the symptom>>
**Fix:** <<what changed; link the spec/task>>
**Trap (if any):** <<pointer to a TRAP-NNN below if this bug revealed a reusable trap>>
```

## Active

`<<SLOT: open bugs.>>`

## Fixed

`<<SLOT: resolved bugs, newest first.>>`

## Traps

A **trap** is a failure mode that will fool a future agent — most often the "**green everywhere, broken where nobody looks**" kind, where the type-checker, linter, tests, and build all pass but the thing is still wrong. The traps log is where these are recorded once, canonically, so a close-out entry can *point* to a trap instead of restating it.

The convention for writing a trap (id, the "why every guard misses it" line, the tell) is in `layer-b2/traps-log.scaffold.md`; filled examples are in `layer-b1-example/traps-log.example.md`. Keep the traps themselves here in this doc.

`<<SLOT: TRAP-NNN entries.>>`

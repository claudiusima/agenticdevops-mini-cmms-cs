# Traps Log — SCAFFOLD (Layer B2)

> How to record a **trap**: a failure mode that will fool a future agent. Copy this convention into your bug log's Traps section. For filled examples, see `layer-b1-example/traps-log.example.md`.

## What a trap is

The signature to watch for is **"green everywhere, broken where nobody looks."** The type-checker passes, the linter passes, the tests pass, the build passes — and the thing is still wrong, because none of those guards exercises the place it breaks. A trap is that gap, written down, so the next person doesn't fall in.

Traps are distinct from bugs. A bug is "this specific thing broke." A trap is "here is a *class* of thing that looks fine to every automated check and isn't — here's how to actually catch it." Every good trap ends with a **tell**: the concrete way to detect the problem that the standard guards miss.

## Entry format

```
### TRAP-<<NNN>> — <<one-line description of the deceptive failure>>

<<What happened / what the thing looks like.>>

**Why every guard misses it.** <<Walk the chain: typecheck → ? lint → ? tests → ?
build → ? — and name where the failure actually surfaces (usually: only when the
real artifact runs, in production, where nobody was looking).>>

**The tell.** <<The concrete check that DOES catch it — the thing to actually do
or read, since the automated guards won't. This is the payload.>>
```

## The meta-lesson these encode

Automated guards don't catch everything, and a green check is not proof. The traps log is the institutional memory of *where green lies*. The strongest single trap most projects hit early: **a grep that returns nothing is evidence about the grep, not about the code — validate the grep before trusting its silence.**

`<<SLOT: your project's traps go in the bug log; this scaffold is the how-to. Start the log empty and add a trap each time a "green everywhere" failure teaches you one.>>`

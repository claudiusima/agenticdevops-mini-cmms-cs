# Traps Log — Acme Notes (WORKED EXAMPLE, read-only)

> Layer B1: filled examples of the `traps-log.scaffold.md` convention, from the fictional worked-example product **Acme Notes**' bug log. Read for shape. A few are shown complete to demonstrate the "green everywhere, broken where nobody looks" payload; the rest by headline.

### TRAP-008 — A runtime dependency whose `require` survives the test runner but NOT the bundler: green everywhere, dead at app launch

A main-process module imported fine under the test runner and compiled fine, but was dropped/misresolved by the production bundler.

**Why every guard misses it.** Typecheck → 0. Lint → clean. Tests → green, because the test runner resolves from `node_modules` and **never loads the bundle**. Build → passes. The failure surfaces only when the app actually *loads the bundled main entry* — and nothing in the standard verification chain does that.

**The tell.** Launch the packaged/bundled app and watch it load, or add a smoke check that imports the bundled entry. A dependency's presence in `node_modules` is not proof it survives bundling.

### TRAP-007 — A required field added to a persisted-record schema after first ship makes existing rows silently vanish

A new **required** field was added to a persisted-record validation schema after real rows already existed without it. On load, those rows failed validation and were filtered out — users' data disappeared from the UI with no error.

**Why every guard misses it.** The schema, the code, and the tests are all internally consistent — tests use fixtures that *have* the new field. Only pre-existing rows written before the change lack it, and no test fixture models "a row from the old schema."

**The tell.** New fields on persisted-record schemas are **optional** (or ship with a migration/default). A same-schema test fixture cannot catch this; you need a fixture written against the *old* shape.

### TRAP-005 — A grep that finds nothing is not evidence of absence until the grep itself is validated

Empty grep output was read as "the pattern isn't in the code" and drove a wrong conclusion — when the real cause was the grep: a computed/mixed-case identifier the literal pattern couldn't match, a case-sensitivity miss, or a file not actually on the search path.

**Why every guard misses it.** Nothing is broken in the tooling; the grep ran fine and returned zero. Zero is just ambiguous — it means "no match for *this* query," not "not present."

**The tell.** Before trusting an empty grep, prove the grep works by matching a string you *know* is there. Only then does silence mean absence. (This one generalizes to every project — it's the strongest early trap to internalize.)

### TRAP-006 — The remote HTTP layer lies about success in three different ways

A third-party API's HTTP layer produced silent false successes: an `ok` status, a downloaded byte stream, and an id string were each individually untrustworthy as proof the operation actually worked.

**The tell.** Verify the *effect*, not the transport-level acknowledgement. (Full entry in the source bug log.)

### TRAP-004 · TRAP-003 · TRAP-002 (headlines)

- **TRAP-004** — `git reset --hard` destroyed uncommitted work (recovered). An *operational* trap: a destructive git command with no undo. The tell: never `reset --hard` with uncommitted changes present.
- **TRAP-003** — a hardcoded transport value that reads like a placeholder is actually **load-bearing security**. The tell: don't "clean up" a suspicious-looking constant without checking what depends on it.
- **TRAP-002** — an ungated tool-definitions list came to contain a tool that should be gated. The tell: when a registry is ungated, adding a gated item to it silently un-gates it.

---

*Meta-lesson, stated in the live log: automated guards don't catch everything — human reading is the real gate. Every trap here is a place where typecheck/lint/test/build were all green and something was still wrong.*

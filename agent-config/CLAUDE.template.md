# CLAUDE.md — TEMPLATE (coding-agent invariants)

> Copy to `CLAUDE.md` at the repo root, fill the slots, delete this banner. **Keep it minimal — invariants only.** Task-specific detail belongs in the per-task spec, not here; a fat CLAUDE.md rots the same way an over-broad rule does. This file exists so specs stop re-teaching the constitution every time.

## Non-negotiable

- **Never read, write, delete, or reset any user data file.** `<<SLOT: name the user-data boundary — e.g. "user notebooks are .db files at any path the user chose; only test-fixtures/ .db files may be touched.">>` The only data files you may touch are the test fixtures under `<<TEST_FIXTURES_DIR>>`.
- **Read the task spec named in the command, in full, before writing any code.**
- **Build with `<<BUILD_CMD>>` when done.**

## Architecture invariants (enforce in every change)

The hard constraints live in `<<ARCHITECTURE_FACTS_DOC>>` — read them and treat them as binding. The ones you will break most easily if you forget:

`<<SLOT: the 3–6 most easily-violated invariants, one line each. E.g. "No business logic in the <<presentation layer>>." / "<<the sync-DB / no-async>> discipline." / "<<canonical storage format>> only — never <<the tempting-but-wrong formats>>." / "typed end-to-end at the <<module boundary>> — never bypass the typed wrapper." Keep these SHORT; the full rationale is in the architecture-facts doc.>>`

## Traps that bite the coding agent specifically

- **A grep that finds nothing is not evidence of absence until the grep itself is validated.** `<<SLOT: your project's version — e.g. computed identifiers invisible to literal grep, case-sensitivity, a file not on the path.>>`
- `<<SLOT: any "green everywhere, broken where nobody looks" trap that only surfaces when the real artifact runs — see the traps log. Name the tell.>>`

## What stays out of this file

Per-task constraints, file lists, and acceptance criteria — those are in the spec. Standing rules the PM enforces (close-out, contract-sync) — those are the PM's job, not yours. Your job is: implement the spec, honor the invariants above, build clean.

# Skills — decision (adopt none)

> A **recorded decision**, not a file you install. Its whole value is stopping a future you (or a keen newcomer) from adding skills because they exist.

## Decision: no agent adopts the skills mechanism. Deliver the value through the mechanism that fits each role.

A skill (a `SKILL.md` an agent auto-loads when a matching task appears) beats a plain rule or checklist in **exactly one** situation: the procedure is **sometimes-relevant**, so pulling it in only when needed is worth more than keeping it always in view. This pipeline mostly doesn't have that shape:

- **PM procedures (spec, verify, close-out) run on *every* task, not sometimes.** Auto-loading buys nothing; they're already always-on in the project instructions. The one real failure here was *drift* (a close-out step forgotten), fixed by a rule + a checklist — not a missing mechanism. → **always-on checklists** (`checklists/`).
- **The coding agent is the only surface skills could ever fit** — its tasks vary by area, which is the sometimes-relevant shape. But today each spec already carries its area's constraints and the invariants live in `CLAUDE.md`. A per-area skill would duplicate what the spec already carries. → **`CLAUDE.md` now.**
- **The review agent doesn't use skills at all** — it gets `.cursor/rules/`.

## Why this also protects the template

Skills only work on surfaces that support the mechanism. Betting a **portable, cross-project** template on them makes it *less* portable, not more. Checklists and rules travel everywhere.

## Adopt-if trigger

`<<ADOPT-IF: the coding agent's work areas keep growing AND you notice specs routinely forgetting area constraints. Then per-area coding-agent skills that auto-load by task type become the right tool — build the one or two that pull their weight, not a skill for every area. Revisit then; don't build blind now.>>`

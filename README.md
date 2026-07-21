# Agentic-DevOps Workflow Template

A reusable, language-agnostic template for running a **human + PM-agent + coding-agent + review-agent** software project with the discipline that keeps living documentation true and stops silent regressions. Extracted and generalized from a real, running project's working loop.

**What this is for.** You are starting a new software project and want this loop from day one instead of rediscovering it. Copy this folder, work through **[`SETUP.md`](SETUP.md)** — the clean repo-to-first-sprint runbook — fill the slots, and you have a governing instruction set, a living-doc system, agent config, and a CI/verify discipline already wired together.

> **Start here → [`SETUP.md`](SETUP.md).** It is the linear setup runbook. `INSTANTIATE.md` is the deeper per-layer detail behind those steps. (Workshop teaching material lives in `teaching/` — temporary; delete it after the workshop, keep everything else as your template.)

**What this is NOT.** Not a code framework, not a language or stack choice, not a CI vendor lock-in. It governs *how humans and agents collaborate and how the docs stay honest* — the parts that were expensive to learn and are identical across stacks.

---

## The one idea

Every recommendation this template inherits passed a single conservative bar: **it must beat a plain prose rule concretely, or it doesn't go in.** Everything here exists because *not* having it caused a real, recorded failure on the source project — a doc that drifted for a month, a false safety promise that sat live for five weeks, a CI saga that cost five human round-trips. If a slot doesn't map to a failure you can imagine hitting, leave it empty; an unfilled slot is cheaper than a wrong one.

---

## The three layers

The template is deliberately split so that the generic machinery and the project-specific facts never tangle.

**Layer A — the workflow (fully generic, language-agnostic).** Roles and the loop, the numbered rules, the Tier-1/Tier-2 living-doc system, the spec format, the coding-agent command format, the atomic close-out, and the CI / verify-by-reading discipline. Nothing here mentions any stack. This is the bulk of the value and it drops into any project unchanged.

**Layer B2 — the architecture-rule capture scaffold (generic structure, empty slots).** The *pattern* for capturing and enforcing a project's hard technical constraints: a "Key Architecture Facts" section that specs must enforce, the contract-docs-move-in-the-same-commit rule, an "authority docs by area" index, a traps log, and a raw-value ratchet. B2 is shape without content — you fill the slots with your project's actual constraints.

**Layer B1 — a filled-in worked example.** The same B2 scaffold, populated with the constraints of a fictional worked-example app (**Acme Notes** — a local-first desktop notebook). B1 is not meant to be used — it is meant to be *read* so you can see what a filled B2 looks like before you fill your own.

The reason for the A / B2 / B1 split: Layer A is copy-and-go; B2 is copy-and-fill; B1 is read-only reference. Keeping them separate means you never have to delete example-specific prose out of the generic files.

---

## The slot convention

Every place you must supply project-specific content is a literal double-angle slot:

- `<<PROJECT_NAME>>`, `<<STACK>>`, `<<REPO_PATH>>` — simple substitutions.
- `<<SLOT: what to write here, and why it matters>>` — a prose slot with guidance inline.
- `<<OPTIONAL: ...>>` — include only if the described situation applies to your project.

**The instantiation gate:** after filling a template file, run `grep -rn '<<' .` at the template root. **Any remaining `<<` is an unfilled slot.** A clean grep means every slot was consciously resolved. `SETUP.md` makes this the last step before your first sprint.

Adopted-if markers use `<<ADOPT-IF: trigger — what to add when it fires>>`. These are things the audit deliberately did **not** turn on (e.g. per-area coding-agent skills, promoting a soft CI check to a hard gate). Leave them as-is; they are the written-down "revisit when X" so a future you doesn't rebuild the reasoning.

---

## File tree

```
workflow-template/
  README.md                         ← this file: layers, slot convention, tree, status
  SETUP.md                          ← START HERE: the linear repo-to-first-sprint runbook
  INSTANTIATE.md                    ← per-layer detail behind the setup steps
  diagrams/                         ← Mermaid sources: the setup flow + the run loop
  teaching/                         ← TEMPORARY workshop material — delete after the workshop

  layer-a/                          ← generic workflow (copy-and-go)
    project-instructions.template.md   the governing instruction set (roles, rules, loop, formats)
    living-docs/                        the doc set every project keeps
      agent_handoff.template.md           always-current state; read first each session
      project_management.template.md      workflow + task-index (§6) row format
      completed_development.template.md   per-entry close-out convention
      bug_log.template.md                 active/fixed bugs + the traps-log convention
      decision-log.template.md            numbered architectural decisions
      development_workflow.template.md     the branch/PR loop + when to skip the PR
      devops_pipeline.template.md          what CI runs + ratchet-promotion criteria

  checklists/                       ← always-on PM procedures (NOT skills — see audit §3.3)
    close-out.checklist.md              the atomic close-out (the four edits, in order)
    spec-authoring.checklist.md         the six-section spec + the pre-flight rules
    packaging-preflight.checklist.md    the runner-environment traps to read before a release tag

  agent-config/                     ← per-agent persistent config (each agent's own mechanism)
    CLAUDE.template.md                  coding-agent invariants (the constitution subset)
    cursor-rules.template.md            review-agent QA role (.cursor/rules/) — mechanical QA
    sub-agents.md                       decision: keep on-demand; do not formalize (+ adopt-if)
    skills.md                           decision: adopt none; the adopt-if trigger

  layer-b2/                         ← architecture-capture scaffold (copy-and-fill)
    architecture-facts.scaffold.md      "Key Architecture Facts" pattern, slots only
    contract-sync.scaffold.md           contract-docs-move-in-the-same-commit rule
    authority-docs-by-area.scaffold.md  the "read the one doc that governs what you touch" index
    traps-log.scaffold.md               the "green everywhere, broken where nobody looks" log
    ratchet.scaffold.md                 the raw-value ratchet (a guard that only ever tightens)

  layer-b1-example/                 ← the same scaffold, filled in (read-only reference)
    architecture-facts.example.md
    authority-docs-by-area.example.md
    traps-log.example.md
```

---

## Where each file goes

The template's files land in **different places**, and this is the part newcomers miss. Each of the four roles configures through its **own** mechanism — only the PM's config is Claude Project instructions.

| Template file | Destination | Loaded by |
|---|---|---|
| `layer-a/project-instructions.template.md` | the **Claude Project instructions field** (+ a git-tracked mirror in the repo) | PM agent, every session |
| `agent-config/CLAUDE.template.md` | `CLAUDE.md` at the repo root | coding agent |
| `agent-config/cursor-rules.template.md` | `.cursor/rules/` in the repo | review agent |
| `layer-a/living-docs/*` | `<<DOCS_DIR>>` in the repo | all agents, on demand |
| `layer-b2` architecture-facts + traps (filled) | `<<DOCS_DIR>>` in the repo | referenced by specs |
| `checklists/*` | `<<DOCS_DIR>>` (or wherever the PM keeps procedures) | PM, per task |
| `agent-config/sub-agents.md`, `agent-config/skills.md` | reference only — recorded decisions, not config to install | — |

**Rule of thumb:** the PM is configured *in the Claude Project*; every other role is configured *by a file in the repo*.

---

## Status — complete

All template files are authored. What remains is project-specific: standing it up for a real new project via `SETUP.md`, and (optional) turning this folder into a GitHub template repo (steps at the end of `INSTANTIATE.md`).

| Area | Files | Status |
|---|---|---|
| Scaffold framing | `README.md`, `SETUP.md`, `INSTANTIATE.md`, `diagrams/` | ✅ |
| Layer A — Instructions | `layer-a/project-instructions.template.md` | ✅ |
| Layer A — living docs | `layer-a/living-docs/*` (7) | ✅ |
| Checklists | `checklists/*` (3) | ✅ |
| Agent config | `agent-config/*` (4) | ✅ |
| Layer B2 scaffold | `layer-b2/*` (5) | ✅ |
| Layer B1 example | `layer-b1-example/*` (3) | ✅ |
| Workshop teaching (temporary) | `teaching/*` | delete after the workshop |

---

## Provenance

Extracted from a real, running software project and generalized. The project it came from is intentionally not named, so the template can be shown freely as a neutral reference. The three decisions that shaped the agent-config layer: **D1** — the review agent does *mechanical* QA (compiles, tests pass, diff matches acceptance criteria); the human drives behavioral testing. **D2** — no agent adopts the skills mechanism; value ships through the mechanism that fits each (coding-agent config, review-agent rules, PM checklists). **D3** — ground-truth deference is its own numbered rule (the human's statements about their own environment override the PM's inference).

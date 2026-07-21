# How to Instantiate This Template for a New Project

> **Want the clean step-by-step from empty repo to first sprint? Use [`SETUP.md`](SETUP.md).** This file is the deeper, per-layer detail *behind* those steps — read it when a setup step needs more explanation.

A step-by-step to stand up the whole loop for a new project — and a short guide to **teaching** it, since a template nobody can explain is a template nobody adopts. Read `README.md` first for the layers and the slot convention; this is the do-it guide.

---

## The mental model (teach this first)

Four participants, **four different config mechanisms** — this is the thing newcomers trip on, so lead with it:

| Role | What they do | Configured by |
|---|---|---|
| **Human lead** | product decisions, behavioral/runtime testing, ground truth | their own head |
| **PM agent** | specs, architecture reasoning, read-verification, doc upkeep | **Claude Project instructions** |
| **Coding agent** | writes the code | **`CLAUDE.md`** in the repo |
| **Review agent** | mechanical QA (compiles/tests/diff-vs-criteria) | **`.cursor/rules/`** in the repo |

And **one idea** under all of it: every rule in the system is a real failure someone already hit, turned into a habit that prevents it. Nothing is there for ceremony — the conservative bar (does this beat a plain rule?) was applied to every piece.

---

## Steps

### 1. Copy the template into (or beside) your new repo
Start from this folder (or the GitHub template repo — see the end). Keep the layer structure; you'll delete the scaffolding once slots are filled.

### 2. Fill Layer A — the workflow (mostly generic, quick)
- **`layer-a/project-instructions.template.md`** → fill the slots (project description, stack, repo path, build commands, the doc names). Paste the result into your **new project's Claude Project instructions field**, and keep a git-tracked **mirror** of it in the repo (e.g. `docs/claude_project_instructions.md`) so the governing doc is diffable. The Project field is canonical; the mirror follows it.
- **`layer-a/living-docs/*`** → fill slots, drop into your `docs/` dir. Most start nearly empty (`agent_handoff`, `completed_development`, `bug_log`) and fill as you work. `project_management` (task-index row format) and the two workflow docs are usable immediately.
- **`checklists/*`** → these are already generic; place them where the PM will reach for them (usually `docs/`). Fill the few command slots.

### 3. Fill Layer B2 — your architecture facts (the real thinking)
This is where your project's specifics go. Use `layer-b1-example/*` as the model — read it, then write your own:
- **`architecture-facts.scaffold.md`** → your hard constraints. Name the single hardest one "no exceptions."
- **`authority-docs-by-area.scaffold.md`** → your area→doc index.
- **`contract-sync.scaffold.md`** → fill the "change X → also update Y" mapping for your boundaries.
- **`traps-log.scaffold.md`** → adopt the convention; start the log empty.
- **`ratchet.scaffold.md`** → only if you have a specific value to drive to zero.

### 4. Install the agent config
- **`agent-config/CLAUDE.template.md`** → `CLAUDE.md` at the repo root. Keep it minimal (invariants only).
- **`agent-config/cursor-rules.template.md`** → `.cursor/rules/qa-role.mdc` in the repo.
- **`agent-config/sub-agents.md`, `skills.md`** → keep as reference (recorded decisions); nothing to install.

### 5. Wire CI
Use `layer-a/living-docs/devops_pipeline.template.md` as the runbook and stand up the actual CI config it describes (typecheck, lint, test, doc-freshness; read-only token). Start soft checks non-blocking.

### 6. Run the instantiation gate
```
grep -rn '<<' .
```
**Every remaining `<<` is an unfilled slot.** A clean grep means every slot was consciously resolved — the same "a human considered this" guarantee the workflow relies on everywhere. Leave `<<ADOPT-IF: …>>` markers in place on purpose; they're the written-down "revisit when X."

---

## Teaching it to someone (a 10-minute walkthrough)

1. **The four roles and their four config mechanisms** (the table above). Where each piece lives.
2. **The loop** (`development_workflow.md`): spec → branch → code → QA → PM read-verify → human runtime-test → atomic close-out → PR → CI → merge.
3. **Walk the rules.** Read the numbered rules in the project instructions out loud; each is "here's a failure, here's the habit." This is the fastest way to convey *why* the discipline exists.
4. **The two things that keep docs true:** contract-sync (Rule 12) and user-docs-in-the-same-commit (Rule 18) — a change and its documentation move together, always.
5. **The traps log:** where "green everywhere, broken where nobody looks" lessons live, so automated green is never mistaken for correct.

---

## Turning this folder into a GitHub template repo (the nice-to-have)

From the template root:
```
git init
git add .
git commit -m "Agentic-devops workflow template v1"
git remote add origin <<YOUR_TEMPLATE_REPO_URL>>
git push -u origin main
```
Then in the repo's **Settings → General**, tick **"Template repository."** New projects start with **"Use this template."** Because the template is a standalone sibling (not nested in a product repo), this is a clean `git init` with nothing to strip out.

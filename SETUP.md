# SETUP — From Nothing to a Running Pipeline

**The complete runbook.** Every step from "I have no project" to "I'm running the DevOps pipeline," in order. Do it once, top to bottom. For per-layer detail see `INSTANTIATE.md`; for the concepts see `teaching/`.

**What you're standing up:** four roles, four config homes.

| Role | Configured by | Where it lives |
|---|---|---|
| Project Agent (Planner) | Claude project instructions | Claude Desktop (+ a repo mirror) |
| Developer Agent (Builder) | `CLAUDE.md` | repo root |
| Peer-Review Agent (Checker) | `.cursor/rules/` | the repo |
| You (the Boss) | your own head | — |

**The big idea in this runbook:** you don't fill the instruction template by hand. You create the project with a **setup prompt**, and the agent **interviews you and drafts its own instructions**. Then a second **bootstrap prompt** finishes the rest. Two prompts, at two different points — that's the whole trick.

---

## Before you start (prerequisites)

- **Claude account with Claude Desktop installed** — the Project Agent lives here.
- **Claude Code enabled** — the Developer Agent.
- **Cursor installed and authenticated with Claude** — the Peer-Review Agent.
- **GitHub account + `git` installed locally.**
- **The Filesystem connector available to Claude Desktop** — this is what lets the Project Agent read and write your repo. Without it, nothing downstream works.
- **Your language toolchain** (e.g. Python or Node) as the build needs.

---

## The steps

### 1. Create the repo from the template
On GitHub, open the template repo → **Use this template** → create your new repo (private).

### 2. Pull it local
```
git clone <your-new-repo-url>
cd <your-new-repo>
```

### 3. Create the Claude project
In Claude Desktop, create a new project and **name it `<Product> PM`** — it's the Project Agent's workspace. **Leave the instructions field empty for now.** We're about to generate the real instructions, so there's nothing to paste yet.

### 4. Connect the project to the repo
Add the **Filesystem connector**, pointed at your local repo path. This is the step people skip — and the agent can't read the template or write your docs without it. Do it before the next step.

### 5. Draft the instructions (Setup Prompt)
Open a chat in the project and paste the **Setup Prompt** (full text below). The agent will read the instructions template, **interview you about what you're building**, and draft the filled-in project instructions — changing only the template's `<<slots>>` and leaving the battle-tested rules intact.

### 6. Install the instructions
Review the draft. When it's right, paste it into the project's **Instructions field** (Settings → replace whatever's there — this is the canonical copy the Project Agent reads every session). Then commit a **mirror** into the repo (e.g. `docs/claude_project_instructions.md`) so the governing doc is diffable in git.

### 7. Bootstrap the rest of the pipeline (Bootstrap Prompt)
Open a **new** chat — this one now loads your real instructions, so it *is* the Project Agent. Paste the **Bootstrap Prompt** (full text below). It reads the template, helps you fill **Layer B** (your architecture facts, authority-docs index, contract-sync map), confirms the other config is in place, and runs the slot gate.

### 8. Configure the Developer Agent
Put your filled **`CLAUDE.md`** at the repo root (from `agent-config/CLAUDE.template.md`). Keep it minimal — invariants only.

### 9. Configure the Peer-Review Agent
Add your filled **`.cursor/rules/qa-role.mdc`** to the repo (from `agent-config/cursor-rules.template.md`). Confirm the review step is wired.

### 10. Wire CI
Stand up the CI config described by `docs/devops_pipeline.md` — typecheck, lint, test, doc-freshness; read-only token; any noisy check starts non-blocking.

### 11. Run the gate and clean up
```
grep -rn '<<' .
```
Every remaining `<<` is an unfilled slot — resolve each (leave `<<ADOPT-IF: …>>` markers in place on purpose). Then delete `layer-b1-example/`, and drop any onboarding docs (`README.md`, `INSTANTIATE.md`, `teaching/`, `diagrams/`) you don't want to keep in the project repo.

### 12. Start your first sprint
Put your top item in `docs/backlog.md`, then tell the Project Agent **"let's spec the first task."** From here every task rides the loop in `docs/development_workflow.md`. **You're now running the pipeline.**

---

## The Setup Prompt  *(paste in step 5 — the project has no instructions yet)*

```
You are helping me set up a new software project's Project Agent — the planning
agent for an agentic DevOps pipeline. Right now you have no project instructions;
your ONLY job in this chat is to produce them.

Do this:

1. Read `layer-a/project-instructions.template.md` in this repo. It is the exact
   skeleton for the instructions — numbered rules and sections with `<<slots>>`
   to fill. The rules and structure are deliberate and battle-tested: DO NOT
   rewrite, reorder, add, or remove rules or sections. Change ONLY the `<<slots>>`.

2. Interview me to fill the slots. Ask a few questions at a time — whatever you
   need to fill every slot:
   - what we're building (product, who it's for, what makes it distinctive)
   - the stack, and the build / dev / release commands
   - the repo path
   - the names of the living docs and where they live (default to the template's)
   - the human lead's name, the coding agent, and the review agent
   Ask follow-ups when my answer is vague. Don't guess a slot you could ask about.

3. When every slot is filled, output the COMPLETE instructions as one copy-paste
   block, ready for me to drop into the Claude project's instructions field.
   Keep every rule and section verbatim — only the slots should differ from the
   template.

Do not plan features or write any code. This task is done when the filled
instructions are in my hands.
```

## The Bootstrap Prompt  *(paste in step 7 — a fresh chat, real instructions now loaded)*

```
You are the Project Agent for <<Product>>. Your project instructions are now
loaded in this project. This first task is SETUP, not feature work.

Do this with me, one step at a time, asking me wherever a decision is mine:

1. Read the template docs in the repo: README.md, INSTANTIATE.md, everything
   under layer-b2/, and layer-b1-example/ as the worked example.
2. Help me fill Layer B2 for THIS project — my Key Architecture Facts, the
   authority-docs-by-area index, and the contract-sync map — using the worked
   example as the model. Write them into docs/ as we go. Start the traps log empty.
3. Confirm CLAUDE.md is at the repo root and .cursor/rules/ exists, both filled
   (no <<slots>> left).
4. Confirm CI is wired per docs/devops_pipeline.md.
5. Run (or have me run) `grep -rn '<<' .` at the repo root and resolve every
   remaining slot until it comes back clean. Then delete layer-b1-example/.

When the grep is clean and 3–5 are done, tell me the workflow is set up, and help
me write the very first task spec.
```

---

## Recap (the whole path in one breath)

Create the repo → pull local → create the `<Product> PM` project (empty) → connect it to the repo → **Setup Prompt: the agent interviews you and drafts its instructions** → install those instructions + mirror them → **Bootstrap Prompt: the agent finishes Layer B and config** → wire Developer + Peer-Review agents → run the slot gate → first sprint.

**Two prompts, two moments:** the **Setup Prompt** runs *before* instructions exist (it writes them); the **Bootstrap Prompt** runs *after* they're installed (it finishes the rest).

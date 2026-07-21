# Day 1 — At a Glance

*One-sheet teaching index. Agentic DevOps for Industry 4.0 · Day 1 (Theory & Setup) · Tue Jul 21, 2026 · 9:00 AM–1:00 PM CDT.*
*Each hour = 45-min lesson + 15-min break. Full docs: `hour-1…` through `hour-4…` in this folder.*

**Agent key (used all day):** Boss = you · **Planner = Project Agent (Claude Desktop)** · **Builder = Developer Agent (Claude Code)** · **Checker = Peer-Review Agent (Cursor)**. No formal sub-agents — the Builder spins one up only if *it* decides to, case by case.

---

## The running clock

| Time | Block |
|---|---|
| 9:00 – 9:45 | **Hour 1** — The Post-Agentic World: Buy, Build, and Why Agentic DevOps Matters |
| 9:45 – 10:00 | Break |
| 10:00 – 10:45 | **Hour 2** — How the Workflow Works |
| 10:45 – 11:00 | Break |
| 11:00 – 11:45 | **Hour 3** — The Pipeline in Depth, then Pull the Template |
| 11:45 – 12:00 | Break |
| 12:00 – 12:45 | **Hour 4** — Kickoff for Day 2: Pick the Build, Stand Up the Pipeline |
| 12:45 – 1:00 | Day-1 wrap / Q&A |

---

## Hour 1 — The Post-Agentic World: Buy, Build, and Why Agentic DevOps Matters  *(9:00–9:45)*

| ~Min | Beat |
|---|---|
| 10 | **Intros** — go-round: name, role, last AI-build attempt + where it hurt |
| 5 | **What to Expect** — 2-day frame; Day 1 theory+setup, Day 2 live build; prereq check |
| 10 | **Has Buy vs. Build Changed?** — buy the substrate · build the edge · own agentic integration |
| 12 | **What to Study** — 5 layers: Model · Orchestration · Data · Engineering discipline · Judgment (we live in Engineering discipline) |
| 8 | **What Is Agentic DevOps & Why It Matters** — critical-mass failure mode; ~600-sprint / zero-regression proof |

---

## Hour 2 — How the Workflow Works  *(10:00–10:45)*

High-level tour + discussion (Hour 3 goes deep). Beats:

- **The cast** — four roles, each covering the others' blind spots.
- **Why the split matters** — Planner reads, Checker runs; neither alone is enough.
- **The loop** — spec → branch → build → review → PM read-verify → runtime test → atomic close-out → PR → CI → merge.
- **The memory problem** — the living docs (notebooks) are read first, updated the instant a task is done.
- **Every rule is a scar** — walk a few; each is a prevented failure.
- **Green isn't proof** — a human reads or runs the real thing.

*Visual: `diagrams/workflow-loop.md`.*

---

## Hour 3 — The Pipeline in Depth, then Pull the Template  *(11:00–11:45)*

| ~Min | Beat |
|---|---|
| 3 | **How this hour works** — 200-student reality: do-your-own-repo if you can, else watch + replicate; all become collaborators |
| 22 | **Pipeline in depth, live on Notus** — living-docs memory · the three agents in action · sub-agent note · **regression caught (proof)** · human gates |
| 15 | **Hands-on** — pull the template → create the repo *(setup steps 1–2)*; **stop right before the Claude project** |
| 5 | **Wrap** — you have a repo; next hour we pick the build and stand up the pipeline |

*Bring: a real Notus regression example for the "proof" beat.*

---

## Hour 4 — Kickoff for Day 2: Pick the Build, Stand Up the Pipeline  *(12:00–12:45)*

| ~Min | Beat |
|---|---|
| 5 | **Day-2 build format** — live build, not a lecture; published to the shared repo |
| 8 | **Cohort vote** — general I4.0 · UNS/MQTT · manufacturing AI agent · Python microservice |
| 3 | **Make it available + confirm Python** — add product context to the repo; all collaborators |
| 6 | **Create & connect the Project Agent** — new Claude project (empty instructions) · connect Filesystem *(the skipped step)* |
| 8 | **Draft the instructions** — Setup Prompt: the agent interviews us and writes its own instructions → install + mirror |
| 7 | **Bootstrap** — Bootstrap Prompt: the Planner finishes Layer B and config |
| 5 | **Wire Developer + Peer-Review** — `CLAUDE.md` · `.cursor/rules/` *(async-fallback if tight)* |
| 3 | **Assign Day-2 roles + close** — "you run the loop tomorrow" |

*Note: architecture facts fill in as we build Day 2 — today stands up the structure.*

---

## What students leave Day 1 with

A working mental model of the pipeline · a repo from the template · a Project Agent stood up and bootstrapped (Developer + Peer-Review wired or finishing async) · a chosen product for Day 2 in a shared repo they all collaborate on.

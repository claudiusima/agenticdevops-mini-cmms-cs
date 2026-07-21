# Hour 3 — The Pipeline in Depth, then Pull the Template

## Agenda

- How This Hour Works
- The Memory That Doesn't Forget
- The Three Agents at Work
- A Regression Getting Caught
- Where Humans Still Gate
- Hands-On: Pull the Template & Create Your Repo

Hour 2 was the map. This hour is the territory — I'll open up my real, running pipeline on Notus so you can see the discipline actually working, then everyone pulls the template and creates their own repo. We stop right before standing up the Project Agent; that's Hour 4.

---

## 1. How This Hour Works

This session is hands-on, but there are a lot of us on this call — there's no way to troubleshoot every environment live. So here's the deal:

- If you can create your repo alongside me, do it.
- If you hit a snag, just watch — you'll replicate it after, and **every student gets added as a collaborator on my repo**, so nobody is locked out.
- Drop environment problems in the helper channel; we'll sweep them rather than stall the room.

If you're watching rather than doing, aim to leave with a clear mental model and a repo you can reproduce in ten minutes afterward.

---

## 2. The Memory That Doesn't Forget

Everything starts with the living docs — the pipeline's memory. On Notus, that's the handoff (where we are right now), the completed-work log, the task index, and the bug log.

The agents forget between sessions; these docs don't. Every task begins by reading them and ends by updating them in the same turn. This one habit is what prevents drift — the slow rot where the next session builds on a wrong picture of the project.

---

## 3. The Three Agents at Work

Watch each agent do its one job on the real pipeline.

- **The Planner (Project Agent — Claude Desktop)** owns the product. It reads the docs, reasons about the change, and writes the spec — the exact instruction sheet for one task — before a line of code is written. No spec, no build.
- **The Builder (Developer Agent — Claude Code)** takes the spec and writes the code against it.
- **The Checker (Peer-Review Agent — Cursor)** reviews mechanically — does it compile, do the tests pass, does the change match what the spec asked for — and catches gaps a read alone would miss.

**A note on sub-agents:** this pipeline does not use a formal cast of sub-agents. The Builder will occasionally spin one up on its own, case by case, if it decides a task needs one — but that's its call, not a layer we configure. Don't over-engineer this.

---

## 4. A Regression Getting Caught

This is the proof. I'll walk a real case from the Notus history where a change would have quietly broken something else, and show exactly where the pipeline caught it.

The point to land: the automatic checks can all be green while something is still wrong. The discipline — the spec, the read-back, the review — is what catches it. That's the difference between building that survives scale and building that collapses at critical mass.

---

## 5. Where Humans Still Gate

This is not full autonomy, and it shouldn't be. The human keeps the gates that matter:

- Product decisions.
- The runtime test — does this actually work, and does it feel right?
- Sign-off on anything consequential or destructive.

The pipeline makes the agents trustworthy to delegate to. It does not take you out of the loop.

---

## 6. Hands-On: Pull the Template & Create Your Repo

Now everyone stands up the starting point.

1. **Create the repo from the template.** On GitHub: open the template repo → Use this template → new repo. (Or create an empty repo and copy the template folder in.) Clone it locally.
2. **Seed the template** and look at the layer structure — the generic workflow, the fill-in scaffolds for your project's own rules, and the read-only worked example.

We stop here — right before creating the Project Agent. That's the first thing we do in Hour 4, once we know what we're building. Do it now if you can; otherwise watch, and remember you'll all be collaborators on my repo.

---

## Break (15 min)

Back for Hour 4 — Kickoff for Day 2.

---

## The four things to leave Hour 3 with

1. **The living docs are the memory** — read at the start of every task, updated the moment it's done; this is what stops drift.
2. **Each agent has one job** — Planner plans and holds context, Builder writes, Checker reviews; no formal sub-agents.
3. **Green isn't proof** — you saw a regression the checks would have missed get caught, and the human gates that keep this from being blind autonomy.
4. **You have a repo** — the pipeline gets stood up around a real product next hour.

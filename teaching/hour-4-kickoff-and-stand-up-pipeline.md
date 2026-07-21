# Hour 4 — Kickoff for Day 2: Pick the Build, Stand Up the Pipeline

## Agenda

- The Day-2 Build Format
- Pick the Product
- Make It Available
- Create & Connect the Project Agent
- Draft the Instructions (the agent writes its own)
- Bootstrap the Pipeline
- Wire the Developer & Peer-Review Agents
- Assign Day-2 Roles & Close

We decide what we're building tomorrow, put it in the shared repo, then stand up the pipeline — and the neat part is that the Project Agent **writes its own instructions** about the very thing we just voted to build. The goal: Day 2 is a live build on the pipeline you configured yourself, not a lecture.

---

## 1. The Day-2 Build Format

Day 2 is a live, end-to-end build of the tool we're about to pick, using this pipeline: product scaffolding → core development → integration and testing with a full peer-review pass → publish to the shared private repo. Everyone is a collaborator, so everyone gets the result. It's a build, not a lecture — you'll be running the loop, not watching slides.

---

## 2. Pick the Product

Four framed categories. We vote, and we land on one.

| Category | Example |
|---|---|
| A general Industry 4.0 tool | a broadly useful shop-floor or integration utility |
| A UNS / MQTT data tool | something that reads, shapes, or routes UNS/MQTT data |
| An AI agent solving a manufacturing problem | anomaly detection · downtime logger · OEE calculator |
| A Python microservice | a focused service other tools call |

Keep the vote about the category, not the fine details — we shape the specifics once we start building. Default build language is Python; it changes only if the pick clearly dictates otherwise.

---

## 3. Make It Available

We add the selected product's starting context to the repo so the cohort has one shared, canonical place for it. Everyone is a collaborator, so everyone can see it and follow along tomorrow.

---

## 4. Create & Connect the Project Agent

Now we create the pipeline's brain.

1. **Create the Claude project (the Project Agent)** in Claude Desktop. Name it after the product plus its role — it's the Planner's workspace. Leave the instructions field empty for now; we're about to generate the real ones.
2. **Connect it to the repo** with the Filesystem connector, pointed at the repo. This is the step people skip — and without it, the agent can't read the template or write our docs, which is its whole job.

---

## 5. Draft the Instructions (the agent writes its own)

Open a chat and paste the **Setup Prompt**. The agent reads the instruction template, then **interviews us about the product we just voted to build** — and drafts the filled-in project instructions, keeping the battle-tested rules and filling only the blanks. Point this out to the room: the pipeline is writing its own configuration, tailored to today's decision. Review the draft, then paste it into the project's instructions field and mirror it into the repo.

---

## 6. Bootstrap the Pipeline

Open a **new** chat — this one loads the real instructions, so it *is* the Project Agent now. Paste the **Bootstrap Prompt**. It reads the template, helps fill Layer B, confirms the pieces are in place, and runs the slot gate. The pipeline's brain is finishing its own setup with you — that's the pipeline already doing its job.

One expectation to set: the project's detailed architecture facts — its hard rules and traps — get filled in as we build tomorrow, because they come from the real code. Today stands up the structure; Day 2 fills in the specifics.

---

## 7. Wire the Developer & Peer-Review Agents

With the Project Agent live, add the other two:

- **Developer Agent (Claude Code):** drop `CLAUDE.md` at the repo root — the coding agent's invariants — and connect it to the project context.
- **Peer-Review Agent (Cursor):** add the `.cursor/rules/` file that gives Cursor its standing review job, and confirm the review step is wired.

If we're tight on time, the load-bearing part is the Project Agent plus the two prompts — it's fine to finish the Developer and Peer-Review wiring before we start Day 2.

---

## 8. Assign Day-2 Roles & Close

- **Have open for Day 2:** Claude Desktop (Project Agent), Claude Code, Cursor, and the repo.
- **Watch for:** the loop in action — spec → build → review → your runtime test → close-out — and the living docs updating as we go.
- **The promise:** tomorrow is a live build on the pipeline you just configured yourselves. You're not going to watch me build — you're going to run the loop.

---

## End of Day 1

Day 2 — the live build.

---

## The four things to leave Hour 4 (and Day 1) with

1. **You picked the build** — Day 2 has a real target, in the shared repo, everyone a collaborator.
2. **The agent wrote its own instructions** — the Setup Prompt drafted them from an interview about today's pick.
3. **The pipeline is stood up** — instructions installed, bootstrapped, Developer and Peer-Review agents wired (or finishing before Day 2).
4. **Day 2 is yours to run** — a live build on your own configured pipeline, not a lecture.

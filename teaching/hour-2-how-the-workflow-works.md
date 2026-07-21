# Hour 2 — How the Workflow Works

## Agenda

- The Cast: You + Three AI Agents
- Why the Split Matters
- The Loop
- The Memory Problem
- Every Rule Is a Scar
- Green Isn't Proof

The pipeline is four roles and one strict habit — write it down, read it back, keep the notebooks true. This hour is the high-level tour: who does what, how a single job flows through them, and why it holds together at scale. Next hour we open it up on a real, running project.

---

## 1. The Cast: You + Three AI Agents

You don't build alone. Four participants, and each does the part they're best at.

| Nickname | Official role | The tool | What they do |
|---|---|---|---|
| The Boss | you, the human lead | — | Decide what to build. Click around the finished thing and say "yes, that's right" or "no, that's broken." |
| The Planner | Project Agent | Claude Desktop | Think hard, write down exactly what to build before anyone codes, then check the finished work by carefully reading it. |
| The Builder | Developer Agent | Claude Code | Write the actual code. |
| The Checker | Peer-Review Agent | Cursor | Make sure the code turns on, passes its tests, and matches what the Planner asked for. |

---

## 2. Why the Split Matters

The whole point is that each agent catches mistakes the others can't:

- The **Planner** can read code but can't run it.
- The **Checker** can run it but shouldn't make the big decisions.
- The **Boss** can feel when something's off but shouldn't have to babysit the boring checks.

Take any one away and things slip through. That's the design — overlapping blind spots, not a single point of trust.

---

## 3. The Loop

One job flows through the pipeline in a fixed order:

1. **Boss** says what they want.
2. **Planner** writes a small instruction sheet — a "spec" — for that one job.
3. **Builder** builds it.
4. **Checker** runs it — does it turn on, pass tests, match the sheet?
5. **Planner** reads the finished code — did anything else break?
6. **Boss** clicks around and gives the thumbs-up.
7. **Planner** writes down what got done — in the same breath.

Nothing skips step 2. No building without a written sheet first — a job with no sheet can't be checked against anything. *(The picture: `diagrams/workflow-loop.md`.)*

---

## 4. The Memory Problem

Here's the key idea. The AI agents forget everything between jobs — every session starts blank.

So the project keeps a set of notebooks that never forget:

| Notebook | What it holds |
|---|---|
| Handoff | "Where are we right now?" — read this first, every time. |
| Completed work | Everything we've ever built, so we don't rebuild it. |
| Bug log | Every bug we've hit, and the traps that fool people. |
| Task list | What's in progress, what's done. |
| Decisions | The big choices we made, and why. |

Before anyone starts a job, they read the notebooks. If the notebooks are wrong, everyone gets lost. So there's one iron habit: **the moment a job is done, update the notebooks in the same breath — never "later."** Later never comes, and a stale notebook sends the next session in the wrong direction.

---

## 5. Every Rule Is a Scar

The pipeline has a list of rules, and they can look like a lot. Here's the frame that makes them click:

> Every rule is a scar. Each one is a specific, real failure that already happened once — turned into a habit so it can't happen again.

A few examples:

- **"Read the real code before you write anything."** Guessing what the code says causes real defects.
- **"When the Boss says he uses version 22, believe him."** The Planner once argued with the Boss about his own machine for three rounds and was wrong the whole time.
- **"A search that finds nothing tells you about the search, not the code."** Prove your search works before you trust its silence.
- **"Change a contract, change its documentation in the same breath."** Or the docs quietly go false — and false docs are worse than none, because people trust them.

Teach the rules by walking the list and telling the story behind each one. The story is what makes people follow a process instead of quietly abandoning it.

---

## 6. Green Isn't Proof

The automatic checks — does it compile, do the tests pass — can all be green while the thing is still broken, because none of them looked in the place it broke. We keep a list of these called traps: "looks fine to every automatic check, still wrong, here's how to actually catch it."

The lesson underneath: a green light is not proof. A human reading or running the real thing is the real gate — which is exactly what you'll see next hour, live.

→ Coming up in Hour 3: the same pipeline, opened up on my real project (Notus), with each part doing its job — then everyone pulls the template and creates their repo.

---

## Break (15 min)

Back for Hour 3 — The Pipeline in Depth.

---

## The four things to leave Hour 2 with

1. **Four roles, each covering the others' blind spots** — Boss, Planner, Builder, Checker.
2. **The agents forget; the notebooks don't** — read them first, update them the instant a job is done.
3. **Every rule is a healed scar** — not ceremony, prevention.
4. **Green isn't proof** — a human reading or running the real thing is the real gate.

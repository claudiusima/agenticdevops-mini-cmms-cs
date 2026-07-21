# Hour 1 — The Post-Agentic World: Buy, Build, and Why Agentic DevOps Matters

## Agenda

- Welcome
- What to Expect
- Has Buy vs. Build Changed?
- What Should I Study or Learn?
- What is Agentic DevOps and Why Does it Matter?

In the post-agentic world you no longer wait for a vendor to build every tool — you buy the platform and build the gaps — but building with AI agents collapses at scale unless you run it with real DevOps discipline. This workshop teaches that discipline.

---

## 1. Welcome

- Fellowship
- Introduce the instructor (Me)
- Foundations of Digital Transformation, Industry 4, Industry 5

---

## 2. What to Expect

Over the next two days...

- **Day 1 (today):** why the post-agentic world changes how you build, the pipeline framework, and hands-on setup of your own three-agent pipeline. Ends with the cohort voting on what to build tomorrow.
- **Day 2:** a live, end-to-end build of a real Industry 4.0 tool with the pipeline you configured — published to a private GitHub repo as we go.
- **What you keep:** the reusable pipeline (not scoped to the one tool), the tool itself, a backlog/gap analysis, and the recording at iiot.university.
- **Level & prerequisites:** intermediate; assumes Industry 4.0 / IIoT familiarity (UNS, MQTT, edge/cloud); does not require a software-development background (but it will certainly help). The tools we will be using — Claude Desktop, Cursor, Claude Code, and a GitHub account.

---

## 3. Has Buy vs. Build Changed?

Short answer: yes. For years the rule was "buy everything; build nothing you can avoid," because building meant hiring a software team that could build and maintain software manually. AI agents changed that math — you can now build just the gaps, cheaply, without a dev team. The line between buy and build didn't disappear — but it did move.

| You BUY | You BUILD | You BUY and BUILD |
|---|---|---|
| Connect · collect · store · enterprise-analyze | User-level analyze · visualize · find patterns · report · solve | Agentic integration |
| The platform substrate — hard, standardized, and not your differentiator: brokers, historians, MES, DataOps, enterprise analytics. | The gap-closing tools — the specific analysis, views, pattern-finding, reports, and solutions your operation needs and no vendor ships. | The connective tissue — agents that reach across bought platforms and built tools. Part vendor capability, part your own wiring. |

Your take away: buy the commodity substrate, build the differentiated edge, and treat agentic integration as the seam you own. Everything after this is about building that "build" column without it collapsing.

---

## 4. What Should I Study or Learn?

Five layers. You don't have to master all five — but you should know what each is and which ones you're weakest in. Walk each; ask the room where they feel the gaps.

| Layer | What it is | What to study |
|---|---|---|
| Model | The AI itself | LLM vs. SLM (a big general model vs. a small specialized one), context management, tokenomics — what tokens cost and how not to waste them |
| Orchestration | How agents act and coordinate | MCP (how agents connect to tools and data), tool calling, multi-agent workflows, guardrails / human-in-the-loop |
| Data | What the agents reason over | Contextualization, semantic modeling, the UNS as the substrate agents query, and knowledge graphs for traversing relationships |
| Engineering discipline | Keeping built software trustworthy | Agentic DevOps (this workshop), evals, observability, security & permissions |
| Judgment | Deciding what's worth building or buying | Build-vs-buy literacy, and evaluating vendor AI claims critically |

Think of it this way: Model, Orchestration, and Data are what you build with; Engineering discipline is what keeps it from collapsing; Judgment is what points it at the right problems. This workshop lives in the Engineering-discipline layer — the one almost everyone skips, and the one that decides whether "build" survives scale.

---

## 5. What Is Agentic DevOps, and Why Does It Matter?

**What it is.** A repeatable pipeline for building software with AI agents, run like real DevOps: a Project Agent that owns the product, plans the work, and holds context; a Developer Agent that writes the code; and a Peer-Review Agent that keeps it clean and catches gaps — wrapped in context management, documentation discipline, review gates, version control, and regression control. (Next hour we give these three plain nicknames — Planner, Builder, Checker — and walk exactly how they hand work back and forth.)

**Why it matters — the failure mode it prevents.** Almost everyone building with AI hits the same wall: the tools work fine at small scale, then collapse into regression-and-refactor hell the moment complexity crosses a critical mass. The problem isn't the AI — it's the absence of DevOps discipline built for agentic development. Without it, every new feature has a chance of silently breaking an old one, and you burn your gains cleaning up messes.

**The proof it works.** Two Industry 4.0 platforms, built solo alongside an army of agents at roughly $50K in compute — one of them past ~600 development sprints with zero regressions and zero refactors. That track record is the evidence this pipeline holds exactly where undisciplined agent-building falls apart.

**Why you should care specifically:** your "build" column from Section 3 only outweighs your "buy" column if what you build is disciplined enough to survive scale. Agentic DevOps is that discipline.

→ Coming up in Hour 2: how the pipeline actually runs — the four roles, the memory that carries between sessions, and the rules that keep every change honest.

---

## Break (15 min)

Back for Hour 2 — How the Workflow Works.

---

## The four things to leave Hour 1 with

1. **Buy vs. build changed:** buy the substrate (connect/collect/store/analyze), build the edge (analyze/visualize/pattern/report/solve), and own the agentic-integration seam.
2. **Five layers to grow in:** Model, Orchestration, Data, Engineering discipline, Judgment — this workshop is the Engineering-discipline layer.
3. **The failure mode is critical mass:** agent-built tools collapse into regression-and-refactor hell without DevOps discipline.
4. **Discipline is the whole game:** build only beats buy if it survives scale — and a ~600-sprint, zero-regression track record is the proof it can.

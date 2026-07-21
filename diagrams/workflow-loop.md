# Diagram source — How the workflow WORKS

*Mermaid flowchart. Renders directly and is clean source for an agent to build a diagram from. Shows how one job flows through the loop, including the checks that loop back.*

**Legend:** rounded = start/end · rectangle = an action · diamond = a check that can send the work back.
**Cast:** Boss = the human lead · Planner = Project Agent (Claude Desktop) · Builder = Developer Agent (Claude Code) · Checker = Peer-Review Agent (Cursor).
**Colors (intentional — keep them, they're by role):** 🟢 green = start/finish · 🔵 blue = the PM · 🟦 teal = the Builder · 🟡 yellow = a gate that can loop work back · ⬜ gray = a plain step.

```mermaid
flowchart TD
    S([Boss describes what they want]) --> R["PM reads the notebooks first — handoff, completed work, bugs — plus the relevant source and docs"]
    R --> SP["PM writes the spec (task_ID_slug.md) and adds the task-index row"]
    SP --> BR["Cut a branch"]
    BR --> CC["Builder (CC) implements — code + user-docs in one commit"]
    CC --> QA{"Checker (Cursor): typecheck / lint / tests pass, and the diff matches the acceptance criteria?"}
    QA -- "no" --> CC
    QA -- "yes" --> PV{"PM reads the actual changed files — anything broken or off-spec?"}
    PV -- "yes" --> CC
    PV -- "no" --> RL["Relaunch if the main/preload layer changed, so the running app is the new code"]
    RL --> BT{"Boss runtime-tests — does it work and feel right?"}
    BT -- "no" --> CC
    BT -- "yes" --> CO["PM atomic close-out, all in the same turn: task-index → done, bug log, completed work, handoff"]
    CO --> PR["Commit + push the branch, open a PR"]
    PR --> CI{"CI: typecheck / lint / tests / docs — all green?"}
    CI -- "red" --> CC
    CI -- "green" --> M([Squash-merge, delete the branch])

    classDef term fill:#DCFCE7,stroke:#16A34A,color:#14532D,stroke-width:2px;
    classDef pm fill:#DBEAFE,stroke:#2563EB,color:#1E3A8A;
    classDef build fill:#CCFBF1,stroke:#0D9488,color:#134E4A;
    classDef gate fill:#FEF9C3,stroke:#CA8A04,color:#713F12,stroke-width:2px;
    classDef step fill:#F1F5F9,stroke:#64748B,color:#0F172A;

    class S,M term;
    class R,SP,CO pm;
    class CC build;
    class QA,PV,BT,CI gate;
    class BR,RL,PR step;
```

**The through-line to point out when teaching:** the notebooks are read at the very start (top) and written at the close-out (`CO`) — the memory that carries between jobs. And the **four yellow diamonds** (Checker, PM read, Boss test, CI) are the four gates that can send work back — that's "green isn't proof; a human reads or runs the real thing," drawn as loop-backs.

**To have your agent build it:** paste this file (or the fenced block) with "build a flow diagram from this Mermaid, and keep the colors." Structure, branches, and the by-role palette are all encoded — the agent renders rather than infers.

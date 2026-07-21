# Diagram source — System Map: documents, personas, and how they work together

*Mermaid diagram. Renders directly (GitHub / VS Code / Obsidian / mermaid.live) and is clean source for an agent to build a diagram from. This is the "everything at once" view — the four personas, the documents each one uses, and the arrows that connect them.*

**Legend:** rounded = the human · boxes = agents and documents · a box's color tells you what kind of thing it is.
**Colors (intentional — keep them):** 🟢 green = the Boss · 🔵 blue = Planner · 🟦 teal = Builder · 🟣 purple = Checker · 🟡 yellow = the task spec (the artifact that flows) · ⬜ gray = agent config · 🟠 orange = the memory (living docs) · 🩷 pink = architecture capture · 🔵 indigo = PM checklists.

```mermaid
flowchart TD
    BOSS(["Boss — the human lead"])

    subgraph CONFIG["Agent configuration — how each agent is set up"]
        direction LR
        PI["project-instructions<br/>Claude Project + repo mirror"]
        CL["CLAUDE.md"]
        CR[".cursor/rules"]
    end

    subgraph AGENTS["The three AI agents"]
        direction LR
        PLAN["Planner<br/>Project Agent · Claude Desktop"]
        BUILD["Builder<br/>Developer Agent · Claude Code"]
        CHECK["Checker<br/>Peer-Review Agent · Cursor"]
    end

    SPEC["Task spec — one per job"]

    subgraph MEMORY["The memory — living docs (read first, updated at close-out)"]
        direction LR
        HAND["agent_handoff"]
        TASKS["task index"]
        DONE["completed_development"]
        BUGS["bug_log + traps"]
        DEC["decision-log"]
        BACK["backlog"]
        DW["development_workflow"]
        DP["devops_pipeline"]
    end

    subgraph ARCH["Architecture capture — what specs must enforce"]
        direction LR
        AF["architecture facts"]
        AUTH["authority-docs-by-area"]
        CS["contract-sync"]
    end

    subgraph PROC["PM procedures — checklists"]
        direction LR
        SA["spec-authoring"]
        CO["close-out"]
        PP["packaging-preflight"]
    end

    PI --> PLAN
    CL --> BUILD
    CR --> CHECK

    BOSS -->|says what to build| PLAN
    MEMORY -->|read first| PLAN
    ARCH -->|enforced by| PLAN
    PROC -->|followed by| PLAN
    PLAN -->|writes| SPEC

    SPEC --> BUILD
    ARCH -->|honored by| BUILD
    BUILD -->|code + synced contract/user docs| CHECK

    SPEC -->|acceptance criteria| CHECK
    CHECK -->|QA result| BOSS
    BOSS -->|runtime test + sign-off| PLAN
    PLAN -->|atomic close-out writes| MEMORY

    classDef boss fill:#DCFCE7,stroke:#16A34A,color:#14532D,stroke-width:2px;
    classDef plan fill:#DBEAFE,stroke:#2563EB,color:#1E3A8A,stroke-width:2px;
    classDef build fill:#CCFBF1,stroke:#0D9488,color:#134E4A,stroke-width:2px;
    classDef check fill:#EDE9FE,stroke:#7C3AED,color:#4C1D95,stroke-width:2px;
    classDef spec fill:#FEF9C3,stroke:#CA8A04,color:#713F12,stroke-width:2px;
    classDef cfg fill:#F1F5F9,stroke:#64748B,color:#0F172A;
    classDef mem fill:#FFEDD5,stroke:#EA580C,color:#7C2D12;
    classDef arch fill:#FCE7F3,stroke:#DB2777,color:#831843;
    classDef proc fill:#E0E7FF,stroke:#4F46E5,color:#312E81;

    class BOSS boss;
    class PLAN plan;
    class BUILD build;
    class CHECK check;
    class SPEC spec;
    class PI,CL,CR cfg;
    class HAND,TASKS,DONE,BUGS,DEC,BACK,DW,DP mem;
    class AF,AUTH,CS arch;
    class SA,CO,PP proc;
```

**How to read it (the story in one pass):** the **Boss** tells the **Planner** what to build. The Planner is set up by its **project-instructions**, reads the **memory** and the **architecture facts** first, follows the **spec-authoring** checklist, and writes a **task spec**. The **Builder** (set up by `CLAUDE.md`) builds from that spec; the **Checker** (set up by `.cursor/rules`) reviews it against the spec's acceptance criteria and reports back. The Boss runtime-tests and signs off, then the Planner does the **close-out** — writing everything that happened back into the **memory**, so the next job starts from a true picture.

**Note:** this maps the *running-system* documents. The onboarding docs — `README`, `SETUP`, `INSTANTIATE`, `teaching/`, and these `diagrams/` — are the "getting started" set and sit outside the loop.

**To have your agent build it:** paste this file (or the fenced block) with "build a diagram from this Mermaid, and keep the colors." Every node, edge, group, and color is encoded — the agent renders rather than infers.

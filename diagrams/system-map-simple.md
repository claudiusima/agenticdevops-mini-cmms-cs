# Diagram source — System Map (SIMPLE / overview)

*The screenshare-friendly overview: the four personas and the five document groups as single boxes — no individual filenames. Use this to show the shape; use `system-map.md` when you want every document named.*

**Legend:** rounded = the human · boxes = agents and document groups.
**Colors (intentional — keep them):** 🟢 green = the Boss · 🔵 blue = Planner · 🟦 teal = Builder · 🟣 purple = Checker · 🟡 yellow = the task spec · ⬜ gray = agent config · 🟠 orange = the memory · 🩷 pink = architecture capture · 🔵 indigo = PM checklists.

```mermaid
flowchart TD
    BOSS(["Boss"])
    CFG["Agent Config"]
    PLAN["Planner<br/>Project Agent · Claude Desktop"]
    BUILD["Builder<br/>Developer Agent · Claude Code"]
    CHECK["Checker<br/>Peer-Review Agent · Cursor"]
    SPEC["Task Spec"]
    MEM["The Memory<br/>living docs"]
    ARCH["Architecture Capture"]
    PROC["PM Checklists"]

    CFG -.sets up.-> PLAN
    CFG -.sets up.-> BUILD
    CFG -.sets up.-> CHECK

    BOSS -->|what to build| PLAN
    MEM -->|read first| PLAN
    ARCH --> PLAN
    PROC --> PLAN
    PLAN -->|writes| SPEC
    SPEC --> BUILD
    BUILD -->|code| CHECK
    CHECK -->|QA result| BOSS
    BOSS -->|sign-off| PLAN
    PLAN -->|close-out| MEM

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
    class CFG cfg;
    class MEM mem;
    class ARCH arch;
    class PROC proc;
```

**How to read it (one pass):** the **Boss** tells the **Planner** what to build. The Planner reads **the memory** first, leans on **architecture capture** and **PM checklists**, and writes a **task spec**. The **Builder** builds it; the **Checker** reviews it; the Boss signs off; the Planner's **close-out** writes everything back into the memory. **Agent config** is what sets up each of the three agents. That's the whole system on one slide.

**The five document groups:** Agent Config · Task Spec · The Memory · Architecture Capture · PM Checklists. (Open `system-map.md` for the full version that names every document inside these groups.)

**To have your agent build it:** paste this file (or the fenced block) with "build a diagram from this Mermaid, and keep the colors."

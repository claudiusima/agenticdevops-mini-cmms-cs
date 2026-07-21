# Diagram source — How to SET UP the workflow (no project → running pipeline)

*Mermaid flowchart mirroring the steps in `SETUP.md`. Renders directly and is clean source for an agent to build a diagram from.*

**Legend:** rounded = start/end · rectangle = a step · diamond = a gate.
**Colors (intentional — keep them):** 🟢 green = start/finish · 🔵 blue = a step you do · 🟠 orange = the load-bearing steps (connect the repo + the two agent prompts) · 🟣 purple = the bootstrap-guided config block · 🟡 yellow = the slot gate.

```mermaid
flowchart TD
    A([Start — new project]) --> S1["1 · Create the repo — 'Use this template'"]
    S1 --> S2["2 · Pull it local"]
    S2 --> S3["3 · Create the Claude project — empty instructions"]
    S3 --> S4["4 · Connect the project to the repo (Filesystem)"]
    S4 --> S5["5 · Setup Prompt — the agent interviews you and drafts the instructions"]
    S5 --> S6["6 · Install the instructions — project field + repo mirror"]
    S6 --> S7["7 · Bootstrap Prompt — the agent finishes Layer B and confirms config"]
    S7 --> P

    subgraph P ["Guided by the Bootstrap Prompt"]
        direction TD
        S8["8 · CLAUDE.md at repo root — Developer Agent"]
        S9["9 · .cursor/rules — Peer-Review Agent"]
        S10["10 · Wire CI"]
        S8 --> S9 --> S10
    end

    P --> G{"11 · Gate: grep for leftover slot markers — any left?"}
    G -- "yes" --> H["Resolve each remaining slot"]
    H --> G
    G -- "clean" --> C2["Delete the worked example; drop onboarding docs you won't keep"]
    C2 --> D([12 · First sprint — pipeline in use])

    classDef term fill:#DCFCE7,stroke:#16A34A,color:#14532D,stroke-width:2px;
    classDef step fill:#DBEAFE,stroke:#2563EB,color:#1E3A8A;
    classDef key fill:#FFEDD5,stroke:#EA580C,color:#7C2D12,stroke-width:2px;
    classDef gate fill:#FEF9C3,stroke:#CA8A04,color:#713F12,stroke-width:2px;
    classDef config fill:#EDE9FE,stroke:#7C3AED,color:#4C1D95;

    class A,D term;
    class S1,S2,S3,S6,H,C2 step;
    class S4,S5,S7 key;
    class S8,S9,S10 config;
    class G gate;
    style P fill:#F5F3FF,stroke:#7C3AED,color:#4C1D95;
```

**Teaching note — the two prompts are the story.** The **Setup Prompt** (step 5) runs *before* the project has instructions: the agent interviews you and **writes its own instructions** by filling the template. The **Bootstrap Prompt** (step 7) runs *after* they're installed: the agent finishes Layer B and the rest of the config. The other orange step (4, connect the repo) is the one people forget — without it the agent can't read the template to do either.

**To have your agent build it:** paste this file (or the fenced block) with "build a flow diagram from this Mermaid, and keep the colors." Structure, branches, and palette are all encoded — the agent renders rather than infers.

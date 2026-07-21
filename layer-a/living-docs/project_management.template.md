# <<PROJECT_NAME>> — Project Management  *(TEMPLATE)*

> Holds the workflow specifics and the **task index**. The task-spec *format* lives in the spec-authoring checklist; this doc holds the index of tasks and the row format for it.

## Task-spec format

Every task gets a spec at `<<TASK_SPEC_PATH_FORMAT>>` (e.g. `docs/tasks/task_<ID>_<slug>.md`), six sections, before any coding-agent command. See `checklists/spec-authoring.checklist.md`.

## Coding-agent command format

```
<<AGENT_CMD_PREFIX>> "Read <<TASK_SPEC_PATH>> in full before writing any code.
[2–4 sentence summary of what to implement, which files, key constraints.]
<<STANDING_INVARIANTS>>"
```

## The task index

**Row format — enforce it, because a readable index is a usable index:**

- One row per task **for its whole lifecycle**. Status transitions **edit the existing row in place** — never append a duplicate.
- Leading status symbol from a fixed set: `<<STATUS_SYMBOLS: e.g. ✅ complete · 🔴 not started · 🟡 in progress · ❄️ deferred>>`.
- Title: soft target ≤`<<N1>>` words, hard cap ≤`<<N2>>` words; single separator (e.g. em-dash); no bold annotations in the title cell.
- Date in the verified column when complete.

| Status | ID | Title | Verified |
|---|---|---|---|
| `<<...>>` | `<<...>>` | `<<...>>` | `<<...>>` |

## Queued / not-yet-specced items

`<<SLOT: the short list of things agreed but not yet turned into specs. Keep it honest — this is not the backlog (that's <<BACKLOG_DOC>>), it's the near-term queue.>>`

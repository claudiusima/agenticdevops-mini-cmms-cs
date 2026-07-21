# <<PROJECT_NAME>> — Agent Handoff  *(TEMPLATE)*

> **Format: always-current. Updated every turn, not end-of-session.** This is the first thing every agent reads. Fill the slots, delete this banner.
>
> **Why it's read first:** it is the single place that answers "where are we right now?" — and the one close-out edit most likely to drift, which is why Rule 16 binds it to the turn. If this file is stale, every session starts misoriented.

## Read me first in any new session

Mandatory before responding to the human:

1. This file — state of play.
2. `<<COMPLETED_DEV_DOC>>` *most-recent entries only* — what just shipped (the reliable ship history).
3. `<<TASK_INDEX_DOC>>` task table — live task status.
4. `<<BUG_LOG_DOC>>` — active bugs.
5. `<<BACKLOG_DOC>>` — prioritized "what's next" + effort estimates.

Then read what's relevant per the Tier-1/Tier-2 list in the project instructions.

## Current state

`<<SLOT: 1–3 short paragraphs. What's the frontier right now? What just shipped, what's in flight (or "nothing in flight — clean"), what's the next real thing. Rewrite this every turn so it names the just-shipped task and the next one — never a prior session's frontier. Historical lessons worth keeping stay as short parentheticals, not fresh narration.>>`

## Immediate next steps

`<<SLOT: the ordered next actions. Keep it to the real forks, not a menu.>>`

## Architecture authorities by area (read the one you're touching)

`<<SLOT: map each area to its authority doc — e.g. "data/persistence → data_model.md", "module boundary → contract doc", "packaging → packaging doc". This is the same content as authority-docs-by-area; point here or restate the short version.>>`

## Standing notes

- **Keep the instructions mirror in sync.** The canonical project instructions live in the Claude Project; a git-tracked mirror lives at `<<INSTRUCTIONS_MIRROR_PATH>>`. When the instructions change, rewrite the mirror in the same turn and bump its "last synced" date. If the two diverge, the Project copy wins.
- **No repo doc is attached to the Claude Project.** Every living doc is read on demand from the repo so it can't go stale. `<<OPTIONAL: record any hard-won lesson about attachments going stale here.>>`
- `<<SLOT: other standing notes unique to this project — rulings not to relitigate, invariants a new session must not rediscover.>>`

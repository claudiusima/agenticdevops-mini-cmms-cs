# <<PROJECT_NAME>> — Development Workflow  *(TEMPLATE)*

> **Why this exists:** CI can only protect the main branch if it runs **before** code lands. That is the whole reason for pull requests here. Branch protection, required approvals, and review ceremony are optional and can be skipped deliberately on a solo/small repo.

## 1. The loop

```
 1. Task spec written     → <<TASK_SPEC_PATH_FORMAT>>            (PM)
 2. Branch cut            → git checkout -b <ID>-<slug>          (human)
 3. Coding agent implements → code + user-docs in the same commit
 4. Review agent QA       → mechanical: typecheck/lint/test + diff vs. acceptance criteria
 5. PM verifies (Rule 7)  → reads the actual changed files
 6. Human runtime-tests   → relaunch first if the changed layer is cached (Rule 14)
 7. PM close-out (Rule 16)→ task-index row, bug log, completed-dev — all one turn
 8. Commit + push branch  → all of the above, one branch
 9. Open PR               → CI runs (see <<DEVOPS_PIPELINE_DOC>>)
10. CI green → self-merge → squash, delete branch
```

**Steps 5–7 happen on the branch, before the PR.** The PM's living-doc edits are **part of the task's commit**, not a separate push. A task whose code merged but whose close-out didn't is the failure Rule 16 exists to prevent.

**Step 6 gates step 7.** Don't write "human-verified" into a close-out before the human has verified. If runtime verification is impossible until a packaged build, say so in the entry rather than implying someone watched it work.

## 2. Branch naming

`<TASK-ID>-<short-slug>`, lowercase. One task per branch; a `-fix1` gets its own branch and PR (keeps the verification story readable).

## 3. Commit messages

```
<TASK-ID>: <what changed, imperative, ≤72 chars>

<optional body: why, not what — the spec already says what>
```

Squash on merge; the squashed message is the one that lasts.

## 4. The pull request

Title mirrors the commit. Body template:

```markdown
**Spec:** <<TASK_SPEC_PATH>>

## What changed
<2–4 sentences.>

## User-facing impact
<One line. "None." is valid. If a user would notice anything, name it AND the
 user-docs updated in this same PR. Same sentence that goes in the close-out entry.>

## Verification
- [ ] PM Rule-7 verified against the actual changed files
- [ ] Human runtime-tested (relaunched first if the changed layer is cached — Rule 14)
- [ ] Close-out landed: task-index row, bug log (if applicable), completed-dev
- [ ] Rule 12: contract docs updated in this PR, or N/A
- [ ] Rule 18: user-docs updated in this PR, or "None." justified above
```

Keep the checklist short. Four boxes get read; twelve get ticked without reading.

## 5. What CI checks

See `<<DEVOPS_PIPELINE_DOC>>` for the authoritative list and the ratchet-promotion criteria.

## 6. Invariants a PR does not soften

`<<SLOT: the handful of never-cross lines for this project — e.g. never modify a user data file; contract docs move in the same commit (Rule 12); user-docs move in the same commit (Rule 18); relaunch before runtime-verifying (Rule 14); generated content is regenerated, never hand-edited.>>`

## 7. Merging

**Squash and merge. Delete the branch.** Self-merge is fine — the reviewer of record is the review agent + the human's runtime test. Branch protection is deliberately off on a solo repo (self-approval is theatre; a required-approval rule you can't satisfy is absurd). What *is* worth enabling once CI has been green a while: **"require status checks to pass before merging"** — converts CI from advice to a gate, costs nothing, can't lock you out.

## 8. When to skip the PR

Rarely, and consciously. **Never** for anything the coding agent wrote (that's the whole point). **Acceptable** for a PM-only living-doc correction with no code. **Not acceptable** for user-docs (it's a promise to users and CI checks it). If you push straight to main, CI still runs on the push — it just tells you afterwards.

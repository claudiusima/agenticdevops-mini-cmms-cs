# <<PROJECT_NAME>> — DevOps Pipeline  *(TEMPLATE)*

> An operational **runbook**: what CI runs, what each guard protects, and the criteria for changing them. Keep this separate from the coding-standards / philosophy doc — anyone asking "what does CI do and why is this check failing?" should land *here*.

## What CI runs

`<<CI_CONFIG_PATH>>` (e.g. `.github/workflows/ci.yml`), on every push to the main branch and every pull request. Runtime: `<<CI_RUNTIME: e.g. Node 24 / Python 3.12 — and WHY this exact version>>`.

| Step | Command | Fails the build? |
|---|---|---|
| Install | `<<INSTALL_CMD>>` | yes |
| `<<OPTIONAL: native-addon rebuild or similar infra step + why>>` | `<<...>>` | yes |
| Typecheck / static | `<<TYPECHECK_CMD>>` | yes |
| Lint | `<<LINT_CMD>>` | yes |
| Test | `<<TEST_CMD>>` | yes |
| Generated-doc freshness | `<<DOCS_CHECK_CMD>>` | yes |
| `<<OPTIONAL: PR-only hard/soft checks>>` | `<<...>>` | `<<yes / no (continue-on-error)>>` |

**Read-only by default.** The workflow requests read-only repo permissions and never requests a write token. See "the drift-detecting agent" below for why that matters.

`<<OPTIONAL: if a build step has a non-obvious environment reality (native compile, ABI mismatch, cross-platform packaging), document the decision and the rejected alternatives here — this is exactly where the CI saga's lessons live so they don't recur.>>`

## What each guard protects

`<<SLOT: one line per check — what real failure it catches. Name the ratchets: a guard that only ever tightens (e.g. an allowlist that only shrinks). See layer-b2/ratchet.scaffold.md.>>`

## Soft checks and the promotion criterion

A check that will produce false positives on day one should start as a **non-blocking reminder** (warns, doesn't fail), or it gets disabled on day two. **Promote it to a hard failure only after it has run clean across real merged PRs** — i.e. every time it fired, the change genuinely warranted the action. Until then it stays advisory.

`<<SLOT: list any soft checks and their promotion criteria.>>`

## The drift-detecting agent — deliberately constrained

A documentation drift-detector may be added later. Its rules are fixed **in advance**, because the temptation to relax them arrives *after* it's useful:

1. **It drafts; a human approves.** It opens a pull request. It **never commits to the main branch**, never pushes, never merges. This is why CI requests no write token — the pipeline is a *checker*, not a *writer*.
2. **Auto-written, unverified docs are worse than missing docs**, because users trust documentation. A wrong page confidently answers with a falsehood. Generated prose never lands without a human reading it first.

If tempted to give CI write access "just to auto-fix the generated pages," don't — regeneration is a local step a human runs and commits; the CI ratchets exist precisely to catch the case where they forgot.

# Contract-Sync — SCAFFOLD (Layer B2)

> The reusable form of **Rule 12**: when a module-boundary contract changes, its documentation and typed surfaces move **in the same commit**. Copy the mapping into your contract doc / spec-authoring checklist, filled for your boundaries.

## The rule

Stale contract docs mean broken code at module boundaries — the failure surfaces at runtime, far from the change, in a different module than the one edited. The only defense that holds is: **the contract, its schema, its typed surface, and its human-readable doc all change together, in one commit.** A spec that changes a contract but not its docs is incomplete and must not ship.

## What counts as a "contract"

Anything two independently-editable parts of the system agree on:

- the interface between processes/services (IPC channels, RPC/REST endpoints, message shapes);
- serialized data schemas (the validation schemas for persisted or transmitted data);
- database migrations / the persisted schema;
- any format one part writes and another reads.

## The mapping — fill it for your project

When a spec changes **X**, it must also update **Y**, in the same commit:

| Change | Must also update (same commit) |
|---|---|
| `<<a boundary channel/endpoint>>` | `<<the typed surface, e.g. the preload/api type>>` + `<<the contract doc>>` |
| `<<a validation schema>>` | `<<its consumers>>` + `<<the schema-authority doc>>` |
| `<<a DB migration / schema change>>` | `<<the data-model doc>>` |
| `<<a serialized/on-disk format>>` | `<<the format's spec doc>>` |
| `<<...>>` | `<<...>>` |

## How the PM enforces it

Spec-authoring checklist has the "contract-doc sync in the same commit" line. The PM lists the required doc edits **in the spec** so the coding agent makes them alongside the code. The review agent can flag a diff that changes a contract with no matching doc change. `<<OPTIONAL: a CI check that fails a contract change with no doc change — see ratchet.scaffold.md.>>`

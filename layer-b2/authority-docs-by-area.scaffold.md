# Authority Docs by Area — SCAFFOLD (Layer B2)

> The index that answers "**before I touch X, which one doc governs it?**" Copy to your repo (often folded into the handoff doc), filled for your areas. For a filled example, see `layer-b1-example/authority-docs-by-area.example.md`.

## Why this exists

A project accumulates area-specific decisions (how the canvas works, how persistence works, how packaging works). If those decisions live only in people's heads or scattered across the log, every spec risks re-deriving — or contradicting — them. This index makes it a one-lookup habit: **read the one authority doc for the area you're about to touch, before you spec it.** It's the operational half of Rule 3.

## The rule of use

- One area → one authority doc. If two docs both claim an area, that's drift — reconcile it and name the winner.
- Read it **before** speccing, not after. Cite it in the spec.
- `<<OPTIONAL: some areas carry a "read §X.Y first — it exists because we already paid for ignoring it" note. Preserve those; they're scar tissue worth keeping.>>`

## The index — fill it

| Area | Authority doc | Read when |
|---|---|---|
| `<<data / persistence>>` | `<<data-model doc>>` | any schema/migration/storage work |
| `<<module boundary>>` | `<<contract doc>>` | any cross-boundary work |
| `<<UI / design>>` | `<<design + UX guides>>` | any UI work |
| `<<packaging / release>>` | `<<packaging doc>>` | any build/signing/installer work |
| `<<each major feature domain>>` | `<<that domain's architecture doc>>` | any work in that domain |
| `<<brand / identity>>` | `<<brand manifest>>` | any brand/icon/packaging-branding work |
| `<<...>>` | `<<...>>` | `<<...>>` |

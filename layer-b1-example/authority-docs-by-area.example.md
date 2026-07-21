# Authority Docs by Area — Acme Notes (WORKED EXAMPLE, read-only)

> Layer B1: a filled example of `authority-docs-by-area.scaffold.md`, for the fictional worked-example product **Acme Notes**. It has a rich domain set, so its index is long — which is exactly why the index earns its keep. Read for shape; don't use.

| Area | Authority doc | Read when |
|---|---|---|
| Calendar domain | `calendar_architecture.md` | any calendar work — **read the "where the analogy stops" section first** |
| Chat-integration domain | `chat_architecture.md` | any chat-integration work |
| Mail domain | `mail_architecture.md` | any mail work (the shared ancestor of the calendar and chat domains) |
| Agent / provider seam | `agent_streaming_architecture.md` | any agent/provider adapter work |
| Canvas / shapes / containers | `canvas_spec.md` | any canvas or diagramming work |
| Persistence | `data_model.md` | any schema / migration / storage work |
| Module boundary | `ipc_contracts.md` | any main↔renderer contract work |
| Packaging / signing | `packaging_spec.md` | any build / installer / code-signing work |
| Brand / identity | `brand_asset_manifest.md` | any brand, app-icon, or packaging-branding work |
| UI visual design | `gui_design_guide.md` | any UI work (tokens, type scale, component patterns) |
| UI behavior | `ux_design_guide.md` | any UI work (destructive confirms, state honesty, header consistency) |

**Notes worth keeping (the scar-tissue kind):**
- The calendar doc's "where the analogy stops" section exists because an earlier feature arc paid for two extra fix rounds by copying a sibling domain's shape past the point it held. The "read this first" note is that lesson, made operational.
- One doc was **retired** and its area folded elsewhere; the index names the successor so nobody reads the dead doc. (When an area's authority moves, the index moves with it — that reconciliation is the index doing its job.)

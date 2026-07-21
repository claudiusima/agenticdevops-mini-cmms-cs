# Key Architecture Facts — Acme Notes (WORKED EXAMPLE, read-only)

> **This is Layer B1: a filled-in example of the `architecture-facts.scaffold.md` pattern**, populated with the constraints of a fictional worked-example product, **Acme Notes** — a local-first desktop notebook app (Electron + React + TypeScript, a SQLite store, a rich-text editor, and a custom canvas). Read it to see what a filled architecture-facts section looks like; **don't use it** — it's an illustration, not your project.

## Process / layer boundaries

**No business logic in the renderer process.** The renderer is presentation only. All persistence, search indexing, file dialogs, and data-file lifecycle happen in the main process and are exposed via typed IPC. No database imports anywhere under the renderer tree. **This is the hardest rule — no exceptions.**

## Canonical data formats

**Rich text is stored as the editor's document JSON.** Never HTML, never Markdown. Markdown input rules and HTML paste are accepted as *input transformations*, but the storage format is always the canonical JSON, round-tripped losslessly.

**Canvas shapes and connectors are data, never SVG/raster.** A shape/connector is a row with a typed content blob; the canvas is re-rendered from that data on every load by a custom SVG/DOM overlay — never a third-party graph library.

## Persistence & migrations

**The data-model doc is the schema authority.** Migrations are numbered, versioned, and **one-way** — there is no rollback path, so they're designed additive and tolerant of older schemas. They run on data-file open.

**The full-text index is derived, never authoritative.** It's rebuilt from the canonical content on save; never written to directly or read as source of truth. If it drifts, rebuild it.

## Module-boundary contracts

**IPC channels are typed end-to-end:** a string name, a validation schema for request and response, a main-process handler that validates, and a typed wrapper in the preload surface. A component never calls the raw IPC primitive — always the preload-exposed API. The preload script is the **only** bridge.

## Security baseline

**Context isolation on; node integration off.** The renderer cannot `require()`. Do not weaken these — baseline desktop-app security.

**Never read, write, delete, or reset a user's data file.** User data files (at any path the user chose) are runtime data; only committed test fixtures may be touched. Stated in every spec.

**Image blobs live in the database, not on disk** — referenced by ID from within the document JSON.

## Styling / brand

**Design tokens only; no raw values.** Every color goes through a semantic token (never a raw palette class); inline styles are reserved for the cataloged exceptions (user-configurable shape colors, runtime-computed drag positions). **Brand is centralized** — reuse the mark component and the brand token; never re-draw the mark inline or hardcode the brand color.

## Testing boundaries

**Unit tests for main-process logic and pure renderer logic; end-to-end tests for user-facing flows in the packaged app.** Don't unit-test IPC — exercise it end-to-end.

---

*Each fact above maps to a numbered decision in the project's decision log. In the real project these are enforced in every spec and form the spine of the coding agent's `CLAUDE.md`.*

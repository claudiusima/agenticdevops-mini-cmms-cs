# CMMess — Functional Specification (v1 / MVP)

> **The product-behavior authority.** This doc says *what CMMess does* — features,
> roles, lifecycles, and what's explicitly out of v1. It sits between
> `docs/user_story.md` (why) and the contract docs (`data-model.md`,
> `api-contract.md`, `uns-contract.md`), which are *derivations* of it. Where this
> doc and `docs/architecture-facts.md` touch the same ground, architecture-facts
> holds the constraint and this doc holds the behavior — they must agree; if they
> don't, that's drift to reconcile, not a license to pick one.
>
> Items marked **[default]** are PM-proposed defaults the Senior Architect has not
> explicitly ruled on — flag any that are wrong. Everything else is decided
> (2026-07-22 unless noted). Genuinely open forks live in § 9.

## 1. Product overview

CMMess is a reactive CMMS for facility maintenance teams: a single shared
multi-user instance with two roles — **Users** (technicians/engineers who execute
work) and **Planners** (managers who plan and schedule it).

The core primitive is the **event-driven work order**: a downtime event on an
asset seeds a work order. There are **two event producers** feeding one pipeline —
the **UNS** (automatic detection via MQTT) and the **front end** (a User or
Planner reports downtime from the UI). In addition, work orders can be **created
directly** (no downtime event at all — e.g., "guard rail loose"). CMMess is
**fully usable with zero UNS connection**: manual asset registration, manual
downtime reporting, and manual work-order creation form a complete standalone
loop (DEC-008). This is a key MVP requirement, not a degraded mode.

```
UNS broker ──┐
             ├─→ downtime event ─→ WO seeded     (origins: uns_downtime, manual_downtime)
Front end ───┤
             └──────────────────→ WO created     (origin: manual)
```

v1 is reactive-only, but nothing may preclude a later preventive/scheduled origin
(e.g., `pm_schedule`) — the origin field is the extension point.

## 2. Roles & permissions

Authorization is enforced server-side per endpoint (DEC-005); the renderer only
shows/hides UI for UX. The matrix below is the behavioral contract every
endpoint's role check implements.

| Capability | User | Planner |
|---|---|---|
| Log in / view own profile | ✓ | ✓ |
| Browse assets, asset detail (status, downtime + WO history) | ✓ | ✓ |
| Register a manual asset | ✓ | ✓ |
| Report a downtime event (asset down) | ✓ | ✓ |
| End a downtime event (asset back up) — manual events | ✓ | ✓ **[default]** |
| Create a work order directly (origin `manual`) | ✓ | ✓ |
| View all work orders | ✓ | ✓ |
| Plan / schedule / assign a work order | ✗ | ✓ |
| Start work on an **Open** (unplanned) WO — self-serve | ✓ | see FS-Q3 |
| Start work on a **Planned** WO | ✓ (assignee) **[default]** | see FS-Q3 |
| Complete a WO (with completion notes) | ✓ (executor) | see FS-Q3 |
| Cancel a WO | ✗ **[default]** | ✓ |
| Edit WO description/details before work starts | creator **[default]** | ✓ |

Decided explicitly: planning/scheduling is Planner-gated but is **not** a gate on
execution — a User can pick up any Open WO and start it (the 3am-breakdown case).

## 3. Assets & the registry

- An **asset** is a generic, configurable entity — never a plant-specific
  equipment table. **Asset identity is its UNS-style path** (e.g.
  `site/area/line/cell/asset`), for every asset regardless of how it was
  registered. One namespace.
- Each asset has a typed **provenance**: `uns_discovered` or `manual`.
  - `uns_discovered`: the UNS is authoritative; the local registry row is a cache
    rebuilt from UNS discovery (DEC-007).
  - `manual`: registered from the front end by a User or Planner; the registry is
    authoritative (DEC-008).
- **Merge rule (DEC-008):** if UNS discovery later finds an asset at the same
  path as a manual asset, they are the same asset — provenance flips to
  `uns_discovered` and all attached history (downtime events, work orders) stays,
  because identity is the path.
- Asset detail shows: current up/down status, downtime history with derived
  durations, and work-order history. Status and duration are always **derived
  from the timestamped event log**, never stored as totals (architecture-facts
  § Derived vs. authoritative).
- Manual registration captures: path, display name, and free-form
  description/metadata **[default — exact fields land in `data-model.md`]**.

## 4. Downtime events

- A downtime event is a pair of timestamped transitions: **down** at t₁, **up**
  at t₂ (t₂ absent while ongoing). Duration is computed, never stored.
- **Producers:** UNS-detected (backend MQTT client observes the down signal) or
  front-end-reported (either role, from the asset's detail view).
- **Seeding:** every downtime event seeds **one** work order automatically at the
  moment the down transition is recorded, with origin `uns_downtime` or
  `manual_downtime` matching the producer, linked to the event. **[default —
  duplicate/overlap policy is FS-Q1/FS-Q2]**
- **Ending:** UNS-detected events end when the UNS up-signal arrives;
  front-end-reported events end when a person marks the asset back up.
  Completing the work order does **not** auto-end the downtime, and ending the
  downtime does not auto-complete the WO — the event log records what the asset
  did; the WO records what people did. **[default]**

## 5. Work orders

**Fields (behavioral level — schema lands in `data-model.md`):** id · asset
(required, any provenance) · origin (`uns_downtime` | `manual_downtime` |
`manual`; typed, extensible) · linked downtime event (present for the two
downtime origins, absent for `manual`) · title + description · priority
(`low`/`medium`/`high` **[default — FS-Q6]**) · `created_by` (the actual person,
or system for UNS-seeded) · `assigned_to` · scheduled window · status ·
completion notes · timestamps per transition.

**State machine (decided):**

```
Open → Planned → In Progress → Completed
  └──────────────────────→ Cancelled (from any non-terminal state)
```

| Transition | Who |
|---|---|
| (seed/create) → Open | system (event pipeline) or either role (manual) |
| Open → Planned | Planner (assign + schedule) |
| Open → In Progress | any User, self-serve |
| Planned → In Progress | assigned User **[default]** |
| In Progress → Completed | the executing User, completion notes required **[default: notes required]** |
| any non-terminal → Cancelled | Planner **[default]** |

- **Open** = seeded/created, unplanned. **Planned** = a Planner has assigned a
  User and/or set a scheduled window. **In Progress** = someone is executing.
  **Completed/Cancelled** = terminal.
- Skipping Planned is normal, not an exception path — reactive work often goes
  Open → In Progress directly.

## 6. Planning & scheduling (Planner)

- The Planner's working view is the queue of **Open** work orders (filter/sort by
  priority, asset, age).
- Planning an order = assigning a User, setting a scheduled window (start
  datetime + expected duration **[default]**), and adjusting priority.
- MVP scheduling is **fields on the work order + list views** — no calendar or
  capacity visualization in v1 **[default — cut, revisit post-MVP]**.

## 7. MVP screen inventory

What exists, not how it looks — `docs/design-guide.md` governs visuals.

1. **Login** — role comes from the account, not a picker.
2. **Asset browser** — the registry as a UNS-path hierarchy; up/down status at a
   glance; entry point for manual asset registration.
3. **Asset detail** — status, downtime history (derived durations), WO history;
   actions: report downtime / mark back up / create WO.
4. **Work-order list** — all WOs, filterable by status/assignee/asset/origin;
   "my work" filter for Users.
5. **Work-order detail** — full record + the role-legal state transitions as
   actions; Planner sees assign/schedule controls here.
6. **Work-order create** — direct manual creation (asset, title, description,
   priority).
7. **Planner queue** — Open WOs awaiting planning (may be the WO list with a
   canned filter rather than a separate screen **[default]**).

## 8. Out of scope for v1

Recorded so their absence reads as decided, not forgotten:

- **Preventive/scheduled maintenance** — excluded, but the origin field, state
  machine, and scheduling fields must not preclude it (the stated extension
  path).
- Notifications (email/push/in-app alerting).
- Reporting/analytics dashboards (MTTR/MTBF etc.) — the derived-from-events model
  is designed to make these computable later.
- Parts/inventory management.
- Attachments/photos on work orders.
- Multi-site/multi-tenant separation — one shared instance.
- Publishing to the UNS — v1 the backend only subscribes **[default — FS-Q8]**.
- Calendar/capacity scheduling views (see § 6).
- User-administration UI (see FS-Q5 for MVP account provisioning).

## 9. Open product questions

Each has a proposed default so work isn't blocked; the Architect's answer
supersedes.

- **FS-Q1 — Duplicate downtime, two producers.** Asset is already down via a UNS
  event and a person also reports it (or vice versa). *Default:* while an asset
  has an ongoing downtime event, a second down-report on it is rejected with a
  pointer to the ongoing event — one ongoing event per asset.
- **FS-Q2 — Repeat downtime while a prior WO is still open.** Asset cycles
  down→up→down with the first WO unresolved. *Default:* each event seeds its own
  WO (the log stays honest); smarter linking/dedup is post-MVP.
- **FS-Q3 — Can Planners execute?** Arch-facts says "Users execute." *Default:*
  Planner role includes User capabilities (a superset) — a Planner can start and
  complete work. If roles should be disjoint, say so.
- **FS-Q4 — Cancel authority.** *Default:* Planner-only (a User abandoning work
  moves it back rather than killing it — exact "abandon" behavior TBD with the
  answer here).
- **FS-Q5 — Account provisioning for MVP.** No admin UI in v1 — how do accounts
  exist? *Default:* seeded/config-file accounts (name, password hash, role) at
  backend startup; no self-signup.
- **FS-Q6 — Priority.** *Default:* keep, three-level enum, default `medium`.
- **FS-Q7 — Manual asset editing/retiring.** Can a manual asset be edited or
  removed after registration, especially once WOs hang off it? *Default:* edit
  display name/description freely; no deletes — retire (hide from browser, keep
  history).
- **FS-Q8 — UNS publishing.** Should CMMess ever publish (e.g., WO status back
  into the namespace)? *Default:* not in v1; subscribe-only.

# Task T-004 — Auth + roles: seeded accounts, sessions, server-side enforcement

## 1. Background

Backend-only (Architect decision 2026-07-22: the renderer login screen is a later task). This lands the security foundation every future endpoint copies: seeded config accounts (FS-Q5), a login/logout/session surface, and the **per-endpoint server-side role-check pattern** (DEC-005 — a hidden button is never access control). Planner ⊇ User (FS-Q3) is encoded here once, in the role dependencies.

Authority docs consulted: `docs/architecture-facts.md` § Security baseline, `docs/functional-spec.md` §§ 2, 8 (FS-Q3/FS-Q5), `docs/data-model.md` (schema authority — this task extends it), `docs/api-contract.md` (grows with the three endpoints), `docs/contract-sync.md` rows 1 and 3, DEC-005/DEC-006.

Session note: dev continues **directly on `main`** (Architect, this session); CI runs post-hoc on push.

## 2. What Already Exists (Do Not Rewrite)

- `backend/app/models.py` — the five T-003 models incl. `users` (username unique, role CHECK, password_hash). Extend via **additive migration**, don't restructure.
- `backend/app/config.py` / `db.py` — env-driven config, lazy engine, SQLite FK pragma. Extend the same patterns.
- `backend/alembic/` — env wired, `0001_initial_schema`. Add `0002`, never edit `0001`.
- `backend/app/main.py` — `GET /health` stays **unauthenticated** and must keep passing its test.
- The renderer and `ci.yml` — untouched.

## 3. What to Build

### 3a. Migration `0002` (additive, dual-engine — both legs move with `docs/data-model.md`, Rule 12)

1. `users.active` — bool, not null, server_default true. Why: seeded-config revocation — an account removed from the config must stop logging in, while its row (referenced by history FKs) is never deleted.
2. **`sessions`** — id PK · `token_hash` str(64) unique not null (SHA-256 hex of the raw token — the raw token is never stored) · `user_id` FK→users not null · `created_at`, `expires_at` datetime(UTC) not null. Same portability rules as 0001 (no dialect SQL).

### 3b. Account seeding (FS-Q5)

- Config: TOML at `CMMESS_USERS_FILE` (default `backend/config/users.toml` — **gitignored**; commit `backend/config/users.example.toml` with two example accounts and a comment header explaining the flow). Each entry: `username`, `password_hash` (bcrypt), `role` (`user`|`planner`). Parse with stdlib `tomllib`.
- Seeding runs in the FastAPI **lifespan** (startup): upsert by username (create missing; update role/hash to match config; reactivate if present), and **deactivate** any user in the DB that is absent from the config. Never delete rows. If the schema isn't migrated, fail startup with a clear operator message ("run `alembic upgrade head`") — importing the app still touches nothing (T-003 invariant; only *startup* seeds).
- Hash helper: `python -m app.hash_password` prompts for a password (no echo) and prints the bcrypt hash — hash generation only, not account management. Dependency: `bcrypt>=4`.

### 3c. Auth surface + enforcement pattern (`backend/app/auth.py`, wired into `main.py`)

- `POST /auth/login` — `{username, password}` → 200 `{token, user: {id, username, role}}`. Verify bcrypt; reject inactive users. **All failures return the same generic 401** (no username enumeration). Token: `secrets.token_urlsafe(32)`; store only its SHA-256; expiry now + `CMMESS_SESSION_TTL_HOURS` (default 24).
- `POST /auth/logout` — authenticated; deletes the session; 204.
- `GET /auth/me` — authenticated; → `{id, username, role}`. The protected-endpoint exemplar.
- **Role dependencies — the pattern every future endpoint uses:** `require_user` (any valid session whose user is active — both roles) and `require_planner` (planner only; FS-Q3: Planner ⊇ User means planner passes both). Bearer token via `Authorization: Bearer <token>`. Missing/invalid/expired token or inactive user → 401; valid session, wrong role → 403. Expired/orphaned sessions are treated as invalid on read (no background sweeper in v1).
- All request/response shapes through typed Pydantic models. Never log passwords, hashes, or tokens.

### 3d. Tests (`backend/tests/test_auth.py`) — integration against a migrated tmp DB with a seeded tmp config (env-overridden paths; never `backend/data/` or a real config)

Properties to prove: login happy path (token works on `/auth/me`) · wrong password and unknown username → identical 401 bodies · inactive user (removed from config, re-seeded) can no longer log in, and their existing session stops working · logout revokes (the token 401s after) · expired session 401s (insert one with past `expires_at`) · `require_planner` 403s a `user`-role session and passes a `planner` one (exercised via a minimal planner-gated route on a test app if no production route fits) · `/health` still works with no auth · re-seeding is idempotent and updates a changed role/hash.

### 3e. Contract + docs (same commit — Rule 12)

- `docs/api-contract.md` — new **Auth** section: the bearer scheme, the three endpoints (request/response models, error semantics 401/403), and a note that `require_user`/`require_planner` are the enforcement pattern for all future protected endpoints. TypeScript leg: **N/A this task** (backend-only; the renderer login task will add the TS types).
- `docs/data-model.md` — `sessions` table + `users.active`, and the seeding/revocation semantics, moved with migration 0002.
- `.gitignore` — `backend/config/users.toml`.

## 4. Acceptance Criteria

From `backend/` in a fresh venv (the coding agent changes no files outside §5):

- [ ] `pip install`, `ruff check .`, `mypy .` (strict, no carve-outs), `pytest` all clean; `test_health`, T-003 tests still pass.
- [ ] `alembic upgrade head` from a fresh DB and from an existing 0001 DB both succeed (0002 is additive); no dialect-specific SQL; the env-gated Postgres test still passes when a URL is provided.
- [ ] Every §3d property is proven by a test, including the identical-401 (no-enumeration) check and session revocation on deactivation.
- [ ] Raw tokens and passwords never appear in the DB, logs, or error bodies (tokens stored only as SHA-256; bcrypt for passwords).
- [ ] `/health` remains unauthenticated; importing the app touches no storage; startup without a migrated schema fails with the operator message.
- [ ] `docs/api-contract.md` and `docs/data-model.md` updated in the same commit as the code (Rule 12); `users.example.toml` committed; real config path gitignored.

## 5. Files to Modify

- `backend/app/auth.py` (new) · `backend/app/seeding.py` (new) · `backend/app/hash_password.py` (new, `__main__`-runnable)
- `backend/app/main.py` (edit: router + lifespan) · `backend/app/config.py` (edit: users-file + TTL settings) · `backend/app/models.py` (edit: `active` column, `Session` model)
- `backend/alembic/versions/0002_auth_sessions.py` (new)
- `backend/tests/test_auth.py` (new)
- `backend/config/users.example.toml` (new) · `backend/requirements.txt` (edit: +bcrypt) · `.gitignore` (edit)
- `docs/api-contract.md` (edit, same commit) · `docs/data-model.md` (edit, same commit)

## 6. Coding-Agent Instructions

Read this spec file (`docs/tasks/task_T-004_auth-roles.md`) in full before writing any code. Work directly on `main`.

Implement backend auth per §3: additive migration 0002 (`users.active`, `sessions` with hashed tokens), TOML account seeding in the lifespan with upsert-and-deactivate semantics, `POST /auth/login` / `POST /auth/logout` / `GET /auth/me` with opaque bearer tokens (SHA-256 at rest, TTL via `CMMESS_SESSION_TTL_HOURS`), and the `require_user`/`require_planner` dependencies as the standing enforcement pattern (Planner passes both). Generic 401s on login failure; 401 invalid/expired/inactive, 403 wrong role. Integration tests against migrated tmp DBs + tmp configs prove every §3d property. Update `docs/api-contract.md` and `docs/data-model.md` in the same commit (Rule 12). No renderer changes, no domain endpoints, no MQTT.

Hard constraints decided by this spec:

- **Silencer decision:** none expected; stop and flag the PM if one arises.
- **Database safety (CLAUDE.md):** tests touch only tmp databases and tmp config files — never `backend/data/` or a real users config.
- **Secrets:** bcrypt for passwords, SHA-256-at-rest for tokens, nothing secret in logs or error bodies; no secrets in code (env/config only).
- **Rule 12:** contract surfaces moving with this commit = REST (api-contract.md) + schema (data-model.md). TS leg N/A — backend-only by Architect decision.
- **User-facing impact:** None — no user-visible surface yet (the renderer login task delivers it).

Standing invariants: honor docs/architecture-facts.md and CLAUDE.md; the renderer holds no business logic, DB, or MQTT/UNS access; authorization is enforced server-side; keep contract docs (Rule 12) and user-docs (Rule 18) in the same commit; migrations run on both SQLite and Postgres; never read/write/delete data outside the app's own store; backend gate: install, ruff, mypy, pytest, and app import all clean from `backend/`.

# API Contract — CMMess

> The authority for the renderer↔backend REST surface. Per `docs/contract-sync.md`,
> any endpoint/schema change moves its Pydantic model, its TypeScript type, and this
> doc **in the same commit** (Rule 12). No renderer exists yet, so the TypeScript leg
> is N/A until the renderer lands.

## Endpoints

### GET /health

- **Path:** `/health`
- **Method:** `GET`
- **Auth:** none
- **Response model:** `HealthResponse` (`backend/app/main.py`) — `status: Literal["ok"]`
- **Example response (200):**

  ```json
  {"status": "ok"}
  ```

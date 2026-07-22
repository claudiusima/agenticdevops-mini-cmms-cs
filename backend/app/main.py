"""CMMess backend — FastAPI application entry point."""

from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Response model for GET /health."""

    status: Literal["ok"]


app = FastAPI(title="CMMess Backend")


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    """Liveness check. No auth."""
    return HealthResponse(status="ok")

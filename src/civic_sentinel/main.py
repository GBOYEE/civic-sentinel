"""CivicSentinel — Production FastAPI gateway."""
import os
import time
import uuid
import logging
from typing import Dict

from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from .routers import documents, analysis

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)
logger = logging.getLogger("civic_sentinel")

# Settings
APP_VERSION = "0.1.0"
ENV = os.getenv("CIVIC_ENV", "production")

# Metrics store (in-memory; use Redis in production)
metrics_store: Dict[str, int] = {
    "requests_total": 0,
    "requests_failed": 0,
    "documents_uploaded": 0,
    "analyses_run": 0,
}

def create_app() -> FastAPI:
    app = FastAPI(
        title="CivicSentinel",
        version=APP_VERSION,
        description="AI-powered public policy analysis",
    )

    @app.middleware("http")
    async def logging_middleware(request: Request, call_next):
        request_id = str(uuid.uuid4())[:8]
        request.state.request_id = request_id

        start_time = time.time()
        metrics_store["requests_total"] += 1

        try:
            response = await call_next(request)
            elapsed = time.time() - start_time
            logger.info(
                "request completed",
                extra={
                    "request_id": request_id,
                    "method": request.method,
                    "path": request.url.path,
                    "status_code": response.status_code,
                    "duration_ms": int(elapsed * 1000),
                }
            )
            response.headers["X-Request-ID"] = request_id
            return response
        except Exception as exc:
            metrics_store["requests_failed"] += 1
            logger.error(
                "request failed",
                extra={
                    "request_id": request_id,
                    "method": request.method,
                    "path": request.url.path,
                    "error": str(exc),
                },
                exc_info=True
            )
            raise

    @app.get("/health")
    async def health():
        """Health check."""
        return {
            "status": "ok",
            "timestamp": time.time(),
            "version": APP_VERSION,
            "environment": ENV,
        }

    @app.get("/metrics")
    async def metrics():
        """Expose internal metrics."""
        return metrics_store

    # Include routers
    app.include_router(documents.router, prefix="/api/v1")
    app.include_router(analysis.router, prefix="/api/v1")

    # CORS — permissive for now, tighten in prod
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "src.civic_sentinel.main:app",
        host="0.0.0.0",
        port=int(os.getenv("CIVIC_PORT", 8000)),
        reload=ENV == "development",
    )

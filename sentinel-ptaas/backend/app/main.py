import time

import structlog
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api.routes import assets, auth, integrations, reports, scans, users, vulnerabilities
from app.core.config import settings
from app.db.session import Base, engine

Base.metadata.create_all(bind=engine)
logger = structlog.get_logger()

app = FastAPI(title=settings.app_name)


@app.middleware("http")
async def audit_log_middleware(request: Request, call_next):
    started = time.time()
    response = await call_next(request)
    logger.info(
        "request.completed",
        method=request.method,
        path=request.url.path,
        status_code=response.status_code,
        elapsed_ms=round((time.time() - started) * 1000, 2),
    )
    return response


@app.exception_handler(Exception)
async def unhandled_exception(_: Request, exc: Exception):
    logger.exception("unhandled.error", error=str(exc))
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})


app.include_router(auth.router, prefix=settings.api_prefix)
app.include_router(assets.router, prefix=settings.api_prefix)
app.include_router(vulnerabilities.router, prefix=settings.api_prefix)
app.include_router(scans.router, prefix=settings.api_prefix)
app.include_router(reports.router, prefix=settings.api_prefix)
app.include_router(integrations.router, prefix=settings.api_prefix)
app.include_router(users.router, prefix=settings.api_prefix)


@app.get("/health")
def healthcheck():
    return {"status": "ok", "service": settings.app_name}

import time
import logging
from fastapi import Request

logger = logging.getLogger("app.middleware")


async def request_logger(request: Request, call_next):
    start = time.perf_counter()
    try:
        response = await call_next(request)
        return response
    finally:
        duration_ms = (time.perf_counter() - start) * 1000
        logger.info(
            "%s %s -> %s in %.2fms",
            request.method,
            request.url.path,
            getattr(
                getattr(locals().get("response"), "status_code", None),
                "__str__",
                lambda: "?",
            )(),
            duration_ms,
        )

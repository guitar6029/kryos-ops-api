from fastapi import FastAPI, Request
from app.routers.operators import router as operators_router
from app.routers.health import router as health_router
from app.routers.devices import router as devices_router
from app.middleware.request_logger import request_logger

app = FastAPI()


@app.middleware("http")
async def _request_logger(request: Request, call_next):
    return await request_logger(request, call_next)


@app.get("/")
async def root():
    return {"status": "Kryos Ops - ok"}


@app.get("/health/{service}")
async def health_check(service: str, verbose: bool = False):
    return {"service": service, "status": "ok", "verbose": verbose}


app.include_router(operators_router)
app.include_router(health_router)
app.include_router(devices_router)

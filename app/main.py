from fastapi import FastAPI
from app.routers.operators import router as operators_router
from app.routers.health import router as health_router

app = FastAPI()


@app.get("/")
async def root():
    return {"status": "Kryos Ops - ok"}


@app.get("/health/{service}")
async def health_check(service: str, verbose: bool = False):
    return {"service": service, "status": "ok", "verbose": verbose}


app.include_router(operators_router)
app.include_router(health_router)

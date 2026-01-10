from fastapi import FastAPI
from app.schemas.operator import OperatorCreate

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "Kryos Ops - ok"}

@app.get("/health/{service}")
async def health_check(service: str, verbose: bool = False):
    return {
        "service": service,
        "status": "ok",
        "verbose": verbose
    }

@app.post("/operators")
async def create_operator(payload: OperatorCreate):
    return {"created" : payload}
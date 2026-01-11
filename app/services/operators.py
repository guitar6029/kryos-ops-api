from app.schemas.operator import OperatorCreate, OperatorResponse

# fake db for now
_next_id = 1


async def create_operator(payload: OperatorCreate) -> OperatorResponse:
    global _next_id

    # business rules
    if payload.codename.lower() == "admin":
        raise ValueError("Invalid Codename")

    # if ok
    created = OperatorResponse(
        id=_next_id,
        codename=payload.codename,
        clearance=payload.clearance,
        active=payload.active,
    )
    _next_id += 1
    return created

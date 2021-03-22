import json
from fastapi import APIRouter, HTTPException

from app.schemas.fibonacci import Fibonacci


router = APIRouter()


@router.post("/fibonacci/", status_code=200)
async def fibonacci_calculate(*, payload: Fibonacci):
    if payload.number < 0:
        raise HTTPException(status_code=422, detail="Numbers must be at least 0")
    if payload.number == 0:
        return json.dumps([0])

    fib_list: list = [0, 1]

    for i in range(2, payload.number + 1):
        fib_list.append(fib_list[-1] + fib_list[-2])

    return json.dumps(fib_list)

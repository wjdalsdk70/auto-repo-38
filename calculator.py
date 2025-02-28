# calculator_api/app/routers/calculator.py
from fastapi import APIRouter, HTTPException
from app.models import Calculation, CalculationResult
from typing import Union

router = APIRouter(prefix="/calculator", tags=["calculator"])

@router.post("/", response_model=CalculationResult)
async def calculate(calculation: Calculation):
    try:
        if calculation.operation == "+":
            result = calculation.num1 + calculation.num2
        elif calculation.operation == "-":
            result = calculation.num1 - calculation.num2
        elif calculation.operation == "*":
            result = calculation.num1 * calculation.num2
        elif calculation.operation == "/":
            if calculation.num2 == 0:
                raise ZeroDivisionError("Division by zero")
            result = calculation.num1 / calculation.num2
        else:
            raise ValueError("Invalid operation")
        return {"result": result}
    except (ZeroDivisionError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))
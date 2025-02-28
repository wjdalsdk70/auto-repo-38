# calculator_api/app/models.py
from pydantic import BaseModel

class Calculation(BaseModel):
    num1: float
    num2: float
    operation: str

class CalculationResult(BaseModel):
    result: float
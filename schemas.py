from pydantic import BaseModel, field_validator


class GetIDSchema(BaseModel):

    operator: str
    x: int
    y: int

    @field_validator('operator')
    @classmethod
    def validate_operator(cls, v: str) -> str:
        valid_operators = '+-*/'
        # valid_operators = ["+", "-", "*", "/"]
        if v not in valid_operators:
            raise ValueError("Недопустимый оператор")
        return v

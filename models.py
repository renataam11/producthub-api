from typing import Annotated
from pydantic import BaseModel, Field, StringConstraints

class Product(BaseModel):
    name: Annotated[
        str,
        StringConstraints(strip_whitespace=True, min_length=1)
    ]
    price: float = Field(gt=0)
    stock: int = Field(ge=0)


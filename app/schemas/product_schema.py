from pydantic import BaseModel, Field
from typing import List, Optional


class Address(BaseModel):
    city: str
    pincode: int


class Product(BaseModel):
    id: int
    name: str = Field(min_length=3)
    price: float = Field(gt=0)
    address: Address
    products: Optional[List[str]] = None
from pydantic import BaseModel, Field
from typing import List, Optional


class Address(BaseModel):
    city: str
    pincode: int


class User(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(gt=0)
    address: Address = Field(min_length=3)
    hobbies: Optional[List[str]] = None
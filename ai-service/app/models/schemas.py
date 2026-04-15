from pydantic import BaseModel
from typing import List

class ProductRequest(BaseModel):
    name: str
    description: str = ""
    reviews: List[str] = []
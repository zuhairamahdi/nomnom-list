from pydantic import BaseModel
from typing import List
from app.schemas.item import ItemOut
class ListCreate(BaseModel):
    name: str

class ListOut(BaseModel):
    id: int
    name: str
    items: List[ItemOut] = []
    class Config:
        orm_mode = True

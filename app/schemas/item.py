from pydantic import BaseModel
class ItemCreate(BaseModel):
    name: str
    quantity: str

class ItemOut(ItemCreate):
    id: int
    is_checked: bool
    class Config:
        orm_mode = True

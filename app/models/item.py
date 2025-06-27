from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    quantity = Column(String)
    is_checked = Column(Boolean, default=False)
    list_id = Column(Integer, ForeignKey("grocery_lists.id"))

    list = relationship("GroceryList", back_populates="items")

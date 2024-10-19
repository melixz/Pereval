from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base

class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(String, nullable=False)
    title = Column(String, nullable=True)
    item_id = Column(Integer, ForeignKey("items.id"))

    item = relationship("Item", back_populates="images")

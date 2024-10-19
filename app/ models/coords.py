from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.base_class import Base


class Coords(Base):
    __tablename__ = "coords"

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(String, nullable=False)
    longitude = Column(String, nullable=False)
    height = Column(String, nullable=True)

    items = relationship("Item", back_populates="coords")

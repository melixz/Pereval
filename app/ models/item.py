from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    beauty_title = Column(String, nullable=True)
    title = Column(String, nullable=False)
    other_titles = Column(String, nullable=True)
    connect = Column(String, nullable=True)
    add_time = Column(DateTime, nullable=True)
    status = Column(String, default="new")
    user_id = Column(Integer, ForeignKey("users.id"))
    coords_id = Column(Integer, ForeignKey("coords.id"))
    level_id = Column(Integer, ForeignKey("levels.id"))

    user = relationship("User", back_populates="items")
    coords = relationship("Coords", back_populates="items")
    level = relationship("Level", back_populates="items")
    images = relationship("Image", back_populates="item")

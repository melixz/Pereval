from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.base_class import Base


class Level(Base):
    __tablename__ = "levels"

    id = Column(Integer, primary_key=True, index=True)
    winter = Column(String, nullable=True)
    summer = Column(String, nullable=True)
    autumn = Column(String, nullable=True)
    spring = Column(String, nullable=True)

    items = relationship("Item", back_populates="level")

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.base_class import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    fam = Column(String, nullable=True)
    name = Column(String, nullable=True)
    otc = Column(String, nullable=True)
    phone = Column(String, nullable=True)

    items = relationship("Item", back_populates="user")

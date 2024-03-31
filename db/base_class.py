from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

Base = declarative_base()


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    beauty_title = Column(String)
    title = Column(String)
    other_titles = Column(String)
    connect = Column(String)
    add_time = Column(DateTime)
    status = Column(String, default='new')  # Добавленное поле status
    user_id = Column(Integer, ForeignKey('users.id'))
    coords_id = Column(Integer, ForeignKey('coords.id'))
    level_id = Column(Integer, ForeignKey('levels.id'))

    user = relationship("User", back_populates="items")
    coords = relationship("Coords", back_populates="items")
    level = relationship("Level", back_populates="items")
    images = relationship("Image", back_populates="item")


class RequestModel(BaseModel):
    beauty_title: Optional[str] = None
    title: Optional[str] = None
    other_titles: Optional[str] = None
    connect: Optional[str] = None
    add_time: Optional[datetime] = None
    status: Optional[str] = None
    coords_id: Optional[int] = None
    level_id: Optional[int] = None
    # Поле user_id исключено, т.к. не должно редактироваться через этот API
    # Поле images исключено из модели, т.к. требует отдельной логики для обработки связей

    class Config:
        orm_mode = True


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    fam = Column(String)
    name = Column(String)
    otc = Column(String)
    phone = Column(String)

    items = relationship("Item", back_populates="user")


class Coords(Base):
    __tablename__ = 'coords'

    id = Column(Integer, primary_key=True)
    latitude = Column(String)
    longitude = Column(String)
    height = Column(String)

    items = relationship("Item", back_populates="coords")


class Level(Base):
    __tablename__ = 'levels'

    id = Column(Integer, primary_key=True)
    winter = Column(String)
    summer = Column(String)
    autumn = Column(String)
    spring = Column(String)

    items = relationship("Item", back_populates="level")


class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    data = Column(String)
    title = Column(String)
    item_id = Column(Integer, ForeignKey('items.id'))

    item = relationship("Item", back_populates="images")


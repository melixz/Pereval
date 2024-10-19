from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class UserBase(BaseModel):
    email: str
    fam: Optional[str] = None
    name: Optional[str] = None
    otc: Optional[str] = None
    phone: Optional[str] = None

    class Config:
        from_attributes = True


class CoordsBase(BaseModel):
    latitude: str
    longitude: str
    height: Optional[str] = None

    class Config:
        from_attributes = True


class LevelBase(BaseModel):
    winter: Optional[str] = None
    summer: Optional[str] = None
    autumn: Optional[str] = None
    spring: Optional[str] = None

    class Config:
        from_attributes = True


class ImageBase(BaseModel):
    data: str
    title: Optional[str] = None

    class Config:
        from_attributes = True


class ItemBase(BaseModel):
    beauty_title: Optional[str] = None
    title: str
    other_titles: Optional[str] = None
    connect: Optional[str] = None
    add_time: Optional[datetime] = None
    status: Optional[str] = "new"
    user: Optional[UserBase] = None
    coords: Optional[CoordsBase] = None
    level: Optional[LevelBase] = None
    images: List[ImageBase] = []

    class Config:
        from_attributes = True


# Модель для PATCH запроса (частичное обновление)
class RequestModel(BaseModel):
    beauty_title: Optional[str] = None
    title: Optional[str] = None
    other_titles: Optional[str] = None
    connect: Optional[str] = None
    add_time: Optional[datetime] = None
    status: Optional[str] = None
    user_id: Optional[int] = None
    coords_id: Optional[int] = None
    level_id: Optional[int] = None

    class Config:
        from_attributes = True

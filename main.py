import os
import uvicorn
from fastapi import FastAPI, __version__
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from datetime import datetime
from db.session import ItemService
from typing import List, Optional
from time import time


app = FastAPI()
item_service = ItemService()

html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>FastAPI</title>
    </head>
    <body>
        <h1>Hello from PerevalAPI@{__version__}</h1>
        <ul>
            <li><a href="/docs">/docs</a></li>
            <li><a href="/redoc">/redoc</a></li>
        </ul>
    </body>
</html>
"""


# Модель для User
class UserBase(BaseModel):
    email: str
    fam: Optional[str] = None
    name: Optional[str] = None
    otc: Optional[str] = None
    phone: Optional[str] = None

    class Config:
        from_attributes = True


# Модель для Coords
class CoordsBase(BaseModel):
    latitude: str
    longitude: str
    height: Optional[str] = None

    class Config:
        from_attributes = True


# Модель для Level
class LevelBase(BaseModel):
    winter: Optional[str] = None
    summer: Optional[str] = None
    autumn: Optional[str] = None
    spring: Optional[str] = None

    class Config:
        from_attributes = True


# Модель для Image
class ImageBase(BaseModel):
    data: str
    title: Optional[str] = None

    class Config:
        from_attributes = True


# Модель для Item, включающая в себя связи
class ItemBase(BaseModel):
    beauty_title: Optional[str] = None
    title: str
    other_titles: Optional[str] = None
    connect: Optional[str] = None
    add_time: Optional[datetime] = None
    status: Optional[str] = 'new'
    user_id: Optional[int] = None
    coords_id: Optional[int] = None
    level_id: Optional[int] = None

    # Возможно, вам понадобится включить связанные объекты как подмодели
    user: Optional[UserBase] = None
    coords: Optional[CoordsBase] = None
    level: Optional[LevelBase] = None
    images: List[ImageBase] = []

    class Config:
        from_attributes = True


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
        from_attributes = True
# Модель для создания Item, если требуется


class ItemCreate(ItemBase):
    pass


# Модель для ответа, содержащая полный набор данных, включая id
class ItemResponse(ItemBase):
    id: int


@app.post("/submitData/")
async def submit_data(item: ItemBase):
    item_service.add_item(item)
    return {"message": "Data submitted successfully"}


@app.put("/items/{item_id}/status/{status}")
async def update_moderation_status(item_id: int, status: str):
    allowed_statuses = ['new', 'pending', 'accepted', 'rejected']
    if status not in allowed_statuses:
        return {"error": "Invalid status value"}
    try:
        item_service.set_moderation_status(item_id, status)
        return {"message": "Moderation status updated successfully"}
    except ValueError as e:
        return {"error": str(e)}


@app.get("/submitData/{item_id}")
async def get_item(item_id: int):
    try:
        item = item_service.get_item(item_id)
        return item
    except ValueError as e:
        return {"error": str(e)}


@app.patch("/submitData/{item_id}")
async def edit_item(item_id: int, item: RequestModel):
    try:
        state, message = item_service.edit_item(item_id, item)
        return {"state": state, "message": message}
    except Exception as e:  # Используйте более конкретное исключение, если возможно
        return {"state": 0, "message": str(e)}


@app.get("/submitData/")
async def get_items_by_user_email(user__email: Optional[str] = None):
    if user__email:
        items = item_service.get_items_by_user_email(user__email)
        return items
    else:
        return {"error": "Email is required"}


@app.get("/")
async def root():
    return HTMLResponse(html)


@app.get('/ping')
async def hello():
    return {'res': 'pong', 'version': __version__, "time": time()}


if __name__ == "__main__":
    port = os.getenv("PORT") or 8001
    uvicorn.run(app, host="127.0.0.1", port=int(port))



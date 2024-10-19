from fastapi import APIRouter, Depends
from app.models.pydantic_models import ItemBase, RequestModel
from app.services.item_service import ItemService
from sqlalchemy.orm import Session
from db.session import get_db
from typing import Optional

router = APIRouter(prefix="/api", tags=["Items"])


# Отправка данных
@router.post("/submitData/")
async def submit_data(item: ItemBase, db: Session = Depends(get_db)):
    service = ItemService(db)
    service.add_item(item)
    return {"message": "Data submitted successfully"}


# Обновление статуса модерации
@router.put("/items/{item_id}/status/{status}")
async def update_moderation_status(
    item_id: int, status: str, db: Session = Depends(get_db)
):
    service = ItemService(db)
    service.set_moderation_status(item_id, status)
    return {"message": "Status updated"}


# Получение элемента по ID
@router.get("/submitData/{item_id}")
async def get_item(item_id: int, db: Session = Depends(get_db)):
    service = ItemService(db)
    item = service.get_item(item_id)
    return item


# Получение всех элементов по email пользователя
@router.get("/submitData/")
async def get_items_by_user_email(
    user_email: Optional[str] = None, db: Session = Depends(get_db)
):
    if user_email:
        service = ItemService(db)
        items = service.get_items_by_user_email(user_email)
        return items
    return {"error": "Email is required"}


# Редактирование элемента, если его статус 'new'
@router.patch("/submitData/{item_id}")
async def edit_item(item_id: int, item: RequestModel, db: Session = Depends(get_db)):
    service = ItemService(db)
    state, message = service.edit_item(item_id, item)
    return {"state": state, "message": message}

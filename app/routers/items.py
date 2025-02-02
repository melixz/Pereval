from fastapi import APIRouter, Depends
from app.models.pydantic_models import ItemBase, RequestModel
from app.services.item_service import ItemService
from sqlalchemy.orm import Session
from db.session import get_db
from typing import Optional

router = APIRouter(prefix="/api", tags=["Items"])


@router.post("/submitData/", summary="Отправка данных")
async def submit_data(item: ItemBase, db: Session = Depends(get_db)):
    """
    Отправка нового элемента в базу данных.
    """
    service = ItemService(db)
    service.add_item(item)
    return {"message": "Data submitted successfully"}


@router.put("/items/{item_id}/status/{status}", summary="Обновление статуса модерации")
async def update_moderation_status(
    item_id: int, status: str, db: Session = Depends(get_db)
):
    """
    Обновление статуса модерации для элемента по его ID.
    """
    service = ItemService(db)
    service.set_moderation_status(item_id, status)
    return {"message": "Status updated"}


@router.get("/submitData/{item_id}", summary="Получение элемента по ID")
async def get_item(item_id: int, db: Session = Depends(get_db)):
    """
    Получение элемента по ID.
    """
    service = ItemService(db)
    item = service.get_item(item_id)
    return item


@router.get("/submitData/", summary="Получение всех элементов по email пользователя")
async def get_items_by_user_email(
    user_email: Optional[str] = None, db: Session = Depends(get_db)
):
    """
    Получение всех элементов по email пользователя.
    """
    if user_email:
        service = ItemService(db)
        items = service.get_items_by_user_email(user_email)
        return items
    return {"error": "Email is required"}


@router.patch("/submitData/{item_id}", summary="Редактирование элемента")
async def edit_item(item_id: int, item: RequestModel, db: Session = Depends(get_db)):
    """
    Редактирование элемента по ID, если его статус 'new'.
    """
    service = ItemService(db)
    state, message = service.edit_item(item_id, item)
    return {"state": state, "message": message}

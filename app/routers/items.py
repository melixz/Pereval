from fastapi import APIRouter, Depends
from app.models.item import ItemBase
from app.services.item_service import ItemService
from sqlalchemy.orm import Session
from db.session import get_db

router = APIRouter(
    prefix="/api",
    tags=["Items"]
)

@router.post("/submitData/")
async def submit_data(item: ItemBase, db: Session = Depends(get_db)):
    service = ItemService(db)
    service.add_item(item)
    return {"message": "Data submitted successfully"}

@router.put("/items/{item_id}/status/{status}")
async def update_moderation_status(item_id: int, status: str, db: Session = Depends(get_db)):
    service = ItemService(db)
    service.set_moderation_status(item_id, status)
    return {"message": "Status updated"}

@router.get("/submitData/{item_id}")
async def get_item(item_id: int, db: Session = Depends(get_db)):
    service = ItemService(db)
    item = service.get_item(item_id)
    return item

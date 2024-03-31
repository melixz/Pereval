import uvicorn
from fastapi import FastAPI
from db.base_class import Item
from db.session import ItemService
from typing import Optional
from db.base_class import RequestModel



app = FastAPI()
item_service = ItemService()


@app.post("/submitData/")
async def submit_data(item: Item):
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


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)



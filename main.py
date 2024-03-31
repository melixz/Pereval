from fastapi import FastAPI
from db.base_class import Item
from db.session import ItemService
import uvicorn

app = FastAPI()
item_service = ItemService()

@app.post("/submitData/")
async def submit_data(item: Item):
    item_service.add_item(item)
    return {"message": "Data submitted successfully"}


@app.get("/submitData/{id}")
async def get_data(id: int):
    try:
        data = item_service.get_data_by_id(id)
        return data
    except ValueError as e:
        return {"error": str(e)}


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


@app.get("/items/{item_id}/status")
async def get_moderation_status(item_id: int):
    try:
        status = item_service.get_moderation_status(item_id)
        return {"status": status}
    except ValueError as e:
        return {"error": str(e)}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)



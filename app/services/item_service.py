from sqlalchemy.orm import Session
from app.models.item import Item
from app.models.user import User
from app.models.coords import Coords
from app.models.level import Level
from app.models.image import Image
from fastapi import HTTPException


class ItemService:
    def __init__(self, db: Session):
        self.db = db

    def add_item(self, item_data):
        user = User(**item_data.user.dict())
        coords = Coords(**item_data.coords.dict())
        level = Level(**item_data.level.dict())
        images = [Image(**image.dict()) for image in item_data.images]

        item = Item(
            beauty_title=item_data.beauty_title,
            title=item_data.title,
            other_titles=item_data.other_titles,
            connect=item_data.connect,
            add_time=item_data.add_time,
            user=user,
            coords=coords,
            level=level,
            images=images,
        )

        self.db.add(item)
        self.db.commit()

    def set_moderation_status(self, item_id, status):
        item = self.db.query(Item).get(item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        item.status = status
        self.db.commit()

    def get_item(self, item_id):
        item = self.db.query(Item).get(item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

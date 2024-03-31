import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.base_class import Item, User, Coords, Level, Image



db_host = os.getenv("POSTGRES_SERVER")
db_port = os.getenv("POSTGRES_PORT")
db_user = os.getenv("POSTGRES_USER")
db_pass = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")

engine = create_engine(f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}@{db_name}")
Session = sessionmaker(bind=engine)


class ItemService:
    def __init__(self):
        self.session = Session()

    def add_item(self, item_data):
        # Создать объекты для связанных таблиц
        user = User(**item_data.user.dict())
        coords = Coords(**item_data.coords.dict())
        level = Level(**item_data.level.dict())
        images = [Image(data=image.data, title=image.title) for image in item_data.images]

        # Создать объект Item и установить связи
        item = Item(
            beauty_title=item_data.beauty_title,
            title=item_data.title,
            other_titles=item_data.other_titles,
            connect=item_data.connect,
            add_time=item_data.add_time,
            user=user,
            coords=coords,
            level=level,
            images=images
        )

        self.session.add(item)
        self.session.commit()

    def set_moderation_status(self, item_id, status):
        item = self.session.query(Item).get(item_id)
        if item:
            item.status = status
            self.session.commit()
        else:
            raise ValueError(f"Item with id {item_id} not found")

    def get_moderation_status(self, item_id):
        item = self.session.query(Item).get(item_id)
        if item:
            return item.status
        else:
            raise ValueError(f"Item with id {item_id} not found")

    def get_item(self, item_id):
        item = self.session.query(Item).get(item_id)
        if item:
            return item
        else:
            raise ValueError(f"Item with id {item_id} not found")

    def edit_item(self, item_id, item_data):
        item = self.session.query(Item).filter(Item.id == item_id, Item.status == 'new').first()
        if item:
            # Здесь обновите поля item с использованием данных из item_data
            # Пропустите обновление полей, содержащих ФИО, адрес почты, и телефон
            self.session.commit()
            return 1, "Record updated successfully"
        else:
            return 0, "Item not found or not in 'new' status"

    def get_items_by_user_email(self, email):
        items = self.session.query(Item).join(User).filter(User.email == email).all()
        if items:
            return items
        else:
            return []

    def __del__(self):
        self.session.close()




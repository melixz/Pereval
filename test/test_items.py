import datetime
import pytest
from app.models.item import Item
from app.models.user import User
from app.models.coords import Coords
from app.models.level import Level
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.base_class import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def db():
    # Создаем все таблицы, включая зависимости (User, Coords, Level)
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()


def test_create_item(db):
    # Создаем необходимые объекты для внешних ключей
    user = User(
        email="test@example.com", fam="Test", name="User", otc="Otch", phone="123456789"
    )
    coords = Coords(latitude="45.0", longitude="90.0", height="1000")
    level = Level(winter="hard", summer="easy", autumn="medium", spring="medium")

    # Добавляем их в сессию
    db.add(user)
    db.add(coords)
    db.add(level)
    db.commit()

    # Создаем объект Item
    item = Item(
        beauty_title="Test Item",
        title="Test Title",
        other_titles="Another Title",
        connect="Test Connection",
        add_time=datetime.datetime.now(),
        status="new",
        user_id=user.id,
        coords_id=coords.id,
        level_id=level.id,
    )

    # Добавляем объект Item в базу данных
    db.add(item)
    db.commit()

    # Проверяем, что объект Item был успешно создан
    assert item.id is not None

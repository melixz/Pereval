import pytest
from fastapi import __version__
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from db.base_class import Base, Item, User, Coords, Level, Image
from httpx import AsyncClient
from main import app
from time import time


# Настройка тестовой БД в памяти
@pytest.fixture(scope="module")
def test_engine():
    return create_engine("sqlite:///:memory:")


@pytest.fixture(scope="module")
def test_session(test_engine):
    Base.metadata.create_all(test_engine)
    Session = sessionmaker(bind=test_engine)
    session = Session()
    yield session
    session.close()


# Тестирование создания экземпляров моделей
def test_create_item(test_session):
    item = Item(
        beauty_title="Test Item",
        title="Test Title",
        other_titles="Another Title",
        connect="Test Connection",
        add_time=datetime.now(),
        status="new",
    )
    test_session.add(item)
    test_session.commit()

    assert item.id is not None


def test_create_user(test_session):
    user = User(
        email="test@example.com",
        fam="Smith",
        name="John",
        otc="Otch",
        phone="1234567890",
    )
    test_session.add(user)
    test_session.commit()

    assert user.id is not None


def test_create_coords(test_session):
    coords = Coords(latitude="45.0", longitude="90.0", height="200")
    test_session.add(coords)
    test_session.commit()

    assert coords.id is not None


def test_create_level(test_session):
    level = Level(winter="hard", summer="easy", autumn="medium", spring="easy")
    test_session.add(level)
    test_session.commit()

    assert level.id is not None


def test_create_image(test_session, test_engine):
    # Предполагается, что уже существует Item для связи
    test_session.add(
        Item(
            beauty_title="Test Item for Image",
            title="Test Title",
            other_titles="Another Title",
            connect="Test Connection",
            add_time=datetime.now(),
            status="new",
        )
    )
    test_session.commit()

    last_item_id = test_session.query(Item).order_by(Item.id.desc()).first().id

    image = Image(data="FakeImageData", title="Test Image", item_id=last_item_id)
    test_session.add(image)
    test_session.commit()

    assert image.id is not None


@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "FastAPI" in response.text


@pytest.mark.asyncio
async def test_ping():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/ping")
    assert response.status_code == 200
    assert response.json() == {
        "res": "pong",
        "version": __version__,
        "time": pytest.approx(time(), abs=5),
    }

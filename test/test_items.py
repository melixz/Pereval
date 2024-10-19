import pytest
from app.models.item import Item
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.base_class import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def db():
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()


def test_create_item(db):
    item = Item(
        beauty_title="Test Item",
        title="Test Title",
        other_titles="Another Title",
        connect="Test Connection",
        add_time=datetime.now(),
        status="new",
    )
    db.add(item)
    db.commit()
    assert item.id is not None

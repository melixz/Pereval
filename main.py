from fastapi import FastAPI
from app.routers import items
from config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description="API для управления данными",
)

# Подключение маршрутов
app.include_router(items.router)


@app.get("/")
def read_root():
    """
    Возвращает приветственное сообщение.
    """
    return {"Hello": "World"}


# Для проверки состояния приложения
@app.get("/ping")
def ping():
    """
    Проверка состояния приложения.
    """
    return {"res": "pong"}

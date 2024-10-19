from fastapi import FastAPI
from app.routers import items
from config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

# Подключение маршрутов
app.include_router(items.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


# Для проверки состояния приложения
@app.get("/ping")
def ping():
    return {"res": "pong"}

## Описание проекта 

Проект представляет собой приложение FastAPI, которое упрощает задачу туристам по отправке данных о перевалах. Приложение предоставляет API для создания, обновления статуса модерации и просмотра объектов. Туристы смогут вносить данные о перевалах в мобильном приложении и отправлять их в ФСТР. Модератор из федерации будет верифицировать и вносить информацию в базу данных. Пользователи смогут просматривать статус модерации и базу данных с объектами, внесёнными другими.

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/melixz/Pereval
```

2. Установите необходимые зависимости:

```bash
pip install -r requirements.txt
```

3. Создайте файл `.env` в корневой директории проекта и добавьте следующие переменные окружения:

```
POSTGRES_SERVER=<ваш_хост_postgres>
POSTGRES_PORT=<порт_postgres>
POSTGRES_USER=<имя_пользователя_postgres>
POSTGRES_PASSWORD=<пароль_postgres>
POSTGRES_DB=<имя_базы_данных_postgres>
```

## Использование

1. Запустите сервер FastAPI:

```bash
uvicorn main:app --reload
```

2. API будет доступен по адресу http://127.0.0.1:8000.

3. Вы можете получить доступ к документации Swagger UI по адресу http://127.0.0.1:8000/docs.

## Точки доступа API

Ниже приведена таблица доступных точек доступа API:

| Метод  | Эндпоинт                          | Описание                     |
|--------|-----------------------------------|------------------------------|
| `POST` | `/submitData/`                    | Отправить данные             |
| `GET`  | `/submitData/`                    | Получить элементы по email пользователя |
| `PUT`  | `/items/{item_id}/status/{status}`| Обновить статус модерации    |
| `GET`  | `/submitData/{item_id}`           | Получить элемент             |
| `PATCH`| `/submitData/{item_id}`           | Редактировать элемент, если он в статусе 'new'       |
| `GET`  | `/`                               | Возвращает HTML-страницу     |
| `GET`  | `/ping`                           | Возвращает статус сервиса и версию FastAPI |

## Графическая диаграмма 

![API Endpoints Graph](https://diagrams.helpful.dev/d/d:2PeLljYx)


## Swagger UI

Документация Swagger UI для этого API доступна по адресу http://127.0.0.1:8000/docs после запуска сервера. Вы можете использовать Swagger UI для тестирования и взаимодействия с API.

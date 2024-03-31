 Конечно, вот документация для API и Swagger UI на основе предоставленных фрагментов кода:

# Item Moderation API

Это приложение FastAPI, которое предоставляет API для отправки и модерации объектов. Оно позволяет создавать новые объекты, обновлять их статус модерации и получать текущий статус модерации объекта.

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/your-username/your-project.git
```

2. Перейдите в директорию проекта:

```bash
cd your-project
```

3. Установите необходимые зависимости:

```bash
pip install fastapi uvicorn sqlalchemy psycopg2 python-dotenv
```

4. Создайте файл `.env` в корневой директории проекта и добавьте следующие переменные окружения:

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

## API Endpoints

### Отправить данные

- **URL:** `/submitData/`
- **Метод:** `POST`
- **Тело запроса:**

```json
{
  "beauty_title": "Красивый заголовок",
  "title": "Заголовок 1",
  "other_titles": "Другие заголовки",
  "connect": "Связь",
  "add_time": "2023-04-01T12:00:00",
  "user": {
    "email": "user@example.com",
    "fam": "Иванов",
    "name": "Иван",
    "otc": "Отчество",
    "phone": "+79012345678"
  },
  "coords": {
    "latitude": "55.7558",
    "longitude": "37.6173",
    "height": "100"
  },
  "level": {
    "winter": "low",
    "summer": "high",
    "autumn": "medium",
    "spring": "medium"
  },
  "images": [
    {
      "data": "base64_encoded_image_data",
      "title": "Image 1"
    },
    {
      "data": "base64_encoded_image_data",
      "title": "Image 2"
    }
  ]
}
```

- **Ответ:**
  - Статус: `200 OK`
  - Тело:

```json
{
  "message": "Data submitted successfully"
}
```

### Обновить статус модерации

- **URL:** `/items/{item_id}/status/{status}`
- **Метод:** `PUT`
- **Параметры пути:**
  - `item_id` (int): ID объекта для обновления.
  - `status` (str): Новый статус модерации. Допустимые значения: `new`, `pending`, `accepted`, `rejected`.
- **Ответ:**
  - Статус: `200 OK`
  - Тело:

```json
{
  "message": "Moderation status updated successfully"
}
```

- Ошибка: `400 Bad Request` (если предоставленное значение статуса недействительно)
  - Тело:

```json
{
  "error": "Invalid status value"
}
```

### Получить статус модерации

- **URL:** `/items/{item_id}/status`
- **Метод:** `GET`
- **Параметры пути:**
  - `item_id` (int): ID объекта для получения статуса модерации.
- **Ответ:**
  - Статус: `200 OK`
  - Тело:

```json
{
  "status": "pending"
}
```

- Ошибка: `404 Not Found` (если объект с указанным ID не найден)
  - Тело:

```json
{
  "error": "Item with id {item_id} not found"
}
```

## Swagger UI

Документация Swagger UI для этого API доступна по адресу http://127.0.0.1:8000/docs после запуска сервера. Вы можете использовать Swagger UI для тестирования и взаимодействия с API.

## Участие

Если вы обнаружите какие-либо проблемы или у вас есть предложения по улучшению, не стесняйтесь открывать задачи или отправлять запросы на слияние в репозитории проекта на GitHub.

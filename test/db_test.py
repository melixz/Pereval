import psycopg2
from psycopg2 import OperationalError
from config import settings


def test_connection():
    try:
        connection = psycopg2.connect(
            host=settings.POSTGRES_SERVER,
            user=settings.POSTGRES_USER,
            password=settings.POSTGRES_PASSWORD,
            dbname=settings.POSTGRES_DB,
            port=settings.POSTGRES_PORT,
        )
        print("Подключение к базе данных успешно установлено!")
        return True
    except OperationalError as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return False
    finally:
        if connection:
            connection.close()


test_connection()

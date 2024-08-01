import psycopg2
from psycopg2 import OperationalError
import os
from dotenv import load_dotenv

load_dotenv()

# Переменные окружения
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_SERVER = os.getenv("POSTGRES_SERVER", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")  # default postgres port is 5432
POSTGRES_DB = os.getenv("POSTGRES_DB", "tdd")
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


def test_connection():
    try:
        # Вывод параметров подключения для проверки
        print("Параметры подключения:")
        print(f"Host: {POSTGRES_SERVER}")
        print(f"User: {POSTGRES_USER}")
        print(f"Password: {'Пароль скрыт' if POSTGRES_PASSWORD else 'Пароль не задан'}")
        print(f"Database: {POSTGRES_DB}")
        print(f"Port: {POSTGRES_PORT}")

        connection = psycopg2.connect(
            host=POSTGRES_SERVER,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            dbname=POSTGRES_DB,
            port=POSTGRES_PORT,
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

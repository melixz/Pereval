from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


db_host = os.getenv("FSTR_DB_HOST")
db_port = os.getenv("FSTR_DB_PORT")
db_login = os.getenv("FSTR_DB_LOGIN")
db_pass = os.getenv("FSTR_DB_PASS")
db_name = os.getenv("FSTR_DB_NAME")

engine = create_engine(f"postgresql://{db_login}:{db_pass}@{db_host}:{db_port}@{db_name}")
Session = sessionmaker(bind=engine)



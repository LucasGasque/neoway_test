from sqlmodel import create_engine, SQLModel
from src.config import settings

postgresql_connection_string = settings.POSTGRESQL_CONNECTION_STRING

engine = create_engine(postgresql_connection_string)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

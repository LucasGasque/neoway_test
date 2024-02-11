from sqlmodel import create_engine, SQLModel

postgresql_connection_string = "postgresql+psycopg2://postgres:safepassword@localhost:5432/mydb"

engine = create_engine(postgresql_connection_string)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

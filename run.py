from src.pipeline import Pipeline
from src.infra.db import create_db_and_tables

if __name__ == "__main__":
    create_db_and_tables()

    Pipeline.run()

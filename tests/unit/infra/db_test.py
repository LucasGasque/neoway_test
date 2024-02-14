from unittest.mock import patch
from src.infra.db import engine, create_db_and_tables
from sqlmodel import SQLModel


def test_create_db_and_tables():
    with patch.object(SQLModel.metadata, "create_all") as mock_create_all:
        create_db_and_tables()
        mock_create_all.assert_called_once_with(engine)

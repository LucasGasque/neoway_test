import os

os.environ["LOGGERS"] = '["src:DEBUG"]'
os.environ["TEST_BASE_PATH"] = "/home/test/"
os.environ[
    "POSTGRESQL_CONNECTION_STRING"
] = "postgresql+psycopg2://postgres:testpassword@db:5432/testdb"

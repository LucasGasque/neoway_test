from datetime import date
from sqlmodel import Field, SQLModel, CheckConstraint


class PurchaseRecord(SQLModel, table=True):
    cpf: str = Field(
        primary_key=True,
        sa_column_args=(CheckConstraint("cpf ~ '^[0-9]{11}$'"),),
    )
    private: bool = Field(default=False)
    incomplete: bool = Field(default=False)
    last_purchase_date: date | None = Field(nullable=True)
    average_ticket: float | None = Field(nullable=True)
    last_purchase_ticket: float | None = Field(nullable=True)
    most_frequent_store: str | None = Field(
        nullable=True,
        sa_column_args=(CheckConstraint("most_frequent_store ~ '^[0-9]{14}$'"),),
    )
    last_purchase_store: str | None = Field(
        nullable=True,
        sa_column_args=(CheckConstraint("last_purchase_store ~ '^[0-9]{14}$'"),),
    )

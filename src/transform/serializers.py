from pydantic import BaseModel, field_validator
from datetime import date
from src.helpers.exceptions import InvalidCPF, InvalidCNPJ


class PurchaseRecordSerializer(BaseModel):
    cpf: str
    private: bool
    incomplete: bool
    last_purchase_date: date | None
    average_ticket: float | None
    last_purchase_ticket: float | None
    most_frequent_store: str | None
    last_purchase_store: str | None

    @classmethod
    def from_tuple(cls, values: tuple) -> "PurchaseRecordSerializer":
        return cls(
            cpf=values[0],
            private=values[1],
            incomplete=values[2],
            last_purchase_date=values[3],
            average_ticket=values[4],
            last_purchase_ticket=values[5],
            most_frequent_store=values[6],
            last_purchase_store=values[7],
        )

    @field_validator("cpf")
    def validate_cpf(cls, value: str) -> str:
        cpf = value.replace(".", "").replace("-", "")
        if len(cpf) == 11:
            return cpf
        raise InvalidCPF

    @field_validator("most_frequent_store", "last_purchase_store")
    def validate_cnpj(cls, value: str) -> str | None:
        if value == "NULL":
            return None
        cnpj = value.replace(".", "").replace("-", "").replace("/", "")
        if len(cnpj) == 14:
            return cnpj
        raise InvalidCNPJ

    @field_validator("private", "incomplete", mode="before")
    def validate_int(cls, value: str) -> bool:
        return True if value == "1" else False

    @field_validator("average_ticket", "last_purchase_ticket", mode="before")
    def validate_float(cls, value: str) -> float | None:
        if value == "NULL":
            return None
        return float(value.replace(",", "."))

    @field_validator("last_purchase_date", mode="before")
    def validate_date(cls, value: str) -> date | None:
        if value == "NULL":
            return None
        return date.fromisoformat(value)

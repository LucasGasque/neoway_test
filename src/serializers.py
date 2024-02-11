from pydantic import BaseModel, field_validator
from datetime import date
from src.helpers.exceptions import InvalidCPF, InvalidCNPJ


class SalesRecordSerializer(BaseModel):
    cpf: str
    private: str
    incomplete: str
    last_purchase_date: str
    average_ticket: str
    last_purchase_ticket: str
    most_frequent_store: str
    last_purchase_store: str

    @classmethod
    def from_tuple(cls, values: tuple) -> "SalesRecordSerializer":
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
    @classmethod
    def validate_cpf(cls, value: str) -> str:
        cpf = value.replace(".", "").replace("-", "")
        if len(cpf) == 11:
            return cpf
        raise InvalidCPF

    @field_validator("most_frequent_store", "last_purchase_store")
    @classmethod
    def validate_cnpj(cls, value: str) -> str | None:
        if value == "NULL":
            return None
        cnpj = value.replace(".", "").replace("-", "").replace("/", "")
        if len(cnpj) == 14:
            return cnpj
        raise InvalidCNPJ

    @field_validator("private", "incomplete")
    @classmethod
    def validate_int(cls, value: str) -> int:
        return int(value)

    @field_validator("average_ticket", "last_purchase_ticket")
    @classmethod
    def validate_float(cls, value: str) -> float | None:
        if value == "NULL":
            return None
        return float(value.replace(",", "."))

    @field_validator("last_purchase_date")
    @classmethod
    def validate_date(cls, value: str) -> date | None:
        if value == "NULL":
            return None
        return date.fromisoformat(value)

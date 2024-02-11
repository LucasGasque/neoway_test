from sqlmodel import Session

from src.transform.serializers import PurchaseRecordSerializer
from src.infra.db import engine
from src.load.models import PurchaseRecord


class Load:
    def save_records(
        self, transformed_registers: list[PurchaseRecordSerializer]
    ) -> None:
        with Session(engine) as session:
            for register in transformed_registers:
                session.add(PurchaseRecord(**register.model_dump()))

            session.commit()

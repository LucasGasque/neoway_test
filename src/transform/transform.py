from src.transform.serializers import PurchaseRecordSerializer
from src.helpers.exceptions import InvalidCPF, InvalidCNPJ
from logging import getLogger

logger = getLogger(__name__)


class Transform:
    def __transform_into_tuple(self, purchase_record: str) -> tuple:
        return tuple(a for a in purchase_record.split(" ") if a != "")

    def serialize_records(
        self, purchase_records_list: list[str]
    ) -> list[PurchaseRecordSerializer]:
        serialized_registers = []
        for purchase_record in purchase_records_list:
            try:
                serialized_register = PurchaseRecordSerializer.from_tuple(
                    self.__transform_into_tuple(purchase_record)
                )
                serialized_registers.append(serialized_register)
            except InvalidCPF:
                logger.warning(f"Invalid CPF: {purchase_record}")
            except InvalidCNPJ:
                logger.warning(f"Invalid CNPJ: {purchase_record}")
            except Exception as e:
                logger.error(f"Error: {e}")

        return serialized_registers

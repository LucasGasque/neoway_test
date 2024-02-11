from src.transform.serializers import PurchaseRecordSerializer
from src.helpers.exceptions import InvalidCPF, InvalidCNPJ


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
            except (InvalidCPF, InvalidCNPJ):
                ...

        return serialized_registers

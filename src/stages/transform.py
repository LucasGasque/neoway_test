from src.serializers import SalesRecordSerializer
from src.helpers.exceptions import InvalidCPF, InvalidCNPJ


class Transform:
    def __transform_into_tuple(self, register: str) -> tuple:
        return tuple(a for a in register.split(" ") if a != "")

    def serialize_registers(
        self, registers_list: list[str]
    ) -> list[SalesRecordSerializer]:
        serialized_registers = []
        for register in registers_list:
            try:
                serialized_register = SalesRecordSerializer.from_tuple(
                    self.__transform_into_tuple(register)
                )
                serialized_registers.append(serialized_register)
            except (InvalidCPF, InvalidCNPJ):
                ...

        return serialized_registers

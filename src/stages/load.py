from src.serializers import SalesRecordSerializer


class Load:
    def save_registers(
        self, transformed_registers: list[SalesRecordSerializer]
    ) -> None:
        ...

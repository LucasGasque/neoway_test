from src.stages.extract import Extract
from src.stages.transform import Transform
from src.stages.load import Load


class Pipeline:
    @staticmethod
    def run():
        registers_list = Extract.list_registers()

        transformed_registers_list = Transform().serialize_registers(registers_list)

        print(transformed_registers_list[0])

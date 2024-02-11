from src.config import settings


class Extract:
    @staticmethod
    def list_purchase_records() -> list[str]:
        with open(f"{settings.TEST_BASE_PATH}base_teste.txt", "r") as file:
            lines = file.readlines()
            lines = list(map(lambda x: x.strip(), lines))

        return lines[1:]

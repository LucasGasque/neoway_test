from src.config import settings


class Extract:
    @staticmethod
    def list_purchase_records() -> list[str]:
        with open(settings.TEST_BASE_PATH, "r") as file:
            lines = file.readlines()
            lines = list(map(lambda x: x.strip(), lines))

        return lines[1:]

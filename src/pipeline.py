from src.extract.extract import Extract
from src.transform.transform import Transform
from src.load.load import Load
from logging import getLogger

logger = getLogger(__name__)


class Pipeline:
    @staticmethod
    def run() -> None:
        logger.info("Starting pipeline")
        purchase_records_list = Extract.list_purchase_records()


        logger.debug(f"Extracted {len(purchase_records_list)} records")
        transformed_purchase_records_list = Transform().serialize_records(
            purchase_records_list
        )

        Load().save_records(transformed_purchase_records_list)

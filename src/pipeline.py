from src.extract.extract import Extract
from src.transform.transform import Transform
from src.load.load import Load
from logging import getLogger

logger = getLogger(__name__)


class Pipeline:
    @staticmethod
    def run() -> None:
        logger.info("Iniciando o pipeline")

        logger.info("Extraindo os dados")
        purchase_records_list = Extract.list_purchase_records()

        logger.info("Transformando os dados")
        transformed_purchase_records_list = Transform().serialize_records(
            purchase_records_list
        )
        logger.debug(
            f"{len(transformed_purchase_records_list)} registros transformados"
        )

        logger.info("Carregando os dados")
        Load().save_records(transformed_purchase_records_list)

        logger.info("Pipeline finalizado com sucesso!")

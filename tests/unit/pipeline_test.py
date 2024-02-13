from unittest.mock import patch, MagicMock
from src.extract.extract import Extract
from src.transform.transform import Transform
from src.load.load import Load
from src.pipeline import (
    Pipeline,
)


def test_pipeline_run():
    with patch("src.pipeline.logger", new=MagicMock()) as mock_logger, patch.object(
        Extract, "list_purchase_records", return_value=["record1", "record2"]
    ), patch.object(
        Transform,
        "serialize_records",
        return_value=["transformed_record1", "transformed_record2"],
    ), patch.object(Load, "save_records", return_value=None) as mock_save_records:
        Pipeline.run()

        mock_save_records.assert_called_once_with(
            ["transformed_record1", "transformed_record2"]
        )
        mock_logger.info.assert_any_call("Iniciando o pipeline")
        mock_logger.info.assert_any_call("Extraindo os dados")
        mock_logger.info.assert_any_call("Transformando os dados")
        mock_logger.debug.assert_any_call("2 registros transformados")
        mock_logger.info.assert_any_call("Carregando os dados")
        mock_logger.info.assert_any_call("Pipeline finalizado com sucesso!")

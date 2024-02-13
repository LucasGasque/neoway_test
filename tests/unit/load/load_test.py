from unittest.mock import patch
from src.transform.serializers import PurchaseRecordSerializer
from src.load.load import Load


@patch("src.load.load.Session")
def test_save_records(mock_session):
    load = Load()
    transformed_registers = [
        PurchaseRecordSerializer(
            cpf="11111111111",
            private=True,
            incomplete=False,
            average_ticket="NULL",
            last_purchase_date="NULL",
            last_purchase_store="NULL",
            last_purchase_ticket="NULL",
            most_frequent_store="NULL",
        )
    ]
    mock_session_instance = mock_session.return_value.__enter__.return_value

    load.save_records(transformed_registers)

    mock_session.assert_called_once()
    mock_session_instance.add.assert_called_once()
    mock_session_instance.commit.assert_called_once()

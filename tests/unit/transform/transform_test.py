from unittest.mock import patch, MagicMock
from src.helpers.exceptions import InvalidCPF, InvalidCNPJ
from src.transform.transform import Transform


def test_transform_into_tuple():
    transform = Transform()
    purchase_record = "111.111.111-11 1 0 2024-02-13 100,00 50,00 11.111.111/1111-11 22.222.222/2222-22"
    expected_tuple = (
        "111.111.111-11",
        "1",
        "0",
        "2024-02-13",
        "100,00",
        "50,00",
        "11.111.111/1111-11",
        "22.222.222/2222-22",
    )

    result_tuple = transform._Transform__transform_into_tuple(purchase_record)

    assert result_tuple == expected_tuple


@patch("src.transform.transform.PurchaseRecordSerializer.from_tuple")
def test_serialize_records(mock_from_tuple):
    transform = Transform()
    purchase_records_list = [
        "111.111.111-11 1 0 2024-02-13 100,00 50,00 11.111.111/1111-11 22.222.222/2222-22"
    ]
    mock_from_tuple.return_value = MagicMock()

    serialized_registers = transform.serialize_records(purchase_records_list)

    assert len(serialized_registers) == len(purchase_records_list)
    mock_from_tuple.assert_called_once()


@patch("src.transform.transform.PurchaseRecordSerializer.from_tuple")
def test_serialize_records_with_invalid_cpf(mock_from_tuple):
    transform = Transform()
    purchase_records_list = [
        "111.111.111-11 1 0 2024-02-13 100,00 50,00 11.111.111/1111-11 22.222.222/2222-22"
    ]
    mock_from_tuple.side_effect = InvalidCPF

    serialized_registers = transform.serialize_records(purchase_records_list)

    assert len(serialized_registers) == 0
    mock_from_tuple.assert_called_once()


@patch("src.transform.transform.PurchaseRecordSerializer.from_tuple")
def test_serialize_records_with_invalid_cnpj(mock_from_tuple):
    transform = Transform()
    purchase_records_list = [
        "111.111.111-11 1 0 2024-02-13 100,00 50,00 11.111.111/1111-11 22.222.222/2222-22"
    ]
    mock_from_tuple.side_effect = InvalidCNPJ

    serialized_registers = transform.serialize_records(purchase_records_list)

    assert len(serialized_registers) == 0
    mock_from_tuple.assert_called_once()

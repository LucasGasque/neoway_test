import pytest
from datetime import date
from src.helpers.exceptions import InvalidCPF, InvalidCNPJ
from src.transform.serializers import (
    PurchaseRecordSerializer,
)
from tests.mocks.serializers import purchase_record_tuple


def test_from_tuple():
    record = PurchaseRecordSerializer.from_tuple(purchase_record_tuple)

    assert record.cpf == "11111111111"
    assert record.private is True
    assert record.incomplete is False
    assert record.last_purchase_date == date(2024, 2, 13)
    assert record.average_ticket == 100.00
    assert record.last_purchase_ticket == 50.00
    assert record.most_frequent_store == "79379491000850"
    assert record.last_purchase_store == "79379491000850"


def test_validate_cpf_raises_exception():
    with pytest.raises(InvalidCPF):
        PurchaseRecordSerializer(
            cpf="111.111.111-1",
            private="1",
            incomplete="0",
            average_ticket="NULL",
            last_purchase_date="NULL",
            last_purchase_store="NULL",
            last_purchase_ticket="NULL",
            most_frequent_store="NULL",
        )


def test_validate_cnpj_raises_exception():
    with pytest.raises(InvalidCNPJ):
        PurchaseRecordSerializer(
            most_frequent_store="11.111.111/0011-11",
            last_purchase_store="22.222.222/0002-22",
            private="1",
            incomplete="0",
            last_purchase_date="NULL",
            average_ticket="NULL",
            last_purchase_ticket="NULL",
        )


def test_validate_int():
    record = PurchaseRecordSerializer(
        cpf="11111111111",
        private="1",
        incomplete="0",
        average_ticket="NULL",
        last_purchase_ticket="NULL",
        last_purchase_date="NULL",
        most_frequent_store="NULL",
        last_purchase_store="NULL",
    )
    assert record.private is True
    assert record.incomplete is False


def test_validate_float():
    record = PurchaseRecordSerializer(
        cpf="11111111111",
        average_ticket="100,00",
        last_purchase_ticket="50,00",
        private="1",
        incomplete="0",
        last_purchase_date="2024-02-13",
        most_frequent_store="NULL",
        last_purchase_store="NULL",
    )
    assert record.average_ticket == 100.00
    assert record.last_purchase_ticket == 50.00


def test_validate_date():
    record = PurchaseRecordSerializer(
        cpf="11111111111",
        average_ticket="100,00",
        last_purchase_ticket="50,00",
        private="1",
        incomplete="0",
        last_purchase_date="2024-02-13",
        most_frequent_store="NULL",
        last_purchase_store="NULL",
    )
    assert record.last_purchase_date == date(2024, 2, 13)

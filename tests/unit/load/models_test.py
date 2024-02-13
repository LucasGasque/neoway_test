from datetime import date
from src.load.models import (
    PurchaseRecord,
)


def test_valid_purchase_record():
    record = PurchaseRecord(
        cpf="11111111111",
        private=True,
        incomplete=False,
        last_purchase_date=date(2024, 2, 13),
        average_ticket=100.00,
        last_purchase_ticket=50.00,
        most_frequent_store="11111111111111",
        last_purchase_store="22222222222222",
    )

    assert record.cpf == "11111111111"
    assert record.private is True
    assert record.incomplete is False
    assert record.last_purchase_date == date(2024, 2, 13)
    assert record.average_ticket == 100.00
    assert record.last_purchase_ticket == 50.00
    assert record.most_frequent_store == "11111111111111"
    assert record.last_purchase_store == "22222222222222"

from unittest.mock import mock_open, patch
from src.extract.extract import Extract
from tests.mocks.extracts import mock_lines, mock_file


def test_list_purchase_records():
    mock_file_content = "\n".join(mock_file)

    with patch("builtins.open", mock_open(read_data=mock_file_content)):
        purchase_records = Extract.list_purchase_records()

    assert len(purchase_records) == len(mock_lines)
    assert purchase_records == mock_lines

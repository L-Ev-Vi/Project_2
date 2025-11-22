import os
from unittest.mock import mock_open, patch

from src.reading_from_json import reading_from_json


@patch("builtins.open")
def test_reading_from_json(mock_read, file_json):
    mock_open(mock=mock_read, read_data=file_json)
    assert reading_from_json("./data/f.json") is None
    mock_read.assert_called_once_with(os.path.abspath("./data/f.json"), encoding="utf-8")

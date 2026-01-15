import pytest
from text_find import text_find


def test_text_find_missing_file():
    """
    Test that text_find raises FileNotFoundError when the file path does not exist.
    """

    missing_path = "not_a_real_file_28.txt"

    with pytest.raises(FileNotFoundError):
        text_find(missing_path, "keyword")

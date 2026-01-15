import pytest
from text_find import text_find

def test_text_find_keyword_validation(tmp_path):
    """
    Test that text_find raises ValueError when keyword is empty.

    An empty keyword is invalid and should not be searched.
    """

    # Arrange: create a valid text file
    file_path = tmp_path / "sample.txt"
    file_path.write_text("This is a simple test file")

    # Act & Assert: empty keyword should raise an error
    with pytest.raises(ValueError):
        text_find(str(file_path), "")

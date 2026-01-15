from text_find import text_find

def test_text_find_read_valid_file(tmp_path):
    """
    Test that text_find correctly reads a valid input file.

    This test verifies:
    - if the file can be opened/read, text_find should return an int (not crash)
    """

    # Arrange: create a small text file
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Group 28 \n This is the first test file")

    # Act: keyword choice is not the focus; use something unlikely to match
    result1 = text_find(str(file_path), "keyword_in_wrong_format")
    result2 = text_find(str(file_path), "group")

    # Assert: function executed and returned the correct type
    assert isinstance(result1, int), "text_find should return an integer"
    assert isinstance(result2, int), "text_find should return an integer"
import pytest
import os
from text_processor.text_lower import text_lower

def test_text_lower_convert():
    """Test that text_lower correctly converts uppercase text to lowercase."""
    input_path = "tests/poe.txt"
    output_path = "tests/output.txt"

    text_lower(input_path, output_path)

    with open(output_path, "r", encoding="utf-8") as f:
        output_content = f.read()
    
    assert output_content == output_content.lower()
    assert "annabel lee" in output_content

def test_text_lower_empty():
    """Test that text_lower handles empty files correctly."""
    input_path = "tests/empty.txt"
    output_path = "tests/output.txt"

    text_lower(input_path, output_path)

    with open(output_path, "r", encoding="utf-8") as f:
        assert f.read() == ""

def test_text_lower_invalid_type():
    """Test that text_lower raises TypeError for non-string input/output paths."""
    # non-string input_path
    with pytest.raises(TypeError, match="Both input_path and output_path must be strings" ):
        text_lower(123, "tests/output.txt")
    # non-string output_path
    with pytest.raises(TypeError):
        text_lower("tests/poe.txt", 123)
    # both non-string
    with pytest.raises(TypeError):
        text_lower(None, None)

def test_text_lower_invalid_extension():
    """Test that text_lower raises ValueError for non-.txt file extensions."""
    # non-.txt input_path extension
    with pytest.raises(ValueError, match="Both input_path and output_path must have a .txt file extension"):
        text_lower("tests/poe.csv", "tests/output.txt")
    # non-.txt output_path extension
    with pytest.raises(ValueError, match="Both input_path and output_path must have a .txt file extension"):
        text_lower("tests/poe.txt", "tests/output.pdf")

def test_text_lower_input_path_not_found():
    """Test that text_lower raises FileNotFoundError if input file or output file not found."""
    # input file not found
    with pytest.raises(FileNotFoundError, match="is not found"):
        text_lower("tests/non_existent.txt", "tests/output.txt")
    # output file not found
    with pytest.raises(FileNotFoundError, match="is not found"):
        text_lower("tests/poe.txt", "tests/non_existent.txt")
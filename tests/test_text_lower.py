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

def test_text_lower_file_not_found():
    """Test that text_lower raises FileNotFoundError for non-existent input file."""
    with pytest.raises(FileNotFoundError):
        text_lower("tests/non_existent.txt", "tests/output.txt")

def test_text_lower_invalid_type():
    """Test that text_lower raises TypeError for non-string input/output paths."""
    with pytest.raises(TypeError):
        text_lower(123, "tests/output.txt")
    with pytest.raises(TypeError):
        text_lower("tests/poe.txt", None)
    with pytest.raises(TypeError):
        text_lower("tests/poe.txt", 123)

def test_text_lower_invalid_extension():
    """Test that text_lower raises ValueError for non-.txt file extensions."""
    with pytest.raises(ValueError):
        text_lower("tests/poe.csv", "tests/output.txt")
    with pytest.raises(ValueError):
        text_lower("tests/poe.txt", "tests/output.pdf")
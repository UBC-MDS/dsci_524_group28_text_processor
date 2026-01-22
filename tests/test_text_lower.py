import pytest
import os
from text_processor.text_lower import text_lower

def test_text_lower_convert():
    """Test that text_lower correctly converts uppercase text to lowercase."""
    input_path = "tests/poe.txt"
    output_path = "tests/output.txt"
    expected_path = "tests/expected_output/text_lower/poe_lower.txt"

    text_lower(input_path, output_path)

    with open(output_path, "r", encoding="utf-8") as f:
        result = f.read()
    with open(expected_path, "r", encoding="utf-8") as f:
        expected = f.read()
    
    assert result == expected
    assert "annabel lee" in result

def test_text_lower_empty():
    """Test that text_lower handles empty files correctly."""
    input_path = "tests/empty.txt"
    output_path = "tests/output.txt"

    text_lower(input_path, output_path)

    with open(output_path, "r", encoding="utf-8") as f:
        result = f.read()
    with open(input_path, "r", encoding="utf-8") as f:
        empty = f.read()
    
    assert result == empty

def test_text_lower_no_change():
    """Test that text_lower leaves already lowercase text unchanged."""
    input_path = "tests/expected_output/text_lower/poe_lower.txt"
    output_path = "tests/output.txt"

    text_lower(input_path, output_path)

    with open(output_path, "r", encoding="utf-8") as f:
        result = f.read()
    with open(input_path, "r", encoding="utf-8") as f:
        original = f.read()
    
    assert result == original

def test_text_lower_special_characters():
    """Test that text_lower correctly converts text with special characters."""
    input_path = "tests/expected_output/text_lower/special_char.txt"
    output_path = "tests/output.txt"
    expected_path = "tests/expected_output/text_lower/special_char_lower.txt"

    text_lower(input_path, output_path)

    with open(output_path, "r", encoding="utf-8") as f:
        result = f.read()
    with open(expected_path, "r", encoding="utf-8") as f:
        expected = f.read()
    
    assert result == expected

def test_text_lower_overwrite():
    """Test that text_lower can overwrite the input file."""
    input_path = "tests/expected_output/text_lower/poe_overwrite.txt"
    output_path = input_path
    expected_path = "tests/expected_output/text_lower/poe_lower.txt"

    text_lower(input_path, output_path)

    with open(output_path, "r", encoding="utf-8") as f:
        result = f.read()
    with open(expected_path, "r", encoding="utf-8") as f:
        expected = f.read()
    
    assert result == expected

def test_text_lower_whitespace():
    """Test that text_lower preserves whitespace characters."""
    input_path = "tests/expected_output/text_lower/whitespace.txt"
    output_path = "tests/output.txt"
    expected_path = "tests/expected_output/text_lower/whitespace.txt"

    text_lower(input_path, output_path)

    with open(output_path, "r", encoding="utf-8") as f:
        result = f.read()
    with open(expected_path, "r", encoding="utf-8") as f:
        expected = f.read()
    
    assert result == expected

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
    """Test that text_lower raises FileNotFoundError if input file not found."""
    with pytest.raises(FileNotFoundError, match="is not found"):
        text_lower("tests/non_existent.txt", "tests/output.txt")

# Milestone 3: additional unit test
def test_text_lower_raises_when_output_path_points_to_directory(tmp_path):
    """Output path ends with .txt but is actually a directory -> should raise an OS error."""
    input_path = "tests/poe.txt"

    out_dir = tmp_path / "out.txt"
    out_dir.mkdir()

    with pytest.raises(OSError):
        text_lower(input_path, str(out_dir))

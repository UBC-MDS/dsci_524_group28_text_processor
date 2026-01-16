"""
Performs unit tests for the text_replace() function.
"""

import pytest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from src.text_processor.text_replace import text_replace


def test_regular_replace(output_data):
    """Test a typical word replace scenario"""

    text_replace("tests/poe.txt", "tests/output.txt", "sea", "bee")

    with open("tests/output.txt", "r", encoding='utf-8') as f:
        result = f.read()
    with open("tests/expected_output/text_replace/regular.txt", "r", encoding='utf-8') as f:
        expected = f.read()
    
    assert result == expected


def test_whitespace():
    """Check replacement of a single space"""

    text_replace("tests/poe.txt", "tests/output.txt", " ", "space")

    with open("tests/output.txt", "r", encoding='utf-8') as f:
        result = f.read()
    with open("tests/expected_output/text_replace/whitespace.txt", "r", encoding='utf-8') as f:
        expected = f.read()
    
    assert result == expected


def test_case_sensitive():
    """Check that replacements are case sensitive"""

    text_replace("tests/poe.txt", "tests/output.txt", "In", "On")

    with open("tests/output.txt", "r", encoding='utf-8') as f:
        result = f.read()
    with open("tests/expected_output/text_replace/case_sensitive.txt", "r", encoding='utf-8') as f:
        expected = f.read()
    
    assert result == expected
    

def test_replace_with_nothing():
    """Check that replacing an item with nothing works"""

    text_replace("tests/poe.txt", "tests/output.txt", " Lee", "")

    with open("tests/output.txt", "r", encoding='utf-8') as f:
        result = f.read()
    with open("tests/expected_output/text_replace/nothing.txt", "r", encoding='utf-8') as f:
        expected = f.read()
    
    assert result == expected


def test_old_dne():
    """Tests scenario where the old string does not exist in the text"""

    text_replace("tests/poe.txt", "tests/output.txt", "nuclear reactor", "fibula")
    
    with open("tests/output.txt", "r", encoding='utf-8') as f:
        result = f.read()
    with open("tests/expected_output/text_replace/input.txt", "r", encoding='utf-8') as f:
        expected = f.read()
    
    assert result == expected


def test_empty():
    """Checks an empty file writes an empty file"""

    text_replace("tests/empty.txt", "tests/output.txt", "sea", "")
    
    with open("tests/output.txt", "r", encoding='utf-8') as f:
        result = f.read()
    
    assert result == ""


def test_arg_type():
    """Checks that the function throws an error for invalid argument types"""

    with pytest.raises(TypeError):
        text_replace("tests/poe.txt", "tests/output.txt", ["sea", "Lee"], "")
    
    with pytest.raises(TypeError):
        text_replace("tests/poe.txt", "tests/output.txt", "sea", 5)
    
    with pytest.raises(TypeError):
        text_replace("tests/poe.txt", "tests/output.txt", "sea", "")
    
    with pytest.raises(TypeError):
        text_replace("tests/poe.txt", "tests/output.txt", "", "sea")
    
    with pytest.raises(TypeError):
        text_replace("tests/poe.txt", True, "sea", "")
    
    with pytest.raises(TypeError):
        text_replace("tests/poe.txt", "tests/output.txt", "sea", "")


def test_file_type():
    """Tests that the function throws an error if the input file is not a .txt file"""

    with pytest.raises(ValueError, match=".*txt"):
        text_replace("tests/poe.qmd", "tests/output.txt", "sea", "bee")

    with pytest.raises(ValueError, match=".*txt"):
        text_replace("tests/poe.txt", "tests/output.csv", "sea", "bee")


def test_input_file_not_found():
    """Tests that the function throws an error when the input file doesn't exist"""
    with pytest.raises(FileNotFoundError):
        text_replace("tests/dne.txt", "tests/output.txt", "sea", "bee")


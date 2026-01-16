"""
Ideas

exceptions:
inputs are strings - old must be non-empty
input path and output path are valid directories
input path file exists and is a text file/readable?? (https://www.geeksforgeeks.org/python/check-if-file-is-readable-in-python/)
- maybe try image files, rmd files as a test to see what is looks like

regular case

edge cases:
empty text file (https://www.geeksforgeeks.org/python/check-if-a-text-file-empty-in-python/)
nothing to replace
"""

import pytest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.text_processor.text_replace import text_replace


def test_regular_replace(output_data):
    """Test a typical word replace scenario"""

    text_replace("tests/poe.txt", "test/output.txt", "sea", "bee")

    with open("tests/output.txt", "r", encoding='utf-8') as f:
        result = f.read()
    with open("tests/expected_output/text_replace/regular.txt", "r", encoding='utf-8') as f:
        expected = f.read()
    
    assert result == expected

def test_whitespace():
    """Check replacement of whitespaces"""

    text_replace("tests/poe.txt", "tests/output.txt", " ", "space")

    with open("tests/output.txt", "r", encoding='utf-8') as f:
        result = f.read()
    with open("tests/expected_output/text_replace/whitespace.txt", "r", encoding='utf-8') as f:
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
    pass

def test_old_dne():
    """Tests scenario where the old string does not exist in the text"""
    text_replace("tests/poe.txt", "tests/output.txt", "nuclear reactor", "fibula")
    pass

def test_empty():
    """Checks an empty file writes an empty file"""
    text_replace("tests/empty.txt", "tests/output.txt", "sea", "")
    pass

def test_arg_type():
    """Checks that the function throws an error for invalid argument types"""
    text_replace("tests/poe.txt", "tests/output.txt", ["sea", "Lee"], "")
    text_replace("tests/poe.txt", "tests/output.txt", "sea", 5)
    text_replace("tests/poe.txt", "tests/output.txt", "sea", "")
    text_replace("tests/poe.txt", "tests/output.txt", "", "sea")
    text_replace("tests/poe.txt", True, "sea", "")
    text_replace("tests/poe.txt", "tests/output.txt", "sea", "")
    pass

def test_directory():
    """Tests that the function throws an error for invalid directories"""
    pass

def test_file_type():
    """Tests that the function throws an error if the input file is not a .txt file"""
    pass

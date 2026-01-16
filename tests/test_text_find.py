import pytest
from text_processor.text_find import text_find


def test_text_find_first_occurrence_from_output_txt():
    """
    Returns the FIRST occurrence index.
    Keyword contains a space.
    """
    input_path = "tests/output.txt"

    content = "hello anna lee\nanna lee again\n"
    with open(input_path, "w", encoding="utf-8") as f:
        f.write(content)

    assert text_find(input_path, "anna lee") == 6


def test_text_find_exact_match_not_substring():
    """
    Exact match only: 'anna' should NOT match inside 'annabelle'.
    """
    input_path = "tests/output.txt"

    with open(input_path, "w", encoding="utf-8") as f:
        f.write("annabelle lee lives here\n")

    assert text_find(input_path, "anna") == -1


def test_text_find_keyword_with_extra_spaces_normalized():
    """
    Keyword can have extra spaces; we normalize to single spaces.
    """
    input_path = "tests/output.txt"

    with open(input_path, "w", encoding="utf-8") as f:
        f.write("start anna lee end\n")

    assert text_find(input_path, "  anna   lee  ") == 6


def test_text_find_unicode_letters_allowed():
    """
    Allows Unicode letters (é, ñ, ü).
    """
    input_path = "tests/output.txt"

    with open(input_path, "w", encoding="utf-8") as f:
        f.write("hola josé\n")

    assert text_find(input_path, "josé") == 5


def test_text_find_not_found_returns_minus_one():
    input_path = "tests/output.txt"
    with open(input_path, "w", encoding="utf-8") as f:
        f.write("anna lee\n")

    assert text_find(input_path, "john") == -1


# -----------------------
# Validation tests
# -----------------------

def test_text_find_keyword_empty_raises():
    input_path = "tests/output.txt"
    with open(input_path, "w", encoding="utf-8") as f:
        f.write("anna lee\n")

    with pytest.raises(ValueError, match="non-empty"):
        text_find(input_path, "   ")


def test_text_find_keyword_invalid_characters_raises():
    input_path = "tests/output.txt"
    with open(input_path, "w", encoding="utf-8") as f:
        f.write("anna lee\n")

    with pytest.raises(ValueError, match="only letters and spaces"):
        text_find(input_path, "anna-lee")


def test_text_find_keyword_not_string_raises():
    input_path = "tests/output.txt"
    with open(input_path, "w", encoding="utf-8") as f:
        f.write("anna lee\n")

    with pytest.raises(TypeError, match="keyword must be a string"):
        text_find(input_path, 123)


def test_text_find_input_path_invalid_extension_raises():
    with pytest.raises(ValueError, match=r"\.txt"):
        text_find("tests/output.csv", "anna")


def test_text_find_input_path_not_found_raises():
    with pytest.raises(FileNotFoundError, match="is not found"):
        text_find("tests/does_not_exist.txt", "anna")

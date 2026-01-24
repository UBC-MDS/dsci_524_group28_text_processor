"""Unit tests for text_remove.

These tests verify correct whole-word removal behavior and defensive error handling.
"""
import pytest

from text_processor.text_remove import text_remove


def test_text_remove_removes_whole_word_only(tmp_path):
    """Remove whole-word matches only (e.g., 'the' removed but 'There/other' unchanged)."""
    input_path = tmp_path / "in.txt"
    output_path = tmp_path / "output.txt"

    input_path.write_text("the sea\nThere is the other\n", encoding="utf-8")

    text_remove(str(input_path), str(output_path), "the")

    result = output_path.read_text(encoding="utf-8")
    assert result == " sea\nThere is  other\n"


def test_text_remove_no_match_keeps_text_same(tmp_path):
    """Output should match input when the target token is not present."""
    input_path = tmp_path / "in.txt"
    output_path = tmp_path / "output.txt"

    input_path.write_text("There is other\n", encoding="utf-8")

    text_remove(str(input_path), str(output_path), "the")

    result = output_path.read_text(encoding="utf-8")
    assert result == "There is other\n"


def test_text_remove_overwrite_input_file(tmp_path):
    """Allow overwriting the input file when input_path == output_path."""
    src = tmp_path / "poe_copy.txt"
    src.write_text("the sea\nThere\nother\n", encoding="utf-8")

    text_remove(str(src), str(src), "the")

    result = src.read_text(encoding="utf-8")
    assert result == " sea\nThere\nother\n"


def test_text_remove_empty_input_file(tmp_path):
    """Empty input should produce an empty output file."""
    empty_file = tmp_path / "empty.txt"
    out_file = tmp_path / "output.txt"
    empty_file.write_text("", encoding="utf-8")

    text_remove(str(empty_file), str(out_file), "the")

    assert out_file.read_text(encoding="utf-8") == ""


def test_text_remove_raises_on_wrong_types(tmp_path):
    """Raise TypeError when input_path/output_path/string_to_remove are not strings."""
    out_file = tmp_path / "output.txt"
    with pytest.raises(TypeError):
        text_remove(123, str(out_file), "x")
    with pytest.raises(TypeError):
        text_remove("tests/poe.txt", 456, "x")
    with pytest.raises(TypeError):
        text_remove("tests/poe.txt", str(out_file), 789)


def test_text_remove_raises_on_bad_extension(tmp_path):
    """Raise ValueError when input or output paths do not end with .txt."""
    out_file = tmp_path / "output.csv"
    with pytest.raises(ValueError):
        text_remove("tests/poe.txt", str(out_file), "x")
    with pytest.raises(ValueError):
        text_remove("tests/poe.csv", str(tmp_path / "output.txt"), "x")


def test_text_remove_raises_on_empty_remove_string(tmp_path):
    """Raise ValueError when string_to_remove is an empty string."""
    out_file = tmp_path / "output.txt"
    with pytest.raises(ValueError):
        text_remove("tests/poe.txt", str(out_file), "")


def test_text_remove_raises_when_input_missing(tmp_path):
    """Raise FileNotFoundError when the input file does not exist."""
    out_file = tmp_path / "output.txt"
    with pytest.raises(FileNotFoundError):
        text_remove("tests/does_not_exist.txt", str(out_file), "x")


def test_text_remove_raises_when_output_dir_missing(tmp_path):
    """Raise FileNotFoundError when the output directory does not exist."""
    missing_dir = tmp_path / "missing_dir"
    out_file = missing_dir / "output.txt"
    with pytest.raises(FileNotFoundError):
        text_remove("tests/poe.txt", str(out_file), "the")

# Milestone 3: additional unit test
def test_text_remove_word_at_line_boundaries(tmp_path):
    """Remove word at start/end of lines; keep newlines intact."""
    input_path = tmp_path / "in.txt"
    output_path = tmp_path / "out.txt"

    input_path.write_text("the\nsea the\n the \n", encoding="utf-8")

    text_remove(str(input_path), str(output_path), "the")

    result = output_path.read_text(encoding="utf-8")
    
    assert result == "\nsea \n  \n"

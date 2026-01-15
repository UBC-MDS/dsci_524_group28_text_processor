import pytest
import os
from dsci_524_group28_text_processor.text_lower import text_lower

def test_text_lower_convert():
    """Test that text_lower correctly converts uppercase text to lowercase."""
    # ... set up

def test_text_lower_empty():
    """Test that text_lower handles empty files correctly."""
    # ... set up

def test_text_lower_file_not_found():
    """Test that text_lower raises FileNotFoundError for non-existent input file."""
    # ... set up

def test_text_lower_invalid_type():
    """Test that text_lower raises TypeError for non-string input/output paths."""
    # ... set up)

def test_text_lower_invalid_extension():
    """Test that text_lower raises ValueError for non-.txt file extensions."""
    # ... set up
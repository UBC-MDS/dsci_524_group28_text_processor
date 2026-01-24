"""
A module that reads a text file to locate the first occurrence of 'keyword' in text
and returns its character index.

Note: The returned index refers to the text read from the processed file
(e.g., lowercased / cleaned by earlier steps), not the raw file text.
"""

import os
import re


def text_find(input_path: str, keyword: str) -> int:
    """
    Finds the first whole-word instance of `keyword` in a text file.

    Keyword rules:
    - keyword must be a string
    - keyword cannot be empty/whitespace
    - keyword may contain spaces
    - keyword words must contain letters only (UTF-8 Unicode letters allowed)

    Returns:
    - 0-based character index of the first match in the file text
    - -1 if not found

    Raises
    ------
    TypeError
        If input_path or keyword is not a string.
    ValueError
        If input_path is not a .txt file, or keyword is invalid.
    FileNotFoundError
        If the input file does not exist.
    OSError
        If there is an error reading the file.
    """
    # Validate input_path
    if not isinstance(input_path, str):
        raise TypeError("input_path must be a string")
    if not input_path.endswith(".txt"):
        raise ValueError("input_path must have a .txt file extension")
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"The input file '{input_path}' is not found")

    # Validate keyword type
    if not isinstance(keyword, str):
        raise TypeError("keyword must be a string")

    # Normalize keyword: strip ends, lowercase, collapse whitespace between words
    tokens = keyword.strip().lower().split()
    if len(tokens) == 0:
        raise ValueError("keyword must be a non-empty string")

    # Validate: letters only (Unicode-aware)
    for token in tokens:
        if not token.isalpha():
            raise ValueError("keyword must contain only letters and spaces")

    keyword_norm = " ".join(tokens)

    # Read processed text; lower for safety (doesn't change string length)
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            text = f.read().lower()
    except OSError as err:
        raise OSError(f"An error occurred while reading the file: {err}")

    # Exact whole-word match for keyword (supports spaces)
    pattern = r"\b" + re.escape(keyword_norm) + r"\b"
    match = re.search(pattern, text)
    return match.start() if match else -1

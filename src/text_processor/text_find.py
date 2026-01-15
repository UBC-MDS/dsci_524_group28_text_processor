"""
A module that reads a text file to locate the first occurrence of 'keyword' in text and returns its character index.

Note: The returned index refers to the cleaned (lowercased) text, not the raw
file text. Because normalization can remove characters/words, indices may not match
the original file.
"""
import re

def text_find(input_path: str, keyword: str) -> int:
    """
    Finds the first whole-word instance of `keyword` in a text file.

    Both file text and keyword are lowercased before searching. Keyword must be
    a non-empty string containing only letters and spaces (e.g. "anna lee").

    Returns the 0-based character index of the first occurrence in the normalized
    text, or -1 if not found.

    Raises
    ------
    TypeError
        If `keyword` is not a string.
    ValueError
        If `keyword` is empty or contains characters other than letters and spaces.
    FileNotFoundError, PermissionError, IsADirectoryError, UnicodeDecodeError
        If the file cannot be opened/read as text.
    """
    if not isinstance(keyword, str):
        raise TypeError("keyword must be a string")

    keyword_norm = keyword.strip().lower()
    if keyword_norm == "":
        raise ValueError("keyword must be a non-empty string")

    if not re.fullmatch(r"[A-Za-z ]+", keyword_norm):
        raise ValueError("keyword must contain only letters and spaces")

    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read().lower()

    pattern = r"\b" + re.escape(keyword_norm) + r"\b"
    match = re.search(pattern, text)
    return match.start() if match else -1
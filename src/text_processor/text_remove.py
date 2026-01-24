"""
A module that provides functionality to remove a specified word from a text file.
"""

from __future__ import annotations

import os
import re


def text_remove(input_path: str, output_path: str, string_to_remove: str) -> None:
    """Remove all occurrences of a whole word from a text file and write to a new file.

    The function reads the input file using UTF-8 encoding, removes every occurrence
    of ``string_to_remove`` as a whole word (not as a substring), and writes the resulting
    text to the output file using UTF-8 encoding.

    Parameters
    ----------
    input_path : str
        Path to the input text file. Must be a string ending with ``.txt``.
    output_path : str
        Path to write the processed text file. Must be a string ending with ``.txt``.
        If ``input_path`` and ``output_path`` are the same, the input file will be
        overwritten.
    string_to_remove : str
        The word to remove from the input text. Must be a non-empty string.

    Returns
    -------
    None
        Writes output to file and returns ``None``.

    Raises
    ------
    TypeError
        If ``input_path`` or ``output_path`` is not a string, or if
        ``string_to_remove`` is not a string.
    ValueError
        If a path does not end with ``.txt`` or if ``string_to_remove`` is empty.
    FileNotFoundError
        If the input file does not exist, or if the output directory does not exist.
    OSError
        If an error occurs during file reading/writing.

    Examples
    --------
    >>> text_remove("example.txt", "removed.txt", "the")
    """
    if not isinstance(input_path, str) or not isinstance(output_path, str):
        raise TypeError("Both input_path and output_path must be strings")
    if not isinstance(string_to_remove, str):
        raise TypeError("string_to_remove must be a string")

    if not input_path.endswith(".txt") or not output_path.endswith(".txt"):
        raise ValueError("Both input_path and output_path must have a .txt file extension")

    if string_to_remove == "":
        raise ValueError("string_to_remove must be a non-empty string")

    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"The input file '{input_path}' is not found")

    output_dir = os.path.dirname(output_path)
    if output_dir != "" and not os.path.isdir(output_dir):
        raise FileNotFoundError(f"The output directory '{output_dir}' does not exist")

    pattern = r"\b" + re.escape(string_to_remove) + r"\b"

    try:
        with open(input_path, "r", encoding="utf-8") as f_in:
            lines = f_in.readlines()

        with open(output_path, "w", encoding="utf-8") as f_out:
            for line in lines:
                f_out.write(re.sub(pattern, "", line))

    except OSError as e:
        raise OSError(f"Error reading from or writing to files: {e}") from e

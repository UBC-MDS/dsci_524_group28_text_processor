from __future__ import annotations

from pathlib import Path
from typing import Iterable, Union


def remove_strings(
    input_path: Union[str, Path],
    targets: Union[str, Iterable[str]],
    output_path: Union[str, Path],
    *,
    case_sensitive: bool = True,
) -> Path:
    """
    Remove specified target word(s) from a text file and write the result to a new file.

    This function removes only *whole-word* matches rather than arbitrary substrings.
    A target is considered a match only when it appears as a complete word delimited
    by whitespace or punctuation. Substrings within larger words are not removed.

    The function is intended to be implemented using explicit loops (e.g., iterating
    over lines and words) instead of relying on a single built-in string replacement
    wrapper.

    Parameters
    ----------
    input_path : str or pathlib.Path
        Path to the input text file.
    targets : str or Iterable[str]
        One target word or a collection of target words to remove.
        For example, targets could be ["cat", "dog"].
    output_path : str or pathlib.Path
        Path to write the processed text file after removal.
    case_sensitive : bool, default=True
        Whether matching should be case-sensitive. If False, words are matched
        in a case-insensitive manner.

    Returns
    -------
    pathlib.Path
        The path to the output file that was written.

    Raises
    ------
    FileNotFoundError
        If the input file does not exist.
    ValueError
        If targets is empty or contains only empty strings.
    TypeError
        If input_path or output_path is not path-like, or if targets has
        an invalid type.

    Examples
    --------
    >>> # Suppose "input.txt" contains: "category cat catalog"
    >>> remove_strings("input.txt", "cat", "output.txt")
    PosixPath('output.txt')
    >>> # The output file contains: "category  catalog"
    """
    pass

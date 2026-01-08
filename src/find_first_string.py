def find_first_string(text_path: str, keyword str) -> int:
    """
    Finds the first instance of a string in a text file.

    This function reads a text file from the provided path and returns the
    character index of the first occurrence of `keyword`. If the string is not
    found, it returns -1.

    Parameters
    ----------
    text_path : str
        Path to the text file to search.
    keyword : str
        The string to find within the text file.

    Returns
    -------
    int
        Character index of the first occurrence of `keyword`, or -1 if not found.

    Examples
    --------
    >>> find_first_string("sample.txt", "hello")
    10
    >>> find_first_string("sample.txt", "not_here")
    -1
    """
    pass
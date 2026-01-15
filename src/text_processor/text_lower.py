"""
A module that reads a UTF-8 text file, converts all uppercase characters to lowercase, then writes the output to a new file.
"""

def text_lower(input_path: str, output_path: str):
    """
    Converts all characters in a text file to lowercase, then writes the result into another file.
    
    Parameters
    ----------
    input_path : str
        Path to the input text file. Must be a string ending with .txt
    output_path : str
        Path to write the processed text file. Must be a string ending with .txt. If input and output paths are the same, the input file will be overwritten.

    Returns
    -------
    None
        Function writes directly to a UTF-8 file and returns None.

    Raises
    ------
    FileNotFoundError
        If the input file does not exist.
    TypeError
        If input_path or output_path is not a string.
    ValueError
        If input_path or output_path does not have a .txt file extension.
    OSError
        If there is an error reading from or writing to the file.

    Examples
    --------
    >>> text_lower("example.txt", "example_lower.txt")
    """
    pass
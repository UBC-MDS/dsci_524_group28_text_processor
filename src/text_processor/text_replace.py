"""
A module that reads a text file, replaces all instances of a string
with another string, then writes the output to a new file.
"""

def text_replace(input_path: str, output_path: str, old: str, new: str):
    """
    Replaces all instances of a string with another string in a text
    file, then writes the result into another file.
    
    Parameters
    ----------
    input_path : str
        The file path to the text file to read.
    output_path : str
        The file path to write the replaced text to.
    old : str
        The string to replace.
    new: str
        The replacement string.

    Returns
    -------
    None

    Examples
    --------
    >>> text_replace("example.txt", "replaced.txt", "color", "colour")
    """
    pass

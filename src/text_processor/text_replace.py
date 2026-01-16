"""
A module that reads a text file, replaces all instances of a string
with another string, then writes the output to a new file.
"""

def text_replace(input_path: str, output_path: str, old: str, new: str):
    """
    Replaces all instances of a string with another string in a text
    file, then writes the result into another file. If the old string does
    not exist in the file, then the output will be the same unaltered file.
    
    Parameters
    ----------
    input_path : str
        An existing file path to the text file to read. The file must be
        readable.
    output_path : str
        The file path to write the replaced text to. The file, should it
        exist, must be writeable.
    old : str
        A (non-empty) string to replace.
    new: str
        The replacement string.

    Returns
    -------
    None

    Examples
    --------
    >>> text_replace("example.txt", "replaced.txt", "color", "colour")
    # replaced.txt contains the contents of example.txt, but with all
    # instances of 'color' replaced with "colour"
    """
    pass

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

    Raises
    ------
    TypeError
        If input_path, output_path, old, or new is not a string.
    ValueError
        If old is an empty string, or the input_path or output_path are not
        paths to .txt files.

    Examples
    --------
    >>> text_replace("example.txt", "replaced.txt", "color", "colour")
    # replaced.txt contains the contents of example.txt, but with all
    # instances of 'color' replaced with "colour"
    """
    
    if not isinstance(input_path, str):
        raise TypeError("input_path must be a string")
    if not isinstance(output_path, str):
        raise TypeError("output_path must be a string")
    if not isinstance(old, str):
        raise TypeError("old must be a string")
    if not isinstance(new, str):
        raise TypeError("new must be a string")
    
    if old == "":
        raise ValueError("old must be a non-empty string")
    
    if not input_path.endswith(".txt"):
        raise ValueError("input_path must be a .txt file")
    if not output_path.endswith(".txt"):
        raise ValueError("output_path must be a .txt file")
    
    with open(input_path, "r", encoding="utf-8") as f:
        input = f.read()

    result = []
    old_len = len(old)
    i = 0

    while i < len(input):
        if input[i:i + old_len] == old:
            result.append(new)
            i += old_len
        else:
            result.append(input[i])
            i += 1


    with open(output_path, "w", encoding="utf-8") as f:
        f.write("".join(result))

    return

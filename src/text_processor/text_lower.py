import os

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
    TypeError
        If input_path or output_path is not a string.
    ValueError
        If input_path or output_path does not have a .txt file extension.
    FileNotFoundError
        If the input file does not exist.
    OSError
        If there is an error reading from or writing to the file.

    Examples
    --------
    >>> text_lower("example.txt", "example_lower.txt")
    """
    # FileNotFoundError exception
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"The input file '{input_path}' does not exist.")

    # TypeError exception if not string for input_path and output_path
    if not isinstance(input_path, str) or not isinstance(output_path, str):
        raise TypeError("Both input_path and output_path must be strings.")

    # ValueError exception if not .txt extension for input_path and output_path
    if not input_path.endswith('.txt') or not output_path.endswith('.txt'):
        raise ValueError("Both input_path and output_path must have a .txt file extension.")

    try:
        with open(input_path, 'r', encoding='utf-8') as infile:
            # read entire file contents as str
            content = infile.read()
        
            while True:
                # read one char at a time
                char = infile.read(1)
                # break loop if end of str reached
                if not char:
                    break
        
        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.write(char.lower())
    
    # OSError exception for read/write issues
    except OSError as err:
        raise OSError(f"An error occurred while reading or writing files: {err}")
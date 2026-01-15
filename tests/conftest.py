import pytest
import os


@pytest.fixture
def output_data():
    file_path = "tests/output.txt"
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write("")
    with open(file_path, "r") as file:
        lines = file.read()
    return lines

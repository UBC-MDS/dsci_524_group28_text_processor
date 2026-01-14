import pytest


@pytest.fixture
def output_data():
    file_path = "tests/output.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines

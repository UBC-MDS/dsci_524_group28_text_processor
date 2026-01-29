# Welcome to Text Processor

|        |        |
|--------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/text-processor.svg)](https://test.pypi.org/project/text-processor/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/text-processor.svg)](https://test.pypi.org/project/text-processor/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

|        |        |
|--------|--------|
| CI/CD  | [![CI](https://github.com/UBC-MDS/dsci_524_group28_text_processor/actions/workflows/build.yml/badge.svg)](https://github.com/UBC-MDS/dsci_524_group28_text_processor/actions/workflows/build.yml) [![codecov](https://codecov.io/gh/UBC-MDS/dsci_524_group28_text_processor/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/dsci_524_group28_text_processor) |
| Package | [![Supported Python Versions](https://img.shields.io/pypi/pyversions/text-processor.svg)](https://test.pypi.org/project/text-processor/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

`text_processor` is a package that assists in the processing of text files in Python. This allows users to generate insights on and clean raw text data without needing to manually read the file or write the text to a new file, and is particularly useful in cases where users only need to perform a simple operation on the text file.

The package consists of the following functions:

- `text_lower`:
  - This function converts all characters in a text file to lower case and writes it to a specified file.
- `text_find`:
  - This function finds the index of the first instance of a specified string in a text file. If the string does not exist in the file, it will return -1.
- `text_remove`:
  - This function removes all instances of a specified string in a text file, then writes it to a new file.
- `text_replace`:
  - This function replaces all instances of a specified string in a text file with another string, then writes it to a new file.

## `text_processor` in the Python Ecosystem

The functions in `text_processor` are analogous to built-in string methods in the [Python standard library](https://docs.python.org/3/library/index.html) such as `str.lower()`, `str.find()`, and `str.replace()`. They are differentiated by how they are built to handle text files specifically, directly reading from and writing to files rather than working directly with the text as strings.

## Documentation

Our online documentation can be found [here](https://ubc-mds.github.io/dsci_524_group28_text_processor/).

## Get started

### Cloning the Repository

Clone this GitHub repository and navigate to the project folder using the following commands:

```bash
git clone https://github.com/UBC-MDS/dsci_524_group28_text_processor.git
cd dsci_524_group28_text_processor
```

### Setting Up the Development Environment

Create and activate the development environment using the `environment.yml` file:

```bash
conda env create -f environment.yml
conda activate 524
```

### Installing the Package

To install the package locally for testing, use the following command while in the root directory:

```bash
pip install -e .
```

To instead install the package from TestPyPI, use the following command:

```bash
pip install -i https://test.pypi.org/simple/ text-processor
```

### Running the Tests

Run the tests using the following command while in the root directory:

```bash
pytest
```

### Building the Documentation

After installing `text_processor`, the documentation can be built using Hatch with the following command:

```bash
quartodoc build
```

### Deploying the Documentation

The documentation is automatically rendered and deployed once updates are pushed to the deployment branch.

## Contributors

- Aitong Wu
- Christine Chow
- Julia Zhang
- Vy Phan

## Copyright

- Copyright © 2026 Julia Zhang, Vy Phan, Aitong Wu, Christine Chow.
- Free software distributed under the [MIT License](./LICENSE).

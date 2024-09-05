# Course: Create an Open-Source Project in Python (By: Cheuk Ting Ho)

SOURCE: https://www.linkedin.com/learning/create-an-open-source-project-in-python?dApp=59033956&leis=LAA

## Setup

NOTE: Different than standard pip installs

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

Check using

```sh
poetry --version
```

Setup project

```sh
poetry init
```

Add `export PATH="/Users/horus/.local/bin:$PATH"` to your shell configuration file.

Enter poetry shell (similar to conda activate environment_name)

```sh
poetry shell
```

Running a python file using poetry environment

```sh
poetry run python ch02_pytest.py
poetry run pytest test_ch02_pytest.py -s -v -l
```

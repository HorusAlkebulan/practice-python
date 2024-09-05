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

Check exit code of last command

```sh
echo $?
```

Sample command history

```sh
(open-source-projects-python-py3.10) (base) horus@Horuss-Mac-Studio-2023 open_source_projects_python % history
  992  pytest -s
  993  pytest -s
  994  pytest -s
  995  flake8 --version
  996  flake8
  997  black reminder.py
  998  flake8
  999  black ch02_pytest.py
 1000  black test_*.py
 1001  git add .
 1002  git commit -m "black formatting"
 1003  git push
 1004  pre-commit --version
 1005  pre-commit install
 1006  pre-commit run --all-files
 1007  git commit -a -m "test pre-commit"
```

running coverage

```sh
coverage run -m pytest .
coverage report --omit=test_ch02_pytest.py
coverage xml --omit=test_ch02_pytest.py
```

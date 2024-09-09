# practice-python

Practice sandbox for python based code

## Initial setup on mac

1. Install miniconda

```bash
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

After installing, initialize your newly-installed Miniconda. The following commands initialize for bash and zsh shells:

```bash
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```

2. create environment

```bash
conda create -n practice-python python=3.10
conda activate practice-python
```

3. install pytorch and any other needed tools

```bash
pip install -r requirements.txt
```

## Testing

* Run all tests, showing locals, stopping on first error, first level verbose

```bash
pytest -l -x -v
```

* Run tests with coverage

```bash
pytest --cov=ch01_stack.py -v
pytest --cov=<your_module_or_package> --cov-report=term-missing --cov-fail-under=90
pytest test.py --cov=sample.py --cov-report=
coverage report -m
```

## Code Formatting

Run black and isort

```sh
isort . && black -v .
```

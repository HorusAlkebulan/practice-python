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
conda create -n pytorch pytorch
conda activate pytorch 
```

3. install pytorch and any other needed tools

```bash
conda install jupyter_core -c conda-forge
conda install -c pytorch torchtext
```

4. installing legacy capable TREC

```bash
conda install -c pytorch torchtext=0.8.1
```

## Testing

* Run all tests, showing locals, stopping on first error, first level verbose

```bash
pytest -l -x -v
```
# Divorce Predictor

![version 0.1.0][img_version]
![python 3.7.1 | 3.8 | 3.9][python_version]

[img_version]: https://img.shields.io/static/v1.svg?label=version&message=0.1.0&color=blue
[python_version]: https://img.shields.io/static/v1.svg?label=python&message=3.7.1%20|%203.8%20|%203.9&color=blue

This is a Machine Learning project that is to be used on experimentation tracking and data science training.
The [Divorce Predictors data set](https://archive.ics.uci.edu/ml/datasets/Divorce+Predictors+data+set) is used as a

# How to install

To setup this repository locally for testing and implementation please follow this guidelines. This repository is based on [Python 3.7.1](https://www.python.org/) or above, [Makefile](https://opensource.com/article/18/8/what-how-makefile) and [Poetry](https://python-poetry.org/). **Poetry** is extensively used as a virtual environment manager, if you use other virtual environment manager, double check the orientations and commands that will be showing here.
After cloning this repository, and having poetry and python 3.7.1 or above installed, run the following command for installing this package for common usage:

```sh
make install
```

## Advanced (development)

If your intention is for code development or maintainance, after installing this package apply the command below to install development dependencies and setup pre-commit:

```sh
make dev
```

Other useful command targets available at `Makefile` are:

```sh
poetry run make test-code
```
The command above will run all unit tests. Notice that I'm using poetry to correctly run inside my development virtual environment.

```sh
poetry run make static-analysis
```
Above command will do an static analysis, checking style with flake8 and computing some code complexity statistics. This will also break if style is wrong or code complexity is too high.

```sh
poetry run make coverage
```

Above command will run all unit tests and check that test coverage is above and specified percentage, defined inside `Makefile`.

## Requirement setup

crate .env com variáveis de KAGGLE_KEY, KAGGLE_USERNAME

# How to use this package

##TODO

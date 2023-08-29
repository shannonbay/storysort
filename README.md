# Story Sort
A variation of Merge Sort which works by finding all non-consecutive sorted runs and merging them

## Requirements
Python 3.10

## Setup
```sh
# Install dependencies
pipenv install --dev

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

## Run Unit Tests with Coverage
pipenv run pytest --cov --cov-fail-under=100

## Credits
This package was created with Cookiecutter and the [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter) project template.

[![Pytests](https://github.com/USER/REPO_NAME/actions/workflows/pytests_linting.yml/badge.svg?branch=main)](https://github.com/USER/REPO_NAME/actions/workflows/pytests_linting.yml)

**TO INIT THE PROJECT RUN THE FOLLOWING COMMANDS:**
```bash
poetry init
poetry add --dev pytest-cov
poetry add --dev mypy
pre-commit install
```

# PROJECT_NAME

## Contribute
Please make sure to install the pre-commit hooks before you start working on the project. If you don't have `pre-commit` installed, you can install it in different ways (see [here](https://pre-commit.com/#install)). Once you have `pre-commit` installed, you can install the hooks by running:

```bash
pre-commit install
```

In order to run the test, using the coverage, you can run:
```bash
pytest --cov=src/

# To enable logger output
pytest --cov=src/ -o log_cli=true -o log_cli_level=DEBUG
```

## Installation and usage
The dependencies are managed using [Poetry](https://python-poetry.org/). To install the dependencies, run:
```bash
poetry install
```

To add a development dependency, run:
```bash
poetry add --dev <package>
```

To add a general dependency, run:
```bash
poetry add <package>
```

## Use

To run the project, you can use the following command:
```bash
python src/app.py
```

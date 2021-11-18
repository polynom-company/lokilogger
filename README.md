# Lokilogger

## Introduction

This package is just a wrapper around [logging](https://docs.python.org/3/library/logging.html) and [colorlog](https://github.com/borntyping/python-colorlog).

## Installation

```shell
pip install lokilogger
```

## Usage

Init LokiLogging.

```python
logging = LokiLogging()
```

Set multiple loggers.

```python
logger1 = logging.setLogger("testlogger1")

DEFAULT_FORMATTER = '"severity": "%(levelname)s", , "message": "%(message)s"'

# Set logger with custom formatter
logger2 = logging.setLogger("testlogger2",DEFAULT_FORMATTER)
```

Disable color.

```python
logging.disableColor("testlogger1")
```

Enable color.

```python
logging.enableColor("testlogger1")
```

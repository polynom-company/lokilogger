# Lokilogger

## Introduction

This package is just a wrapper around [logging](https://docs.python.org/3/library/logging.html) and [colorlog](https://github.com/borntyping/python-colorlog).

## Installation

```shell
pip install lokilogger
```

## Usage

At the start of your program

```python
from lokilogger.logging import set_log_mode
import logging

env = os.getenv("LOGMODE", "DEV")
set_log_mode("env") # A global setting here, you can set it to `PROD`, `DEV`or `DEV_NO_COLOR`
```

Use it in other modules

```python
logger = logging.getLogger(__name__)
logger.error('error message')
```

Output

env=Prod

```shell
"time": "2022-01-15 07:56:05,440, ""severity": "INFO", "logger": "root","module": "logging", "message": "Dev env is set to production"
"time": "2022-01-15 07:56:05,440, ""severity": "ERROR", "logger": "__main__","module": "test", "message": "error message"
"time": "2022-01-15 07:56:05,440, ""severity": "INFO", "logger": "root","module": "test", "message": "error message"
```

env=DEV_NO_COLOR

```shell
2022-01-15 07:54:40,039 | INFO | root | Dev env is set to development without colorlog
2022-01-15 07:54:40,039 | ERROR | __main__ | error message
2022-01-15 07:54:40,039 | INFO | root | error message
```

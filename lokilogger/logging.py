import colorlog
import logging
DEFAULT_FORMATTER_COLOR = '%(log_color)s"severity": "%(levelname)s", "logger": "%(name)s","module": "%(module)s", "message": "%(message)s"'
DEFAULT_FORMATTER = '"severity": "%(levelname)s", "logger": "%(name)s","module": "%(module)s", "message": "%(message)s"'


class LokiLogging:
    """This a custom `logging` for `Loki`.
    """

    def __init__(self):
        """Init LokiLogging which will initialize an empty dictioary of loggers.
        """
        self.loggers = dict()

    def getLogger(self, name: str) -> logging.Logger:
        """Get a logger by its name.

        Args:
            name (str): A logger's name.

        Returns:
            logging.Logger: Return `logging.Logger` object.
        """
        try:
            return self.loggers[name]
        except KeyError:
            raise Exception(f'Logger {name} doesn\'t exist')

    def setLogger(self, name: str, custom_formatter=DEFAULT_FORMATTER_COLOR) -> logging.Logger:
        """Set a logger by giving a name.

        Args:
            name (str): A new logger's name.
            custom_formatter (str, optional): Setup a custom formatter which will overwrite the default one. Defaults to DEFAULT_FORMATTER_COLOR.

        Returns:
            logging.Logger: Return `logging.Logger` object.
        """
        logger = colorlog.getLogger(name)
        handler = logging.StreamHandler()
        handler.setFormatter(colorlog.ColoredFormatter(
            custom_formatter))
        logger.addHandler(handler)
        self.loggers[name] = logger
        return logger

    def disableColor(self, name: str, custom_formatter=DEFAULT_FORMATTER) -> logging.Logger:
        """Disable Colors.

        Args:
            name (str): The logger's name.
            custom_formatter (str, optional): Setup a custom formatter which will overwrite the default one. Defaults to DEFAULT_FORMATTER.

        Returns:
            logging.Logger: Return `logging.Logger` object.
        """
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(custom_formatter))
        logger = self.getLogger(name)
        logger.removeHandler(logger.handlers[0])
        logger.addHandler(handler)
        return logger

    def enableColor(self, name: str, custom_formatter=DEFAULT_FORMATTER_COLOR) -> logging.Logger:
        """Enable Colors.

        Args:
            name (str): The logger's name.
            custom_formatter (str, optional): Setup a custom formatter which will overwrite the default one. Defaults to DEFAULT_FORMATTER_COLOR.

        Returns:
            logging.Logger: Return `logging.Logger` object.
        """
        handler = logging.StreamHandler()
        handler.setFormatter(colorlog.ColoredFormatter(custom_formatter))
        logger = self.getLogger(name)
        logger.removeHandler(logger.handlers[0])
        logger.addHandler(handler)
        return logger

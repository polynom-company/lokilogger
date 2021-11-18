from lokilogger.logging import LokiLogging
logging = LokiLogging()
logger1 = logging.setLogger("testlogger1")

DEFAULT_FORMATTER = '"severity": "%(levelname)s", , "message": "%(message)s"'

# Set logger with custom formatter
logger2 = logging.setLogger("testlogger2", DEFAULT_FORMATTER)

logger1.info("This is an debug message")

logging.disableColor("testlogger1")

logger1.warning("This is an warning message")

logging.enableColor("testlogger1")

logger1.warning("This is an warning message")

logger2.warning("This is an warning message")

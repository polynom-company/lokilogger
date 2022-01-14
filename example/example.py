from lokilogger.logging import setLogMode
import logging

setLogMode("DEV")
logger = logging.getLogger(__name__)
logger.error('error message')

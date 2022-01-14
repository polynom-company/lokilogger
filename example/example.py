from lokilogger.logging import set_log_mode
import logging

set_log_mode("DEV")
logger = logging.getLogger(__name__)
logger.error('error message')

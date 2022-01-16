import logging
import pkg_resources

def set_log_mode(mode:str):
    """Set logging mode

    Args:
        mode (str): PROD, DEV or DEV_NO_COLOR
    """
    path = "config.ini"
    filepath = pkg_resources.resource_filename(__name__, path)
    logging.config.fileConfig(filepath)
    logger = logging.getLogger()
    prod = logger.handlers[0]
    dev = logger.handlers[1]
    color = logger.handlers[2]
    mode = mode.upper()
    if mode == "PROD":
        logger.removeHandler(dev)
        logger.removeHandler(color)
        logger.info(f"Dev env is set to production")
    elif mode == "DEV_NO_COLOR":
        logger.removeHandler(color)
        logger.removeHandler(prod)
        logger.info(f"Dev env is set to development without colorlog")
    else:
        logger.removeHandler(prod)
        logger.removeHandler(dev)
        if mode!= "DEV":
            logger.warning(f"Unrecognized mode, default to development")
        logger.info(f"Dev env is set to development")
        
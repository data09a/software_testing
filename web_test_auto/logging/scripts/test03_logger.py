
import logging


logger = logging.getLogger()

logger.setLevel(logging.INFO)


sh = logging.StreamHandler()

logger.addHandler(sh)


logger.info("info")
logger.debug("debug")
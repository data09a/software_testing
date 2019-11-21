import logging

fm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=fm)

logging.debug("this is a debug...")
logging.info("this is a info...")
logging.warning("this is a warning...")
logging.error("this is a error...")
logging.critical("this is a critical...")




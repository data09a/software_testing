# 导包
import logging


fm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=fm, filename="../log/log01.log")

logging.debug("click the element")

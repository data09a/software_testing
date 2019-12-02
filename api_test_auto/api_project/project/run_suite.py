import unittest
import time
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./case", pattern="test*.py")
file_path = "./report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))

with open(file_path, "wb") as f:
    HTMLTestRunner(stream=f).run(suite)
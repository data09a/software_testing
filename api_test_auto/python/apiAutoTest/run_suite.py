
import unittest
import time

from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./case")

report_path = "./report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))

with open(report_path, "wb") as f:

    HTMLTestRunner(stream=f, title="Test Automation Login Report", description="Operation System：mac")\
        .run(suite)
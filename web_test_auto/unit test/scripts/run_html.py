
import unittest

import time

from HTMLTestRunner import HTMLTestRunner


suite = unittest.defaultTestLoader.discover("../case", pattern="test*.py")

report_dir = "../report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))

with open(report_dir, "wb") as f:
    HTMLTestRunner(stream=f,
                   title="Test Automation Report",
                   description="Operation System  MacOS").run(suite)
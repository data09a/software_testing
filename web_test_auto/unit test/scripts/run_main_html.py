from tools.HTMLTestRunner import HTMLTestRunner

import unittest

suite = unittest.defaultTestLoader.discover("./", pattern="test02*.py")

with open("../report/report.html", "wb") as f:
    HTMLTestRunner(stream=f).run(suite)

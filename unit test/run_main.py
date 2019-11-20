
import unittest

from test01_testcase import Test01


suite = unittest.TestSuite()


suite.addTest(unittest.makeSuite(Test01))


runner = unittest.TextTestRunner()
runner.run(suite)
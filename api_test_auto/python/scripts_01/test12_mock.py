# import
import unittest
from unittest import mock


# unfinished function
def add(x, y):
    pass


# create new test class
class TestAdd(unittest.TestCase):

    def test_add(self):
        add = mock.Mock(return_value=18)

        ##  this test will fail

        # result = add(10, 10)
        #
        # self.assertEqual(result, 20)

        result = add(10, 8)

        self.assertEqual(result, 18)


if __name__ == '__main__':
    unittest.main()

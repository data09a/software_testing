import unittest



def add(x, y):
    return x+y


class Test01(unittest.TestCase):

    def test_add(self):
        result = add(1, 1)
        print("Result：", result)

    def test_add02(self):
        result = add(1, 2)
        print("Result：", result)
        print("__name__module：", __name__)

    def eest_add03(self):
        result = add(1, 2)
        print("Result：", result)


if __name__ == '__main__':
    unittest.main()
import unittest



def add(x, y):
    return x+y


class Test01(unittest.TestCase):

    def test_add(self):
        result = add(1, 1)
        print("结果为：", result)

    def test_add02(self):
        result = add(1, 2)
        print("结果为：", result)
        print("__name__内置变量获取当前运行的模块名称：", __name__)

    def eest_add03(self):
        result = add(1, 2)
        print("结果为：", result)


if __name__ == '__main__':
    unittest.main()
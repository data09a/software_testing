class A:

    def __init__(self):

        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("private method %d %d" % (self.num1, self.__num2))

    def test(self):
        print("parent class method %d" % self.__num2)

        self.__test()


class B(A):

    def demo(self):

        print("subclass %d" % self.num1)

        self.test()
        pass

b = B()
print(b)

b.demo()
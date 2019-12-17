class A:

    def __init__(self):

        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("private method %d %d" % (self.num1, self.__num2))


class B(A):

    def demo(self):
        pass

b = B()
print(b)

b.demo()
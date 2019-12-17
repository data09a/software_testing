class A:

    def test(self):
        print("A --- test method")

    def demo(self):
        print("A --- demo method")


class B:

    def test(self):
        print("B --- test method")

    def demo(self):
        print("B --- demo method")


class C(B, A):
    pass


c = C()

c.test()
c.demo()

print(C.__mro__)
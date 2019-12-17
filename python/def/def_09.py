class A:

    def test(self):
        print("test method")


class B:

    def demo(self):
        print("demo method")


class C(A, B):
    pass


c = C()

c.test()
c.demo()
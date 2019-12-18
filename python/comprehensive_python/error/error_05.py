def demo1():
    return int(input("input integer: "))


def demo2():
    return demo1()


try:
    print(demo2())
except Exception as result:
    print("unknown error %s" % result)

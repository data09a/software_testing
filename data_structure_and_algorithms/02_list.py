import timeit


def t1():
    li = []
    for i in range(1000):
        li.append(i)


def t2():
    li = []
    for i in range(1000):
        li = li + [i]


def t3():
    li = [i for i in range(1000)]


def t4():
    li = list(range(1000))

def t5():
    li = []
    for i in range(10000):
        li.insert(0, i)


timer1 = timeit.Timer("t1()", "from __main__ import t1")
timer2 = timeit.Timer("t2()", "from __main__ import t2")
timer3 = timeit.Timer("t3()", "from __main__ import t3")
timer4 = timeit.Timer("t4()", "from __main__ import t4")
timer5 = timeit.Timer("t5()", "from __main__ import t5")


print("append: %f" % timer1.timeit(number=100))
print("[]+ []: %f" % timer2.timeit(number=100))
print("[i for]: %f" % timer3.timeit(number=100))
print("list(): %f" % timer4.timeit(number=100))
print("insert_start: %f" % timer5.timeit(number=100))


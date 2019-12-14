class Person:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "My name is  %s weight %.2f pounds" % (self.name, self.weight)

    def run(self):
        print("%s likes to run, running is a good exercise" % self.name)

        self.weight -= 0.5

    def eat(self):
        print("%s likes to eat cake." % self.name)

        self.weight += 1


tom = Person("Tom", 145.0)

tom.run()
tom.eat()

linda = Person("Linda", 105)

linda.eat()
linda.run()

print(tom)
print(linda)
class Person:

    def __init__(self, name, weight):

        self.name = name
        self.weight = weight

    def __str__(self):

        return "My name is %s weight %.2f pounds" % (self.name, self.weight)

    def run(self):
        print("%s likes running，running is a good exercise" % self.name)

        self.weight -= 0.5

    def eat(self):
        print("%s likes to eat all kinds of food" % self.name)

        self.weight += 1

john = Person("John", 185.0)


print(john)
john.eat()
john.run()



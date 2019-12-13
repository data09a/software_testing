class Cat:

    def __init__(self, new_name):
        self.name = new_name

    def eat(self):
        print("%s likes to eat fish" % self.name)


tom = Cat("Tom")

print(tom.name)

lazy_cat = Cat("Lazy Cat")
lazy_cat.eat()

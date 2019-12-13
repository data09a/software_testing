class Cat:

    def __init__(self):

        self.name = "Tom"

    def eat(self):
        print("%s likes to eat fish" % self.name)


tom = Cat()

print(tom.name)

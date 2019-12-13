class Cat:

    def eat(self):
        print("%s likes to eat fish" % self.name)

    def drink(self):
        print("%s needs water" % self.name)


tom = Cat()

tom.name = "Tom"

tom.eat()
tom.drink()
tom.name = "Tom"

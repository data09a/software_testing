class Cat:
    def eat(self):
        print("%s likes to eat fish" % self.name)

    def drink(self):
        print("%s needs water" % self.name)


tom = Cat()

tom.name = "Tom"

tom.eat()
tom.drink()

print(tom)

lazy_cat = Cat()
lazy_cat.name = "Lazy Cat"

lazy_cat.eat()
lazy_cat.drink()

print(lazy_cat)

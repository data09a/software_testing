class animal:

    def eat(self):
        print("Eat---")

    def drink(self):
        print("Drink---")

    def run(self):
        print("Run---")

    def sleep(self):
        print("Sleep---")


class dog(animal):

    def bark(self):
        print("bark bark")


rufus = dog()

rufus.eat()
rufus.drink()
rufus.run()
rufus.sleep()
rufus.bark()

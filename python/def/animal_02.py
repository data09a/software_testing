class Animal:

    def eat(self):
        print("eat---")

    def drink(self):
        print("drink---")

    def run(self):
        print("run---")

    def sleep(self):
        print("sleep---")


class Dog(Animal):

    def bark(self):
        print("bark bark")


tom = Dog()

tom.eat()
tom.drink()
tom.run()
tom.sleep()
tom.bark()

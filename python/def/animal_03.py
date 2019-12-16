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

class Jack(Dog):

    def jump(self):
        print("I can jump")


jack = Jack()

jack.jump()
jack.bark()
jack.eat()

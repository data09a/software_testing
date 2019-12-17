class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s running around..." % self.name)


class Tom(Dog):

    def game(self):
        print("%s jumping around..." % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s and %s are playing..." % (self.name, dog.name))

        dog.game()


tom = Tom("little Tom")

jack = Person("Jack")

jack.game_with_dog(tom)
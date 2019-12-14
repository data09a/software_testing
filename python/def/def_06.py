class Cat:

    def __init__(self, new_name):
        self.name = new_name

        print("%s is here" % self.name)

    def __del__(self):

        print("%s is leaving" % self.name)

    def __str__(self):

        return "I am a cat[%s]" % self.name


tom = Cat("Tom")
print(tom)

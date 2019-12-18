class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):

        print("create object, distribute space ")

        instance = super().__new__(cls)

        return instance

    def __init__(self):
        print("start the player")


player = MusicPlayer()

print(player)
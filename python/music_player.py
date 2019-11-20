class MusicPlayer(object):


    instance = None

    # set flag type
    init_flag = False

    def __new__(cls, *args, **kwargs):


        if cls.instance is None:

            cls.instance = super().__new__(cls)


        return cls.instance

    def __init__(self):


        if MusicPlayer.init_flag:
            return


        print("Start the player")

        # modify the flag type
        MusicPlayer.init_flag = True

# set objects
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)

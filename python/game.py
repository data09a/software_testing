class Game(object):

    top_score = 90

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("Help：information line")

    @classmethod
    def show_top_score(cls):
        print("History %d" % cls.top_score)

    def start_game(self):
        print("%s start game..." % self.player_name)


Game.show_help()

Game.show_top_score()

game = Game("John")

game.start_game()
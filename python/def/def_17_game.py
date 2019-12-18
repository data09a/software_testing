class Game(object):
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("Help info: get in the door")

    @classmethod
    def show_top_score(cls):
        print("History record %d" % cls.top_score)

    def start_game(self):
        print("%s start game..." % self.player_name)


Game.show_help()

Game.show_top_score()

game = Game("Jack")

game.start_game()
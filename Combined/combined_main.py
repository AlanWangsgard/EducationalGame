from game.director import Director
from game.mathQuestionView import MathQuestionView
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH
import arcade

class Conductor():
    def __init__(self):
        self.main()

    def main(self):
        self.window = arcade.Window(
            SCREEN_WIDTH, SCREEN_HEIGHT, "The Best Team ")
        game = Director(self.window)
        game.setup()
        self.window.Frogger = game
        self.window.math_game = MathQuestionView(self.window)
        self.window.show_view(self.window.Frogger)
        arcade.run()


Conductor()
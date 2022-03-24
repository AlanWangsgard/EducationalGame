from game.director import Director
from game.mathQuestionView import MathQuestionView
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from menu import Menu
from endscreen import EndScreen
<<<<<<< HEAD
=======
from mid_screen import MidScreen
from bee_game.game import BeeGame
>>>>>>> 7b391b9706eb6c4f4f965c4ba3fecd8dc247cc23
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
        self.window.menu = Menu(self.window)
        self.window.math_game = MathQuestionView(self.window)
        self.window.endscreen = EndScreen(self.window)
<<<<<<< HEAD
=======
        self.window.mid_screen = MidScreen(self.window)
        self.window.BeeGame = BeeGame(self.window)
>>>>>>> 7b391b9706eb6c4f4f965c4ba3fecd8dc247cc23
        self.window.playerScore = 0
        self.window.show_view(self.window.menu)
        arcade.run()


Conductor()
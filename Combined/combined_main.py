from game.director import Director
from game.mathQuestionView import MathQuestionView
from game.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from score.frogger_local_db import FroggerLocalDB
from menu import Menu
from endscreen import EndScreen
from mid_screen import MidScreen
from bee_game.game import BeeGame
import arcade

class Conductor():
    def __init__(self):
        self.main()

    def main(self):
        self.window = arcade.Window(
            SCREEN_WIDTH, SCREEN_HEIGHT, "The Best Team ")

        localDB = FroggerLocalDB()
        localDB.initializeDB()

        game = Director(self.window)
        game.setup()
        self.window.Frogger = game
        self.window.menu = Menu(self.window)
        self.window.math_game = MathQuestionView(self.window)
        self.window.endscreen = EndScreen(self.window)
        self.window.mid_screen = MidScreen(self.window)
        self.window.BeeGame = BeeGame(self.window)
        self.window.playerScore = 0
        self.window.playerLives = 0
        self.window.playerLevel = 0
        self.window.playerName = "TestPlayer"
        self.window.show_view(self.window.menu)
        arcade.run()


Conductor()
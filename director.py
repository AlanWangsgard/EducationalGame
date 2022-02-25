from Frogger.Frogger.game.director import Director
import arcade
from menu import Menu
from endscreen import EndScreen
WIDTH = 800
HEIGHT = 600

class Conductor():
    def __init__(self):
        self.main()

    def main(self):
        self.window = arcade.Window(
            WIDTH, HEIGHT, "Instruction and Game Over Views Example")
        game = Director(self.window)
        game.setup()
        self.window.menu = Menu(self.window)
        self.window.Frogger = game
        self.window.show_view(self.window.menu)
        self.window.endscreen = EndScreen(self.window)
        self.window.show_view(self.window.endscreen)
        arcade.run()


Conductor()
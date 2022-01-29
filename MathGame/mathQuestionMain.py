from game import constants ### WHEN WE REORGANIZE THE FILESYSTEM, THIS WILL NEED CHANGED
from game.mathQuestionView import MathQuestionView

import arcade

def main():

    # start the game
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, "Answer a Question")
    window.math_view = MathQuestionView()
    window.show_view(window.math_view)
    arcade.run()

if __name__ == "__main__":
    main()

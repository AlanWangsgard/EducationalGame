from ..Frogger.Frogger.game import constants ### WHEN WE REORGANIZE THE FILESYSTEM, THIS WILL NEED CHANGED

import arcade

def main():

    # start the game
    window = arcade.Window(constants.MAX_X, constants.MAX_Y, "Answer a Question")
    window.math_view = MathView()
    window
    window.show_view(window.menu_view)
    arcade.run()

if __name__ == "__main__":
    main()

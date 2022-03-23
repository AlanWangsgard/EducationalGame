"""
Example showing how to draw text to the screen.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.drawing_text
"""
import arcade
import random
from game.constants import FONT_PATH, WORDS

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Drawing Text Example"
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20
COLOR = arcade.color.BLACK
COLOR2 = arcade.color.CEIL




class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BEIGE)

        self.text_angle = 0
        self.time_elapsed = 0.0
        self.turn = 1

    def on_update(self, delta_time):
        self.text_angle += 1
        self.time_elapsed += delta_time

    def on_show(self):
        
        with open(WORDS, "r") as infile:
            self.list_of_words = infile.readlines()
        

        self.word = random.choice(self.list_of_words)
        self.letter = self.word[0]

        self.highlight = ""

        




        
            


    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        # Add the screen title
        counter = 0
        start_x = 0
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5
        
        for letter in self.word:
            arcade.draw_text(letter,
                        start_x + counter,
                        start_y,
                        COLOR,
                        DEFAULT_FONT_SIZE * 2,
                        font_name=FONT_PATH,
                        width=SCREEN_WIDTH,
                        align="center")
            counter += 32.2
        
        counter = 0    
        for letter in self.highlight:
            arcade.draw_text(letter,
                            start_x + counter,
                            start_y,
                            COLOR2,
                            DEFAULT_FONT_SIZE * 2,
                            width=SCREEN_WIDTH,
                            align="center")
            counter += 32.2

       





    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if self.highlight == self.word:
    
            self.word = random.choice(self.list_of_words)
            self.highlight = ""
            
        length = len(self.highlight)
        letter = self.word[length]
        self.highlight += letter
        





def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
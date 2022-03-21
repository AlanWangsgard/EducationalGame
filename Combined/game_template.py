"""
Example showing how to draw text to the screen.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.drawing_text
"""
import arcade
import random

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Drawing Text Example"
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20



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
        
        list_of_words= ["apple", "cat", "dog", "rain", "who", "what", "where", "how", "why"]

        self.word = random.choice(list_of_words)
        self.highlight = ""



        
            


    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        # Add the screen title

        start_x = 0
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5
        for i in self.word:
            arcade.draw_text(self.word,
                            start_x,
                            start_y,
                            arcade.color.RED,
                            DEFAULT_FONT_SIZE * 2,
                            width=SCREEN_WIDTH,
                            align="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if self.highlight == self.word:
            list_of_words= ["apple", "cat", "dog", "rain", "who", "what", "where", "how", "why"]
            self.word = random.choice(list_of_words)
        length = len(self.highlight)
        letter = self.word[length]
        self.highlight += letter




def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
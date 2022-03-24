
import arcade
import random
from bee_game.constants import FONT_PATH, WORD_LIST_PATH

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20
COLOR = arcade.color.BLACK
COLOR2 = arcade.color.APPLE_GREEN




class UpperLetters():
    """
    Main application class.
    """

    def __init__(self):
        
        
        with open(WORD_LIST_PATH, "r") as infile:
            self.list_of_words = infile.readlines()
        

        self.word = random.choice(self.list_of_words)
        self.letter = self.word[0]

        self.highlight = ""
        
            


    def draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
       

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

       

    def highlight_letter(self):

            
        length = len(self.highlight)
        letter = self.word[length]
        self.highlight += letter

    def new_word(self):

       
    
        self.word = random.choice(self.list_of_words)
        self.highlight = ""
    
    def is_next_letter(self, letter):
        length = len(self.highlight)
        next_letter = self.word[length]

        if letter == next_letter:
            return True

        if letter != next_letter:
            return False
        
    
    
    def is_highlight(self,):
        length = len(self.highlight)
        if length == len(self.word):
            return True

        if length != len(self.word):
            return False




        





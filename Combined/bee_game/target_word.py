
import arcade
import random
from bee_game.constants import FONT_NAME, WORD_LIST_PATH, WORD_COLOR, HIGHLIGHT_COLOR, SCREEN_HEIGHT, SCREEN_WIDTH

DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20

class TargetWord():
    """
    displays each word at the top of the screen and highlights each letter
    across the word as the player corectly collides with the letter from the 
    letter_flower class.
    attributes: 
            self.list_of_words: the list of words open and read from the words.txt file
            self.word: the random word taken from the list of words
            self.letter: the word is split into each letter
            self.highlight: the letter of each word copied and drawn over the letter in a new color
    """

    def __init__(self):
        #open word text file and add words to a list 
        with open(WORD_LIST_PATH, "r") as infile:
            self.list_of_words = infile.readlines()
        self.highlight = ""
        
    def draw(self):
        """
        Render the screen.
        """
        #define a counter to be able to seperate each letter the same distance apart to be able to highlight right over top of the letter at the same position
        counter = int(-30 * len(self.word) / 2)
        start_x = SCREEN_WIDTH // 2
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5
        
        #use a loop to access each letter in the word text file and draw the word at the top of the screen
        for index, letter in enumerate(self.word):
            arcade.draw_text(letter,
                        start_x + counter,
                        start_y,
                        HIGHLIGHT_COLOR if index < len(self.highlight) else WORD_COLOR,
                        DEFAULT_FONT_SIZE * 2,
                        font_name= FONT_NAME,
                        width=30,
                        align="center")
            counter += 30

    def highlight_letter(self): 
        #set the length of the word to the same length of the highlight
        length = len(self.highlight)
        letter = self.word[length]
        self.highlight += letter

    def new_word(self):
        #get a new random word from the list of words
        self.word = random.choice(self.list_of_words)[:-1]
        self.highlight = ""
        return self.word
    
    def is_next_letter(self, letter):
        #highlight the next letter in the word by verifying if the user has colided with the correct letter in the word
        length = len(self.highlight)
        next_letter = self.word[length]
        return letter == next_letter
    
    def is_highlighted(self):
        #check to see if the entire word if highlighted by checking the length of the word compared to the length of the highlight
        length = len(self.highlight)
        return length == len(self.word)

    def unhighlight(self):
        self.highlight = ""
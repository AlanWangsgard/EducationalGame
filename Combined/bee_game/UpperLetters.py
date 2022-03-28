
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
        
        #take a random word from the list of words and then take the letter and set highlight to empty
        self.word = random.choice(self.list_of_words)
        self.letter = self.word[0]

        self.highlight = ""
        
            


    def draw(self):
        #define a counter to be able to seperate each letter the same distance apart to be able to highlight right over top of the letter at the same position
        counter = 0
        start_x = 0
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 1.5
        
        #use a loop to access each letter in the word text file and draw the word at the top of the screen
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
        
        #use the same loop to highlight the first letter in the word with the second color by using the same counter and draw over top original letter
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
        #set the length of the word to the same length of the highlight    
        length = len(self.highlight)
        letter = self.word[length]
        self.highlight += letter

    def new_word(self):
        #get a new random word from the list of words
        self.word = random.choice(self.list_of_words)
        self.highlight = ""
    
    def is_next_letter(self, letter):
        #highlight the next letter in the word by verifying if the user has colided with the correct letter in the word
        length = len(self.highlight)
        next_letter = self.word[length]

        if letter == next_letter:
            return True

        if letter != next_letter:
            return False
        
    
    
    def is_highlight(self,):
        #check to see if the entire word if highlighted by checking the length of the word compared to the length of the highlight
        length = len(self.highlight)
        if length == len(self.word):
            return True

        if length != len(self.word):
            return False




        





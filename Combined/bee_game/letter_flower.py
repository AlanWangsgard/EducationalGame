import random
from bee_game.constants import FLOWER_COLORS, SCREEN_HEIGHT, SCREEN_WIDTH, FLOWER_PADDING

class LetterFlower():
    '''
    constructor receives a letter and sets position,
    get_value() : returns the letter it represents,
    set_visible(True/False) : determines whether the letter is visible or not,
    get_x(),
    get_y(), 
    '''
    def __init__(self, letter, x, y):
        # letter is a single-character string

        # Be sure to make sure the x and y value you send me
        # follow these guidelines:
        # FLOWER_PADDING < x < SCREEN_WIDTH - FLOWER_PADDING
        # FLOWER_PADDING < y < SCREEN_HEIGHT - FLOWER_PADDING
        # Distance from this flower to any other is more than FLOWER_PADDING

        assert(type(letter) == str)
        assert(len(letter) == 1)
        assert(FLOWER_PADDING < x < SCREEN_WIDTH - FLOWER_PADDING)
        assert(FLOWER_PADDING < y < SCREEN_HEIGHT - FLOWER_PADDING)

        self.letter = letter
        self.x = x
        self.y = y
        self.visible = True
        self.color = random.choice(FLOWER_COLORS)

    def get_value(self):
        return self.letter

    def set_visible(self, visibility):
        self.visible = visibility

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def draw(self):
        if self.visible:
            #Draw the flower
            #Draw the letter
            # One of the two's color should be self.color
            pass

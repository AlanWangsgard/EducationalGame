import arcade
import random
from bee_game.constants import FLOWER_IMAGES, SCREEN_WIDTH, FLOWER_PADDING, FLOWER_MAX_Y

class LetterFlower(arcade.Sprite):
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
        # FLOWER_PADDING <= x <= SCREEN_WIDTH - FLOWER_PADDING
        # FLOWER_PADDING <= y <= SCREEN_HEIGHT - FLOWER_PADDING
        # Distance from this flower to any other is more than FLOWER_PADDING

        assert(type(letter) == str)
        assert(len(letter) == 1)
        assert(FLOWER_PADDING // 2 <= x <= SCREEN_WIDTH - FLOWER_PADDING // 2)
        assert(FLOWER_PADDING // 2 <= y <= FLOWER_MAX_Y)

        sprite_img = random.choice(FLOWER_IMAGES)
        super().__init__(sprite_img)
        self.letter = letter
        self.center_x = x
        self.center_y = y
        self.visible = True

    def get_value(self):
        return self.letter

    def get_x(self):
        return self.center_x

    def get_y(self):
        return self.center_y

    def draw(self):
        if self.visible:
            #Draw the flower
            super().draw()
            #Draw the letter
            arcade.draw_text(self.letter, self.center_x, self.center_y, arcade.color.DEEP_CHESTNUT, 25,
                            anchor_x="center")

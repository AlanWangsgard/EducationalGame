from game.constants import SPRITE_SCALING_COIN, SCREEN_WIDTH, SCREEN_HEIGHT
import arcade
import random


class Coin(arcade.Sprite):
    """
    Creates a coin sprite

    attributes:
                self.coin(None)
                self.coin_list(None)
                self(arcade.Sprite): an instance of Sprite
                self.center_x: random positioning on the x coordinates
                self.center_y: random positioning on the y coordinates


    """
    def __init__(self):
        self.coin = None
        self.coin_list = None
        super().__init__(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)
        self.center_x = random.randrange(SCREEN_WIDTH)
        self.center_y = random.randrange(SCREEN_HEIGHT)

import arcade
import random
import time
from datetime import datetime
from bee_game.generate_letter_flowers import generate_letter_flowers
from bee_game.constants import SCREEN_HEIGHT, SCREEN_WIDTH, GRASS_ODDS, GRASS_IMAGE, GRASS_SCALE, BEE_IMAGE, BEE_SCALE, BEE_SPEED, WORD_LIST_PATH, GAME_LENGTH

class BeeGame(arcade.View):

    def __init__(self, window):
        self.window = window
        self.scene = None
        self.player_sprite = None
        with open(WORD_LIST_PATH, "r") as infile:
            self.words = infile.readlines()
    
    def on_show_view(self):
        arcade.set_background_color(arcade.color.APPLE_GREEN)
        self.setup()

    def setup(self):
        self.game_over = False
        self.keys_down = {"up":False, "down":False, "left":False, "right":False}
        self.score = 0
        self.time = time.time()
        self.scene = arcade.Scene()

        # Add the grass
        for x in range(SCREEN_WIDTH):
            for y in range(SCREEN_HEIGHT):
                chance = random.randint(0, GRASS_ODDS + 1)
                if chance == GRASS_ODDS:
                    grass = arcade.Sprite(GRASS_IMAGE, GRASS_SCALE)
                    grass.center_x = x
                    grass.center_y = y
                    self.scene.add_sprite("Grass", grass)
        # Add the player
        image_source = BEE_IMAGE
        self.player_sprite = arcade.Sprite(image_source, BEE_SCALE)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        # Add the letter flowers.
        self.letters = generate_letter_flowers(random.choice(self.words).strip())

    def on_draw(self):
        arcade.start_render()
        # Draw the background
        self.scene.draw()
        # Draw the letters because they're special
        for letter in self.letters:
            letter.draw()
        # Draw the player
        self.player_sprite.draw()
        if self.game_over:
            arcade.draw_text("Nice Job!", SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 4, arcade.color.FASHION_FUCHSIA, 25,
                            anchor_x="center")
            arcade.draw_text(f"Your Score: {self.score}", SCREEN_WIDTH // 2, SCREEN_HEIGHT * 2 // 3, arcade.color.FASHION_FUCHSIA, 25,
                            anchor_x="center")
            arcade.draw_text("Press 'm' to return to the menu", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.FASHION_FUCHSIA, 15,
                            anchor_x="center")
    
    def on_key_press(self,key,modifiers):
        if not self.game_over:
            if key == arcade.key.SPACE:
                # Player is selecting a letter?
                print("X", self.player_sprite.center_x)
                print("Y", self.player_sprite.center_y)
                for letter_flower in self.letters:
                    if letter_flower.visible:
                        if     ((letter_flower.get_x() <= self.player_sprite.center_x + 30
                            and letter_flower.get_x() >= self.player_sprite.center_x - 30)
                            and (letter_flower.get_y() <  self.player_sprite.center_y + 30
                            and letter_flower.get_y() >  self.player_sprite.center_y - 30)):
                            print("at flower", letter_flower.get_value())
                            letter_flower.visible = False
            elif key == arcade.key.UP or key == arcade.key.W:
                self.keys_down["up"] = True
            elif key == arcade.key.DOWN or key == arcade.key.S:
                self.keys_down["down"] = True
            elif key == arcade.key.LEFT or key == arcade.key.A:
                self.keys_down["left"] = True
                #self.player_sprite = arcade.Sprite(bee2.png, Character_Scaling)
            elif key == arcade.key.RIGHT or key == arcade.key.D:
                self.keys_down["right"] = True
            elif key == arcade.key.N:
                self.letters = generate_letter_flowers(random.choice(self.words).strip())
        if key == arcade.key.M:
            self.window.show_view(self.window.menu)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.keys_down["up"] = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.keys_down["down"] = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.keys_down["left"] = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.keys_down["right"] = False
    
    def on_update(self, delta_time):
        if self.keys_down["up"]:
            self.player_sprite.center_y += BEE_SPEED
        if self.keys_down["down"]:
            self.player_sprite.center_y += -BEE_SPEED
        if self.keys_down["left"]:
            self.player_sprite.center_x += -BEE_SPEED
        if self.keys_down["right"]:
            self.player_sprite.center_x += BEE_SPEED
        
        if self.player_sprite.center_x < 0:
            self.player_sprite.center_x = SCREEN_WIDTH
        elif self.player_sprite.center_x > SCREEN_WIDTH:
            self.player_sprite.center_x = 0
        if self.player_sprite.center_y < 0:
            self.player_sprite.center_y = SCREEN_HEIGHT
        elif self.player_sprite.center_y > SCREEN_HEIGHT:
            self.player_sprite.center_y = 0
        
        if time.time() - self.time > GAME_LENGTH:
            # Game ended!
            self.game_over = True
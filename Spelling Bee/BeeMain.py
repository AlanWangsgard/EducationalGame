import arcade
import random

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE, GRASS_ODDS, GRASS_IMAGE, GRASS_SCALE, BEE_IMAGE, BEE_SCALE, BEE_SPEED

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.scene = None
        self.player_sprite = None
        self.keys_down = {"up":False, "down":False, "left":False, "right":False}
        arcade.set_background_color(arcade.color.APPLE_GREEN)
    
    def setup(self):
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Player")
        for x in range(SCREEN_WIDTH):
            for y in range(SCREEN_HEIGHT):
                chance = random.randint(0, GRASS_ODDS + 1)
                if chance == GRASS_ODDS:
                    grass = arcade.Sprite(GRASS_IMAGE, GRASS_SCALE)
                    grass.center_x = x
                    grass.center_y = y
                    self.scene.add_sprite("Grass", grass)
        image_source = BEE_IMAGE
        self.player_sprite = arcade.Sprite(image_source, BEE_SCALE)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.scene.add_sprite("Player", self.player_sprite)

    def on_draw(self):
        arcade.start_render()
        self.scene.draw()
        self.player_sprite.draw()
        
    
    def on_key_press(self,key,modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.keys_down["up"] = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.keys_down["down"] = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.keys_down["left"] = True
            #self.player_sprite = arcade.Sprite(bee2.png, Character_Scaling)
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.keys_down["right"] = True

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

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
import arcade
import random

Width = 1000
Height = 650
title = "Dungeon Crawl"
Character_Scaling = .5
Character_Movement = 5
Character_Jump = 20
Gravity = 1
Tile_Scaling = .5

class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(Width, Height, title)
        self.scene = None
        self.player_sprite = None
        self.physics_engine = None
        arcade.set_background_color(arcade.color.APPLE_GREEN)
    
    def setup(self):
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Walls", use_spatial_hash=True)
        for x in range(1000):
            for y in range(650):
                chance = random.randint(0,3000)
                if chance == 1:
                    grass = arcade.Sprite(":resources:images/tiles/grass_sprout.png", Tile_Scaling)
                    grass.center_x = x
                    grass.center_y = y
                    self.scene.add_sprite("Grass", grass)
        image_source = ":resources:images/enemies/bee.png"
        self.player_sprite = arcade.Sprite(image_source, Character_Scaling)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.scene.add_sprite("Player", self.player_sprite)
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, walls=self.scene["Walls"]
        )

    def on_draw(self):
        arcade.start_render()
        self.scene.draw()
        self.player_sprite.draw()
        
    
    def on_key_press(self,key,modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = Character_Movement
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -Character_Movement
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -Character_Movement
            #self.player_sprite = arcade.Sprite(bee2.png, Character_Scaling)
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = Character_Movement

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0
    
    def on_update(self, delta_time):
        self.physics_engine.update()
        if self.player_sprite.center_x < 0:
            self.player_sprite.center_x = 1000
        elif self.player_sprite.center_x > 1000:
            self.player_sprite.center_x = 0
        if self.player_sprite.center_y < 0:
            self.player_sprite.center_y = 650
        elif self.player_sprite.center_y > 650:
            self.player_sprite.center_y = 0

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
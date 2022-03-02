import arcade
import arcade.gui
from score.frogger_local_db import FroggerLocalDB
from game.constants import PICTURES_PATH
from score.player_crud import PlayerCRUD
from score.score_crud import ScoreCrud

class Menu(arcade.View):
    def __init__(self, window):
        self.window = window
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.background = arcade.load_texture(PICTURES_PATH + "menu.png")

        self.v_box = arcade.gui.UIBoxLayout()
        self.start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.v_box.add(self.start_button.with_space_around(bottom=20))
        self.save_button = arcade.gui.UIFlatButton(text="Save Game", width=200)
        self.v_box.add(self.save_button.with_space_around(bottom=20))
        self.manager.add(arcade.gui.UIAnchorWidget(
            anchor_x="center_x",
            anchor_y="center_y",
            child=self.v_box
        ))
        localDB = FroggerLocalDB()
        localDB.initializeDB()
        self.playerName = None

    def on_show(self):
        """ This is run once when we switch to this view """
        self.window.clear()
        arcade.set_background_color(arcade.color.RED)
        if not self.playerName:
            # display a popup to get the playername
            self.playerName = "TestPlayer"

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            800, 600,
                                            self.background)
        # arcade.set_background_color(arcade.color.RED)
        arcade.draw_text("Menu", self.window.width / 2, self.window.height -100,
                         arcade.color.RASPBERRY, font_size=50, anchor_x="center")
        self.manager.draw()
        # Maybe draw the player name in the corner
        
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if _x >= 300 and _x <= 500 and _y >=280 and _y <= 320:
            self.window.show_view(self.window.Frogger)
        if _x >= 300 and _x <= 500 and _y >= 330 and _y <= 370:
            # save the game
            pCrud = PlayerCRUD()
            pCrud.addPlayer(self.playerName)
            id = pCrud.getID(self.playerName)

            score = self.window.playerScore
            sCrud = ScoreCrud()
            sCrud.saveScore(id, score)



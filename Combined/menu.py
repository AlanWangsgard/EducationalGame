import arcade
import arcade.gui
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
<<<<<<< HEAD
        self.start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.v_box.add(self.start_button.with_space_around(bottom=20))
        self.save_button = arcade.gui.UIFlatButton(text="Save Game", width=200)
        self.v_box.add(self.save_button.with_space_around(bottom=20))
=======
        self.start_frogger_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.start_frogger_button.on_click = self.start_frogger_click
        self.v_box.add(self.start_frogger_button.with_space_around(bottom=20))
        self.load_button = arcade.gui.UIFlatButton(text="Load Game", width=200)
        self.load_button.on_click = self.load_click
        self.v_box.add(self.load_button.with_space_around(bottom=20))
        
        # Bee game button
        self.bee_game_button = arcade.gui.UIFlatButton(text="Bee Game", width=200)
        # TODO: change button click action 
        self.bee_game_button.on_click = self.start_bee_game_click
        self.v_box.add(self.bee_game_button.with_space_around(bottom=40))
        
>>>>>>> 7b391b9706eb6c4f4f965c4ba3fecd8dc247cc23
        self.manager.add(arcade.gui.UIAnchorWidget(
            anchor_x="center_x",
            anchor_y="center_y",
            child=self.v_box
        ))
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
        
<<<<<<< HEAD
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


=======
    def start_frogger_click(self, event):
        self.window.show_view(self.window.Frogger)

    def start_bee_game_click(self, event):
        self.window.show_view(self.window.BeeGame)

    def load_click(self, event):
        # load the game
        pCrud = PlayerCRUD()
        pid = pCrud.getID(self.window.playerName)
        print(pid)
        gsCrud = GameStateCrud()
        state = gsCrud.getGameStateByPlayerId(pid)
        print(state)
        self.window.Frogger.setup(state[CRUD_INDEXES["level"]], state[CRUD_INDEXES["lives"]], state[CRUD_INDEXES["score"]])
        self.window.show_view(self.window.Frogger)
>>>>>>> 7b391b9706eb6c4f4f965c4ba3fecd8dc247cc23

import arcade
import arcade.gui
from game.constants import PICTURES_PATH, CRUD_INDEXES
from score.player_crud import PlayerCRUD
from score.score_crud import ScoreCrud
from score.game_state_crud import GameStateCrud

class MidScreen(arcade.View):
    def __init__(self, window):
        self.window = window
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.background = arcade.load_texture(PICTURES_PATH + "midscreen.png")

        self.v_box = arcade.gui.UIBoxLayout()
        self.start_button = arcade.gui.UIFlatButton(text="Next Level", width=200)
        self.start_button.on_click = self.start_click
        self.v_box.add(self.start_button.with_space_around(bottom=20))
        self.save_button = arcade.gui.UIFlatButton(text="Save Game", width=200)
        self.save_button.on_click = self.save_click
        self.v_box.add(self.save_button.with_space_around(bottom=20))
        self.load_button = arcade.gui.UIFlatButton(text="Load Game", width=200)
        self.load_button.on_click = self.load_click
        self.v_box.add(self.load_button.with_space_around(bottom=20))
        self.manager.add(arcade.gui.UIAnchorWidget(
            anchor_x="center_x",
            anchor_y="center_y",
            child=self.v_box
        ))

    def on_show(self):
        """ This is run once when we switch to this view """
        self.window.clear()
        self.manager.enable()
        arcade.set_background_color(arcade.color.RED)

    def on_hide_view(self):
        self.manager.disable()
        return super().on_hide_view()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            800, 600,
                                            self.background)
        # arcade.set_background_color(arcade.color.RED)
        arcade.draw_text("Level Complete!", self.window.width / 2, self.window.height -100,
                         arcade.color.RASPBERRY, font_size=50, anchor_x="center")
        self.manager.draw()
        # Maybe draw the player name in the corner
        
    def start_click(self, event):
        self.window.show_view(self.window.Frogger)

    def save_click(self, event):
        # save the game
        pCrud = PlayerCRUD()
        pCrud.addPlayer(self.window.playerName)
        id = pCrud.getID(self.window.playerName)

        score = self.window.playerScore
        sCrud = ScoreCrud()
        sCrud.saveScore(id, score)

        gsCrud = GameStateCrud()
        gsCrud.saveGameState(id, self.window.playerLevel, self.window.playerScore, self.window.playerLives)

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

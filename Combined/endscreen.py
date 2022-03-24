import arcade
from db.db_interactor import DB_Interactor
from game.constants import CERT_FILE_PATH, SCREEN_WIDTH, SCREEN_HEIGHT, PICTURES_PATH
class EndScreen(arcade.View):
    def __init__(self, window):
        self.window = window
        self.background = arcade.load_texture(PICTURES_PATH + "end_screen.png")
        self.dbi = DB_Interactor(CERT_FILE_PATH)

    def on_show(self):
        """ This is run once when we switch to this view """
        self.window.clear()
        arcade.set_background_color(arcade.color.RED)
        self.dbi.update_scores(self.user_score)
        scores_list = self.dbi.get_all_scores()
        self.high_scores = scores_list

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        final_score = f"Final Score:{self.user_score}"
        arcade.draw_text(final_score, SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100, arcade.color.WHITE, 25,
                            anchor_x="center")
        arcade.draw_text("High Scores: ", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 150, arcade.color.WHITE, 25,
                            anchor_x="center")
        space = 100
        for score in self.high_scores:
            color = arcade.color.WHITE
            if score == self.user_score:
                color = arcade.color.CHARTREUSE
            arcade.draw_text(str(score), SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100 - space, color, 25,
                            anchor_x="center")
            space += 50

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        self.window.show_view(self.window.menu)

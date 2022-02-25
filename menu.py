import arcade
import arcade.gui


class Menu(arcade.View):
    def __init__(self, window):
        self.window = window
        self.background = arcade.load_texture("images/menu.png")
        self.start_button = arcade.gui.UIFlatButton(
            center_x=400, center_y=300, text="Start Game", width=200)

    def on_show(self):
        """ This is run once when we switch to this view """
        self.window.clear()
        arcade.set_background_color(arcade.color.RED)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            800, 600,
                                            self.background)
        # arcade.set_background_color(arcade.color.RED)
        arcade.draw_text("Menu", self.window.width / 2, self.window.height -100,
                         arcade.color.RASPBERRY, font_size=50, anchor_x="center")
        self.start_button.draw()
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if _x >= 300 and _x <= 500 and _y >=280 and _y <= 320:
            self.window.show_view(self.window.Frogger)


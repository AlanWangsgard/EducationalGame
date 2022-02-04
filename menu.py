import arcade
class Menu(arcade.View):
    def __init__(self, window):
        self.window = window
        self.background = arcade.load_texture("images/menu.png")

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
        # arcade.draw_text("Menu", self.window.width / 2, self.window.height / 2,
        #                  arcade.color.BABY_BLUE, font_size=50, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        self.window.show_view(self.window.Frogger)


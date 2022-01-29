import arcade
from arcade.gui import UIManager # i think I need this, but I'm not sure.
from game.questionGenerator import QuestionGenerator
from game import constants ### WHEN WE REORGANIZE THE FILESYSTEM, THIS WILL NEED CHANGED


class MathQuestionView(arcade.View):
    """ Class that manages the math question view."""

    def __init__(self):
        # Initialize the math question view.
        super().__init__()
        self.__question_generator = QuestionGenerator()

    def on_show(self):
        # Called when switching to this vew
        arcade.set_background_color(arcade.color.AUROMETALSAURUS)
        self.setup()
    
    def setup(self):
        # Do any setup of variables or timings or colors we need.
        self.new_question()

    def new_question(self):
        # Set up for a new question.
        self.__question = self.__question_generator.generate_sum_question()
        self.__user_input = ""
    
    def on_draw(self):
        # Called regularly to draw the screen.
        # We'll need to draw the first number, the operator, and the second number.
        # Will also need to draw the user's input.
        # And if the user gets it right, we'll need to let them know.
        arcade.start_render()
        arcade.draw_text(self.__question.to_string(), constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                         arcade.color.LAVA, font_size = 80, anchor_x = 'center', anchor_y = 'center')
        '''arcade.draw_text() # The first number.
        arcade.draw_text() # The operator.
        arcade.draw_text() # The second operator.
        arcade.draw_text() # A big bar across, separating the question from the user's input.'''
        arcade.draw_text(self.__user_input, constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 + 200,
                         arcade.color.PURPLE_PIZZAZZ, font_size = 80, anchor_x = 'center', anchor_y = 'center') # The user's input. 

    def on_key_press(self, symbol, modifiers):
        # What happens when the user presses a key.

        # If it's the delete key, then remove the the character on the end of input.
        if symbol == arcade.key.BACKSPACE and len(self.__user_input) > 0:
            self.__user_input = self.__user_input[:-1]
            return
        
        if symbol == arcade.key.ENTER:
            if self.__question.check_answer(int(self.__user_input)):
                # They got it right!
                print("Correct!")
                self.new_question()
                arcade.set_background_color(arcade.color.GRANNY_SMITH_APPLE)
            else:
                # They got it wrong.
                print("Incorrect.")
                arcade.set_background_color(arcade.color.RED_DEVIL)


        # If it's a number key, then add it to the user input.
        if arcade.key.NUM_0 <= symbol <= arcade.key.NUM_9:
            # It's a numpad key.
            number = symbol - arcade.key.NUM_0
            self.__user_input += str(number)
        elif arcade.key.KEY_0 <= symbol <= arcade.key.KEY_9:
            # It's a keyboard number row key.
            number = symbol - arcade.key.KEY_0
            self.__user_input += str(number)

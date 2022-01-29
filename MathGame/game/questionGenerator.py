# Generates questions for the math game.
from game.question import Question
import random

class QuestionGenerator:

    def __init__(self, difficulty = 0):
        pass

    def generate_sum_question(self):
        # pick two numbers, and figure out the answer
        # question = Question(num1, num2, "+", answer)
        # return question
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        operator = "+"
        ans = num1 + num2
        q = Question(num1, operator, num2, ans)
        return q

    def generate_difference_question(self):
        # "-"
        pass

    def generate_product_question(self):
        pass

    def generate_quotient_question(self):
        pass

    def get_difficulty(self):
        pass

    def set_difficulty(self):
        pass

    def increment_difficulty(self):
        pass
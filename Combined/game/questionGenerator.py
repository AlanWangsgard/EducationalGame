
# Generates questions for the math game.
from game.question import Question
import random as rand

class QuestionGenerator:
    # Initials the two numbers involved in the operation to zero.
    num1 = 0
    num2 = 0

    def __init__(self, difficulty = 0):
        self.difficulty = difficulty

    def generate_sum_question(self):
        # pick two numbers, and figure out the answer
        # question = Question(num1, num2, "+", answer)
        # return question
        operator = '+'
        if self.difficulty == 0:
            num1 = rand.randint(0, 5)
            num2 = rand.randint(0, 5)
        elif self.difficulty == 1:
            num1 = rand.randint(1, 10)
            num2 = rand.randint(1, 10)
        elif self.difficulty == 2:
            num1 = rand.randint(10, 20)
            num2 = rand.randint(10, 20)
        q = Question(num1, operator, num2, num1 + num2)
        return q

    def generate_difference_question(self):
        # pick two numbers, and figure out the answer
        # question = Question(num1, num2, "-", answer)
        # return question
        operator = '-'
        if self.difficulty == 0:
            num1 = rand.randint(0, 5)
            num2 = rand.randint(0, 5)
        elif self.difficulty == 1:
            num1 = rand.randint(1, 10)
            num2 = rand.randint(1, 10)
        elif self.difficulty == 2:
            num1 = rand.randint(10, 20)
            num2 = rand.randint(10, 20)
        q = Question(num1, operator, num2, num1 - num2)
        return q

    def generate_product_question(self):
        # pick two numbers, and figure out the answer
        # question = Question(num1, num2, "*", answer)
        # return question
        operator = '*'
        if self.difficulty == 0:
            num1 = rand.randint(0, 5)
            num2 = rand.randint(0, 5)
        elif self.difficulty == 1:
            num1 = rand.randint(1, 10)
            num2 = rand.randint(1, 10)
        elif self.difficulty == 2:
            num1 = rand.randint(10, 20)
            num2 = rand.randint(10, 20)
        q = Question(num1, operator, num2, num1 * num2)
        return q

    def generate_quotient_question(self):
        # pick two numbers, and figure out the answer
        # question = Question(num1, num2, "/", answer)
        # return question
        operator = '/'
        if self.difficulty == 0:
            num1 = rand.randint(0, 5)
            num2 = rand.randint(0, 5)
        elif self.difficulty == 1:
            num1 = rand.randint(1, 10)
            num2 = rand.randint(1, 10)
        elif self.difficulty == 2:
            num1 = rand.randint(10, 20)
            num2 = rand.randint(10, 20)
        q = Question(num1, operator, num2, num1 / num2)
        return q

    def get_difficulty(self):
        return self.difficulty

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def increment_difficulty(self):
        self.difficulty += 1

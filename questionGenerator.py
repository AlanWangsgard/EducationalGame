import random as rand
from game.question import Question

# Generates questions for the math game.
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
            num1 = rand.randint(0, 9)
            num2 = rand.randint(0, 9)
        elif self.difficulty == 1:
            num1 = rand.randint(10, 19)
            num2 = rand.randint(10, 19)
        elif self.difficulty == 2:
            num1 = rand.randint(10, 29)
            num2 = rand.randint(10, 29)
        q = Question(num1, num2, operator)
        return q

    def generate_difference_question(self):
        # pick two numbers, and figure out the answer
        # question = Question(num1, num2, "-", answer)
        # return question
        operator = '-'
        if self.difficulty == 0:
            num1 = rand.randint(0, 9)
            num2 = rand.randint(0, 9)
        elif self.difficulty == 1:
            num1 = rand.randint(10, 20)
            num2 = rand.randint(10, 20)
        elif self.difficulty == 2:
            num1 = rand.randint(10, 29)
            num2 = rand.randint(10, 29)
        q = Question(num1, num2, operator)
        return q

    def generate_product_question(self):
        # pick two numbers, and figure out the answer
        # question = Question(num1, num2, "*", answer)
        # return question
        operator = '*'
        if self.difficulty == 0:
            num1 = rand.randint(0, 9)
            num2 = rand.randint(0, 9)
        elif self.difficulty == 1:
            num1 = rand.randint(10, 20)
            num2 = rand.randint(10, 20)
        elif self.difficulty == 2:
            num1 = rand.randint(10, 29)
            num2 = rand.randint(10, 29)
        q = Question(num1, num2, operator)
        return q

    def generate_quotient_question(self):
        # pick two numbers, and figure out the answer
        # question = Question(num1, num2, "/", answer)
        # return question
        operator = '/'
        if self.difficulty == 0:
            num1 = rand.randint(0, 9)
            num2 = rand.randint(0, 9)
        elif self.difficulty == 1:
            num1 = rand.randint(10, 20)
            num2 = rand.randint(10, 20)
        elif self.difficulty == 2:
            num1 = rand.randint(10, 29)
            num2 = rand.randint(10, 29)
        q = Question(num1, num2, operator)
        return q

    def get_difficulty(self):
        return self.difficulty

    def set_difficulty(self):
        pass

    def increment_difficulty(self):
        difficulty = QuestionGenerator.get_difficulty()
        return  difficulty + 1

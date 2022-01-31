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
            num1 = rand.randint(20, 29)
            num2 = rand.randint(20, 29)
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
            num1 = rand.randint(10, 19)
            num2 = rand.randint(10, 19)
        elif self.difficulty == 2:
            num1 = rand.randint(20, 29)
            num2 = rand.randint(20, 29)
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
            num1 = rand.randint(10, 19)
            num2 = rand.randint(10, 19)
        elif self.difficulty == 2:
            num1 = rand.randint(20, 29)
            num2 = rand.randint(20, 29)
        q = Question(num1, num2, operator)
        return q

    def generate_quotient_question(self):
        # pick two numbers, and figure out the answer
        # question = Question(num1, num2, "/", answer)
        # return question
        operator = '-'
        if self.difficulty == 0:
            num1 = rand.randint(0, 9)
            num2 = rand.randint(0, 9)
        elif self.difficulty == 1:
            num1 = rand.randint(10, 19)
            num2 = rand.randint(10, 19)
        elif self.difficulty == 2:
            num1 = rand.randint(20, 29)
            num2 = rand.randint(20, 29)
        q = Question(num1, num2, operator)
        return q

    def get_difficulty(self):
        return self.difficulty

    def set_difficulty(self):
        pass

    def increment_difficulty(self):
        difficulty = QuestionGenerator.get_difficulty()
        return  difficulty + 1


""" private int num1;
    private int num2;
    private int ans;
    private Timer time;
    private Timer tStart;
    private int tCount;
    private int correct;
    private int tLimit;
    public boolean add = true;
    public boolean minus;
    public boolean mult;
    public boolean div;


    new_question
    ans = 0;
		if (add){
    	    num1 = (int) (Math.random() * 10);
    	    num2 = (int) (Math.random() * 10);
		} """

class Question:
    # Represents a single question to the user.
    # num1: integer       the first number presented left-to-right.
    # operator: string    the operator presented between the two numbers.
    # num2: integer       the second number presented left-to-right.
    # answer: integer     the answer to the math problem.
    __num1 = 0
    __operator = None
    __num2 = 0
    __answer = 0


    def __init__(self, num1, operator, num2, answer):
        # Initializes a Question.
        assert type(num1) == type(num2) == type(answer) == int, "num1, num2, and answer must be integers"
        assert operator in ['+', '-', '*', '/'], "operator must be one of the following: '+', '-', '*', '/'"
        
        self.__num1 = num1
        self.__num2 = num2
        self.__operator = operator
        self.__answer = answer

    def to_string(self):
        # Returns the string form of this question
        # num1 operator num2 = answer
        return str(self.__num1) + self.__operator + str(self.__num2) + "=" + str(self.__answer)

    def check_answer(self, user_answer):
        # Returns True if user_answer is equal to answer
        # user_answer must be an integer.
        assert type(user_answer) == int
        return user_answer == self.__answer

    def get_first_num(self):
        # Returns the first number as a string.
        return str(self.__num1)

    def get_second_num(self):
        # Returns the second number as a string.
        return str(self.__num2)

    def get_operator(self):
        # Returns the operator
        return self.__operator
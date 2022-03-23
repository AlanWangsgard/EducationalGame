from random import randint, choices
from letter_flower import LetterFlower
from constants import SCREEN_WIDTH, FLOWER_MAX_Y, FLOWER_PADDING

# This function will receive a word, and set up a list of LetterFlowers for the game.
def generate_letter_flowers(word):
    print(word)
    #Builds a list of LetterFlowers that are spaced apart enough.

    # Verify that the values in constants will work for this word
    # WordLength < MinLettersPerRow * MinLettersPerCol
    # MinLettersPerCol =     MaxY    / Padding
    # MinLettersPerRow = ScreenWidth / Padding
    extra_letters = int(SCREEN_WIDTH / FLOWER_PADDING - 1) * int(FLOWER_MAX_Y / FLOWER_PADDING - 1) - len(word)
    if extra_letters <= 0:
            print("Error: screen dimensions and padding are not compatible with this word. Try changing \n\tscreen size\n\tpadding\n\tword length")
            return []
    
    # Append some random letters to make it a bit more difficult!
    extra_letters = randint(1, max(extra_letters - 2, 1)) # don't always include as many as possible,
    for letter in choices("abcdefghijklmnopqrstuvwxyz", k=extra_letters): # pick that many random letters
        word += letter # add them to the list of letters we need to generate.

    flower_list = []
    # Add a LetterFlower for each letter in the word
    for letter in word:
        attempts = 0
        position_is_safe = False
        while not position_is_safe:
            # See if we've tried too many times
            attempts += 1
            if (attempts >= 1000):
                print("Too many attempts at finding a good position. Try changing \n\tscreen size\n\tpadding\n\tword length")
                return []

            # Pick a random position
            x = randint(FLOWER_PADDING // 2, SCREEN_WIDTH - FLOWER_PADDING // 2)
            y = randint(FLOWER_PADDING // 2, FLOWER_MAX_Y)
            position_is_safe = True
            # Verify that it's far enough away from all the other letters
            for flower in flower_list:
                if abs(x - flower.get_x()) < FLOWER_PADDING and abs(y - flower.get_y()) < FLOWER_PADDING:
                    # Too close
                    position_is_safe = False
                    break
        # Create a flower
        flower_list.append(LetterFlower(letter, x, y))
    return flower_list


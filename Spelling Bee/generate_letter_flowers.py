from random import randint
from letter_flower import LetterFlower
from constants import SCREEN_WIDTH, FLOWER_MAX_Y, FLOWER_PADDING

# This function will receive a word, and set up a list of LetterFlowers for the game.
def generate_letter_flowers(word):
    #Builds a list of LetterFlowers that are spaced apart enough.

    # Verify that the values in constants will work for this word
    # WordLength < MinLettersPerRow * MinLettersPerCol
    # MinLettersPerCol =     MaxY    / Padding
    # MinLettersPerRow = ScreenWidth / Padding
    if len(word) >= int(SCREEN_WIDTH / FLOWER_PADDING - 1) * int(FLOWER_MAX_Y / FLOWER_PADDING - 1):
            print("Error: screen dimensions and padding are not compatible with this word. Try changing \n\tscreen size\n\tpadding\n\tword length")
            return []

    flower_list = []
    # Add a LetterFlower for each letter in the word
    attempts = 0
    for letter in word:
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


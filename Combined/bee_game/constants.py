from pathlib import Path

DIR = str(Path(__file__).resolve().parent.parent)
PICTURES_PATH = DIR + "/pictures/"
WORD_LIST_PATH = DIR + "/bee_game/words.txt"

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Spelling Bee"

# Colors
FLOWER_COLORS = []
LETTER_COLOR = ""
FLOWER_PADDING = 20
FLOWER_MIN_Y = 150
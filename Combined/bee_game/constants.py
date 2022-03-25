from pathlib import Path

DIR = str(Path(__file__).resolve().parent.parent)
PICTURES_PATH = DIR + "/pictures/"
WORD_LIST_PATH = DIR + "/bee_game/words.txt"
FONT_PATH = PICTURES_PATH  + "Azeret.ttf"
# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Spelling Bee"

# Grass
GRASS_ODDS = 3000
GRASS_IMAGE = ":resources:images/tiles/grass_sprout.png"
GRASS_SCALE = 0.5

# Bee
BEE_IMAGE = ":resources:images/enemies/bee.png"
BEE_SCALE = 0.5
BEE_SPEED = 5

# images
FLOWER_IMAGES = [":resources:images/items/gemRed.png", ":resources:images/items/gemGreen.png", ":resources:images/items/gemBlue.png"]
# The flower padding and screen size need to be calculated to satisfy one of the following equations
# MaxWordLength < MinLettersPerRow * MinLettersPerCol
# MinLettersPerCol =     MaxY     / Padding - 1
# MinLettersPerRow = ScreenWidth  / Padding - 1
FLOWER_PADDING = 100
FLOWER_MAX_Y = 400
GAME_LENGTH = 30 # seconds
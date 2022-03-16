from pathlib import Path

DIR = str(Path(__file__).resolve().parent.parent)
PICTURES_PATH = DIR + "/pictures/"
WORD_LIST_PATH = DIR + "words.txt"

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

# Colors
FLOWER_COLORS = []
LETTER_COLOR = ""
FLOWER_PADDING = 20
FLOWER_MIN_Y = 150
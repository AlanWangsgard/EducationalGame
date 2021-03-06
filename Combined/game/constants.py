import os
from pathlib import Path

DIR = str(Path(__file__).resolve().parent.parent)
CERT_FILE_PATH = DIR + "/db/" + "cert.json" ##### REPLACE WITH YOUR ADMIN SDK CERT FILENAME.
PICTURES_PATH = DIR + "/pictures/"
DB_PATH = DIR + "/score/" + "scores.db"

# car
CAR_SPRITE_SCALING = 0.4
SPRITE_SCALING = 0.4
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)
# coin
SPRITE_SCALING_COIN = 0.2


# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "FROGGER"

#movement
MOVEMENT_SPEED = 5
NO_MOVEMENT = 0

#car spacing
Y_COUNT = 5
Y_START = 100
Y_SPACING = 50

NUM_CARS_PER_ROW = 1

# lives
LIFE_COUNT = 3
LIFE_POSITION_START = 20
LIFE_SPACING = 25
GAME_OVER = 1
PLAY_GAME = 0

MINIMUM_TIME = 5.5

# Saved Game State
CRUD_INDEXES = {
    "pid":  1,
    "level":2,
    "score":3,
    "lives":4
}
from enum import Enum

# Every block that is in board size
BLOCK_WIDTH = 50
BLOCK_HEIGHT = 50

# How much blocks in board
BLOCKS_AMOUNT_Y = 15 + 1  # One here and below is additional frame block
BLOCKS_AMOUNT_X = 15 + 1

# Calculate screen size based on these stats
SCREEN_WIDTH = BLOCKS_AMOUNT_Y * BLOCK_WIDTH
SCREEN_HEIGHT = BLOCKS_AMOUNT_X * BLOCK_HEIGHT

# Title that will be shown on window
SCREEN_TITLE = "Adventures of 3 Balls"


class Blocks(Enum):
    """All blocks IDs that will be used to set textures and make controls."""

    empty = 0
    frame = 1
    wall = 2
    trap = 3
    water = 4


TEXTURES_AND_COLORS = {
    0: (141, 182, 0),
    1: "./game/resources/frame.png",
    2: "./game/resources/wall.png",
    3: "./game/resources/trap.png",
    4: (0, 105, 148)
}

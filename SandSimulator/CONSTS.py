from collections import namedtuple
from typing import Final
GridDimensions = namedtuple("GridDimensions", "WIDTH HEIGHT")
Coords = namedtuple("Coords", "x, y")

GRID: GridDimensions = GridDimensions(300, 300)
SQUARE_SIDE: Final = 2
FPS: Final = 10  # suggested between 10 and 14
BACKGROUND_COLOR: Final = "Black"
DRAW_GRID_LINES: bool = False
GRID_LINES_COLOR: Final = "White"

"""
DONT MODIFY THESE
"""
WIDTH, HEIGHT = SQUARE_SIDE * GRID.WIDTH, SQUARE_SIDE * GRID.HEIGHT

from collections import namedtuple
from typing import Final
GridDimensions = namedtuple("GridDimensions", "WIDTH HEIGHT")
Coords = namedtuple("Coords", "x, y")

GRID: GridDimensions = GridDimensions(250, 250)  # 300x300
GRAIN_SIDE_SIZE: Final = 3  # 2
FPS: Final = 300  # suggested between 10 and 14
BACKGROUND_COLOR: Final = "Black"
DRAW_GRID_LINES: bool = False
GRID_LINES_COLOR: Final = "White"

"""
DONT MODIFY THESE
"""
WIDTH, HEIGHT = GRAIN_SIDE_SIZE * GRID.WIDTH, GRAIN_SIDE_SIZE * GRID.HEIGHT

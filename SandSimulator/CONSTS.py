from collections import namedtuple
from typing import Final
GridDimensions = namedtuple("GridDimensions", "WIDTH, HEIGHT")
Coords = namedtuple("Coords", "x, y")

GRID: GridDimensions = GridDimensions(15, 15)  # 250x250
GRAIN_SIDE_SIZE: Final = 50  # 3
FPS: Final = 10000  # suggested between 10 and 14
BACKGROUND_COLOR: Final = "Black"
MARGIN = 1
COLOR_CHANGE_SPEED: int = 5
TRANSPARENCY: float = 1  # range(0,1)
SATURATION: float = 1  # range(0,1)


DRAW_GRID_LINES: bool = True
GRID_LINES_COLOR: Final = "White"
"""
DONT MODIFY THESE
"""
WIDTH, HEIGHT = GRAIN_SIDE_SIZE * GRID.WIDTH, GRAIN_SIDE_SIZE * GRID.HEIGHT

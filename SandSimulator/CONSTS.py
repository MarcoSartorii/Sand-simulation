from collections import namedtuple
from typing import Final
GridDimensions = namedtuple("GridDimensions", "WIDTH, HEIGHT")
Coords = namedtuple("Coords", "x, y")


BACKGROUND_COLOR: Final = "Black"
FPS: Final = 300

"""
Too high values could make impossible to create the canvas (750x750 is suggested)
Example:
15xGRAIN_SIDE_SIZE, 15xGRAIN_SIDE_SIZE = 750x750

GRID: GridDimensions = GridDimensions(15, 15)  
GRAIN_SIDE_SIZE: Final = 50
"""
GRID: GridDimensions = GridDimensions(100, 100)
GRAIN_SIDE_SIZE: Final = 7  # 3


"""
draws the squares from "MARGIN" pixels inside the square (it takes out the border of the square MARGIN times)
"""
MARGIN = 1  # margin 0 creates the entire square without cutting anything

OPACITY: float = 1  # range(0,1)
SATURATION: float = 1  # range(0,1)
DEGREES: int = 180  # range(0,360)

""" 
negative val rotates the spectre anti clockwise.
positive val rotates the spectre clockwise.
"""
COLOR_CHANGE_SPEED: int = 1  # range(-179,180) -> means min val = -179, max 179


"""
This was used for debug
"""
DRAW_GRID_LINES: bool = False
GRID_LINES_COLOR: Final = "White"

"""
DONT MODIFY THESE
"""
WIDTH, HEIGHT = GRAIN_SIDE_SIZE * GRID.WIDTH, GRAIN_SIDE_SIZE * GRID.HEIGHT

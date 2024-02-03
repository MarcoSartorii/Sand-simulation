import colorsys
from tkinter import Canvas
from typing import Optional

from CONSTS import GridDimensions, Coords, COLOR_CHANGE_SPEED, SATURATION, TRANSPARENCY, MARGIN


class Sand:
    canvas: Canvas
    grid: GridDimensions
    square_side: int
    hue: int
    color_gradiant: int

    def __init__(self, canvas: Canvas, grid: GridDimensions, square_side: int):
        self.hue = 0
        self.color_gradiant = 360
        self.grid = grid
        self.canvas = canvas
        self.square_side = square_side

    def create_grain(self, mouse_pos: Coords, matrix: [[], ...]) -> bool:
        grain_coords: Optional[Coords] = self.get_grain_coords(mouse_pos)
        if grain_coords is None:
            return False
        if matrix[grain_coords.y][grain_coords.x]:
            self.draw_grain(grain_coords)
            return True
        return False

    def get_grain_coords(self, mouse_pos: Coords) -> Optional[Coords]:
        grain_x = mouse_pos.x // self.square_side
        grain_y = mouse_pos.y // self.square_side
        if self.are_valid_grid_coords(grain_x, grain_y, self.grid.WIDTH, self.grid.HEIGHT):
            return Coords(grain_x, grain_y)

    @staticmethod
    def are_valid_grid_coords(grain_x, grain_y, width, height) -> bool:
        return grain_x in range(0, width) and grain_y in range(0, height)

    def draw_grain(self, grain_coords):
        self.canvas.create_rectangle(
            grain_coords.x * self.square_side + MARGIN,
            grain_coords.y * self.square_side + MARGIN,
            grain_coords.x * self.square_side + self.square_side - MARGIN,
            grain_coords.y * self.square_side + self.square_side - MARGIN,
            fill=self.get_next_color(),
            outline=""
        )

    def get_next_color(self):
        if self.hue > self.color_gradiant:
            self.hue = 0
        rgb = colorsys.hsv_to_rgb(self.hue, SATURATION, TRANSPARENCY)
        self.hue += COLOR_CHANGE_SPEED / self.color_gradiant
        self.hue %= 1  # cap hue at 1.0
        r = round(rgb[0] * 255)
        g = round(rgb[1] * 255)
        b = round(rgb[2] * 255)
        rgb_ints = (r, g, b)
        return self._from_rgb(rgb_ints)

    @staticmethod
    def _from_rgb(rgb):
        return "#%02x%02x%02x" % rgb

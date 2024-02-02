import colorsys
from collections import namedtuple
from tkinter import Canvas
from typing import Optional

from CONSTS import GridDimensions, Coords


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

    def create_grain(self, mouse_pos: Coords):
        grid_coords: Optional[Coords] = self.get_grid_coords(mouse_pos)
        if grid_coords is None:
            return
        self.draw_grain(grid_coords)

    def get_grid_coords(self, mouse_pos: Coords) -> Optional[Coords]:
        grid_x = mouse_pos.x // self.square_side
        grid_y = mouse_pos.y // self.square_side
        if self.are_valid_grid_coords(grid_x, grid_y, self.grid.WIDTH, self.grid.HEIGHT):
            return Coords(grid_x, grid_y)

    @staticmethod
    def are_valid_grid_coords(grid_x, grid_y, width, height) -> bool:
        if grid_x not in range(0, width) or grid_y not in range(0, height):
            return False
        return True

    def draw_grain(self, grid_coords):
        self.canvas.create_rectangle(
            grid_coords.x * self.square_side,
            grid_coords.y * self.square_side,
            grid_coords.x * self.square_side + self.square_side,
            grid_coords.y * self.square_side + self.square_side,
            fill=self.get_next_color(),
            outline=""
        )

    def get_next_color(self):
        if self.hue > self.color_gradiant:
            self.hue = 0
        rgb = colorsys.hsv_to_rgb(self.hue, 1, 1)
        self.hue += 1 / self.color_gradiant
        self.hue %= 10000  # cap hue at 1.0
        r = round(rgb[0] * 255)
        g = round(rgb[1] * 255)
        b = round(rgb[2] * 255)
        rgb_ints = (r, g, b)
        return self._from_rgb(rgb_ints)

    @staticmethod
    def _from_rgb(rgb):
        return "#%02x%02x%02x" % rgb

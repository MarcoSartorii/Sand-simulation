import colorsys
from tkinter import Canvas
from typing import Optional

from CONSTS import GridDimensions, Coords, COLOR_CHANGE_SPEED, SATURATION, TRANSPARENCY
from Grain import Grain


class SandGrid:
    canvas: Canvas
    grid: GridDimensions
    square_side: int
    hue: int
    color_gradiant: int
    matrix: Optional

    def __init__(self, canvas: Canvas, grid: GridDimensions, square_side: int):
        self.hue = 0
        self.color_gradiant = 360
        self.grid = grid
        self.canvas = canvas
        self.square_side = square_side
        self.matrix = self.init_matrix(grid.WIDTH, grid.HEIGHT)
        self.matrix: Optional[Optional[Grain], ...] = self.init_matrix(grid.WIDTH, grid.HEIGHT)

    def add_grain(self, mouse_pos: Coords) -> type(None):
        grain: Optional[Grain, ...] = self.get_grain_coords(mouse_pos)
        if grain is None:
            return
        if self.matrix[grain.coords.y][grain.coords.x] is None:  # if the position is free
            self.matrix[grain.coords.y][grain.coords.x] = Grain(coords=grain.coords, canvas=self.canvas,
                                                                color=self.get_next_color(),
                                                                square_side=self.square_side)
        self.matrix[grain.coords.y][grain.coords.x].draw()

    def get_grain_coords(self, mouse_pos: Coords) -> Optional[Grain]:
        grain_x = mouse_pos.x // self.square_side
        grain_y = mouse_pos.y // self.square_side
        if self.are_valid_grid_coords(grain_x, grain_y, self.grid.WIDTH, self.grid.HEIGHT):
            return Grain(coords=Coords(grain_x, grain_y), canvas=self.canvas)

    @staticmethod
    def are_valid_grid_coords(grain_x, grain_y, width, height) -> bool:
        return grain_x in range(0, width) and grain_y in range(0, height)

    def draw_grain(self, grain_coords):
        self.matrix[grain_coords.y][grain_coords.x] = Grain(coords=grain_coords, color=self.get_next_color(),
                                                            canvas=self.canvas, square_side=self.square_side)

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

    def fall(self):
        return

    @staticmethod
    def init_matrix(width: int, height: int):
        matrix: [Optional[Grain], ...] = []
        for _ in range(0, height):
            row = []
            for _ in range(0, width):
                row.append(None)
            matrix.append(row)
        return matrix

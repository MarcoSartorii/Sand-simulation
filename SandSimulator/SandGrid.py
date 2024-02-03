from tkinter import Canvas
from typing import Optional

from CONSTS import GridDimensions, Coords, SATURATION, OPACITY, DEGREES
from Grain import Grain
from Hue import Hue


class SandGrid:
    canvas: Canvas
    grid: GridDimensions
    square_side: int
    hue: Hue
    matrix: Optional

    def __init__(self, canvas: Canvas, grid: GridDimensions, square_side: int):
        self.hue = Hue(start_h=0, saturation=SATURATION, transparency=OPACITY, degrees=DEGREES)
        self.grid = grid
        self.canvas = canvas
        self.square_side = square_side
        self.matrix: Optional[Optional[Grain], ...] = self.init_matrix(grid.WIDTH, grid.HEIGHT)

    def add_grain(self, mouse_pos: Coords) -> type(None):
        grain: Optional[Grain, ...] = self.get_grain_coords(mouse_pos)
        if grain is None:
            return
        if self.matrix[grain.coords.y][grain.coords.x] is None:  # if the position is free
            self.matrix[grain.coords.y][grain.coords.x] = Grain(coords=grain.coords, canvas=self.canvas,
                                                                color=self.hue.next_color(),
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
        self.matrix[grain_coords.y][grain_coords.x] = Grain(coords=grain_coords, color=self.hue.next_color(),
                                                            canvas=self.canvas, square_side=self.square_side)

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

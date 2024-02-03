from tkinter import Canvas
from CONSTS import Coords, MARGIN


class Grain:
    coords: Coords
    color: str
    canvas: Canvas

    def __init__(self, coords: Coords, canvas: Canvas, color: str = None, square_side=None):
        self.square_side = square_side
        self.color = color
        self.coords = coords
        self.canvas = canvas

    def move_down(self, new_coords: Coords):
        self.coords = new_coords

    def draw(self):
        self.canvas.create_rectangle(
            self.coords.x * self.square_side + MARGIN,
            self.coords.y * self.square_side + MARGIN,
            self.coords.x * self.square_side + self.square_side - MARGIN,
            self.coords.y * self.square_side + self.square_side - MARGIN,
            fill=self.color,
            outline=""
        )

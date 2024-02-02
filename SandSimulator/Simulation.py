from collections import namedtuple
from typing import Final
import tkinter
from CONSTS import BACKGROUND_COLOR, WIDTH, HEIGHT, GRID, FPS, GRAIN_SIDE_SIZE, DRAW_GRID_LINES, Coords
from Sand import Sand

Event = namedtuple("Event", "char")
MILLISECONDS: Final = 1000 // FPS


class Simulation:
    window: tkinter.Tk
    canvas: tkinter.Canvas
    is_mouse_pressed: bool
    sand: Sand
    matrix: [[], ...]

    def __init__(self):
        self.is_mouse_pressed = False
        self.init_gui()
        self.init_key_binds()
        self.sand = Sand(self.canvas, GRID, GRAIN_SIDE_SIZE)
        self.matrix = self.init_matrix()

    def init_gui(self):
        self.window = tkinter.Tk()
        self.window.geometry(f"{WIDTH}x{HEIGHT}")
        self.canvas = tkinter.Canvas(self.window, bg=BACKGROUND_COLOR, width=WIDTH, height=HEIGHT)
        if DRAW_GRID_LINES:
            self.draw_grid_lines()
        self.window.title(f"Sand simulator! {GRID.WIDTH}x{GRID.HEIGHT}")
        self.canvas.pack()

    def init_key_binds(self):
        self.window.bind("<ButtonPress-1>", self.mouse_pressed)
        self.window.bind("<Button 1>", self.mouse_pressed)
        self.window.bind("<ButtonRelease-1>", self.mouse_released)

    def update(self):
        self.update_canvas()
        mouse_x, mouse_y = self.get_mouse_pos()
        mouse_coords = Coords(mouse_x, mouse_y)
        if self.is_mouse_pressed:
            self.draw_grain(mouse_coords)
        self.update_matrix_gravity(mouse_coords)
        self.window.after(ms=MILLISECONDS, func=self.update)

    def update_canvas(self):
        self.canvas.update()

    def start(self):
        self.window.after(MILLISECONDS, self.update)
        self.window.resizable(False, False)
        self.window.mainloop()

    def game_over(self):
        self.window.destroy()

    def mouse_pressed(self, event):
        _ = event
        self.is_mouse_pressed = True

    def mouse_released(self, event):
        _ = event
        self.is_mouse_pressed = False

    def get_mouse_pos(self):
        return (
            self.window.winfo_pointerx() - self.window.winfo_rootx(),
            self.window.winfo_pointery() - self.window.winfo_rooty()
        )

    def draw_grain(self, mouse_coords: Coords):
        self.sand.create_grain(mouse_coords, self.matrix)

    def draw_grid_lines(self):
        for i in range(0, GRID.WIDTH):
            self.canvas.create_line(
                i * GRAIN_SIDE_SIZE,
                0,
                i * GRAIN_SIDE_SIZE,
                GRID.HEIGHT * GRAIN_SIDE_SIZE
            )
            self.canvas.create_line(
                0,
                i * GRAIN_SIDE_SIZE,
                GRID.WIDTH * GRAIN_SIDE_SIZE,
                i * GRAIN_SIDE_SIZE,
            )

    @staticmethod
    def init_matrix():
        matrix: [[], ...] = []
        for _ in range(0, GRID.HEIGHT):
            row = []
            for _ in range(0, GRID.WIDTH):
                row.append(True)
            matrix.append(row)
        print(matrix)
        return matrix

    def update_matrix_gravity(self, mouse_coords):
        grain_coords: Coords = self.sand.get_grain_coords(mouse_coords)
        if grain_coords is None:
            return
        if self.matrix[grain_coords.x][grain_coords.y]:
            self.matrix[grain_coords.x][grain_coords.y] = False

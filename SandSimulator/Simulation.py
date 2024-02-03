from collections import namedtuple
from typing import Final
import tkinter
from CONSTS import BACKGROUND_COLOR, WIDTH, HEIGHT, GRID, FPS, GRAIN_SIDE_SIZE, DRAW_GRID_LINES, Coords
from SandGrid import SandGrid
from Colors import Colors

Event = namedtuple("Event", "char")
MILLISECONDS: Final = 1000 // FPS


def green(msg):
    print(Colors().green + msg, end="")


def red(msg):
    print(Colors().red + msg, end="")


class Simulation:
    window: tkinter.Tk
    canvas: tkinter.Canvas
    is_mouse_pressed: bool
    sandGrid: SandGrid

    def __init__(self):
        self.is_mouse_pressed = False
        self.init_gui()
        self.init_key_binds()
        self.sandGrid = SandGrid(self.canvas, GRID, GRAIN_SIDE_SIZE)

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
        if self.is_mouse_pressed:
            mouse_x, mouse_y = self.get_mouse_pos()
            mouse_coords = Coords(mouse_x, mouse_y)
            self.sandGrid.add_grain(mouse_coords)
        self.sandGrid.fall()
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

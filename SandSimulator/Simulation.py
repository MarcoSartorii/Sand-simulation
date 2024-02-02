from collections import namedtuple
from threading import Thread
from typing import Final
import tkinter
from CONSTS import BACKGROUND_COLOR, WIDTH, HEIGHT, GRID, FPS, SQUARE_SIDE, DRAW_GRID_LINES, Coords
from Sand import Sand
Event = namedtuple("Event", "char")
MILLISECONDS: Final = 1000 // FPS


class Simulation:
    window: tkinter.Tk
    canvas: tkinter.Canvas
    is_mouse_pressed: bool
    sand: Sand

    def __init__(self):
        self.is_mouse_pressed = False
        self.init_gui()
        self.init_key_binds()
        self.sand = Sand(self.canvas, GRID, SQUARE_SIDE)

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
            self.draw_sand()
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

    def draw_sand(self):
        mouse_coords = Coords(self.get_mouse_pos()[0], self.get_mouse_pos()[1])
        self.sand.create_grain(mouse_coords)

    def draw_grid_lines(self):
        for i in range(0, GRID.WIDTH):
            self.canvas.create_line(
                i*SQUARE_SIDE,
                0,
                i*SQUARE_SIDE,
                GRID.HEIGHT*SQUARE_SIDE
            )
            self.canvas.create_line(
                0,
                i*SQUARE_SIDE,
                GRID.WIDTH*SQUARE_SIDE,
                i*SQUARE_SIDE,
            )

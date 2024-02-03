import colorsys

from CONSTS import COLOR_CHANGE_SPEED


class Hue:
    hue: int
    saturation: float
    transparency: float
    degrees: int

    def __init__(self, start_h=0, saturation=1, transparency=0, degrees=360):
        self.hue = start_h
        self.saturation = saturation
        self.transparency = transparency
        self.degrees = degrees

    def next_color(self):
        rgb = colorsys.hsv_to_rgb(self.hue, self.saturation, self.transparency)
        self.hue += COLOR_CHANGE_SPEED / self.degrees
        self.hue %= 1  # cap hue at 1.0
        r = round(rgb[0] * 255)
        g = round(rgb[1] * 255)
        b = round(rgb[2] * 255)
        rgb_ints = (r, g, b)
        return self._from_rgb(rgb_ints)

    @staticmethod
    def _from_rgb(rgb):
        return "#%02x%02x%02x" % rgb


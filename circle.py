from drawable import Drawable
from drawable import Coord


class Circle(Drawable):
    def __init__(self, x, y, radius):
        self.pos = Coord(x, y)
        self.radius = radius

    def draw(self, pen):
        self.move_pen(pen, self.pos)
        pen.circle(self.radius)

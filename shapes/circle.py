from shapes.drawable import Drawable


class Circle(Drawable):
    def __init__(self, coord: tuple, radius):
        self.pos = coord
        self.radius = radius

    def draw(self, pen):
        self.move_pen(pen, self.pos)
        pen.begin_fill()
        pen.circle(self.radius)
        pen.end_fill()

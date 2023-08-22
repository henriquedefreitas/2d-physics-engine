from shapes.drawable import Drawable


class Circle(Drawable):
    def __init__(self, coord: tuple, radius, color="white"):
        self.pos = coord
        self.color = color
        self.radius = radius

    def draw(self, pen):
        self.move_pen(pen, self.pos)
        pen.color(self.color)
        pen.dot(self.radius * 2)

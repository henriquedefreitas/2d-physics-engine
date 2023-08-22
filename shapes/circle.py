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
        
    def handle_collision(self, wall):
        if self.pos[0] - self.radius < wall[0][0] or self.pos[0] + self.radius > wall[0][1]:
            return (-0.6, 1)
        if self.pos[1] - self.radius < wall[1][0] or self.pos[1] + self.radius > wall[1][1]:
            return (1, -0.6)
        return (1, 1)

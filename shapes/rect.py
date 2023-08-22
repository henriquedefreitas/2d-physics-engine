from shapes.drawable import Drawable


class Rect(Drawable):
    def __init__(self, p1: tuple, p2: tuple, color="white"):
        self.pos = (p1[0] + p2[0] // 2, p1[1] + p2[1] // 2)
        self.color = color
        self.p1 = p1
        self.p2 = p2

    def draw(self, pen):
        self.move_pen(pen, self.p1)
        pen.color(self.color)
        pen.begin_fill()
        pen.goto((self.p1[0], self.p2[1]))
        pen.goto((self.p2[0], self.p2[1]))
        pen.goto((self.p2[0], self.p1[1]))
        pen.goto((self.p1[0], self.p1[1]))
        pen.end_fill()
        
    def handle_collision(self, *args):
        return (1, 1)

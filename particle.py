from shapes.drawable import Drawable


class Particle:
    def __init__(self, shape: Drawable, acceleration=(0, 0), velocity=(0, 0)):
        self.shape = shape
        self.velocity = velocity
        self.acceleration = acceleration

    def draw(self, pen):
        self.shape.draw(pen)

    def update_velocity(self):
        self.velocity = tuple(map(lambda x, y: x + y, self.velocity, self.acceleration))

    def update_position(self):
        self.pos = tuple(map(lambda x, y: x + y, self.pos, self.velocity))

    @property
    def pos(self):
        return self.shape.pos

    @pos.setter
    def pos(self, coord):
        self.shape.pos = coord

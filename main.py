import time
import turtle
from shapes.circle import Circle
from shapes.rect import Rect
from particle import Particle
from pencil import Pencil

turtle.colormode(255)
turtle.tracer(0, 0)

FPS = 24
WIDTH = 800
HEIGHT = 600
MIN_WIDTH = -WIDTH / 2
MAX_WIDTH = WIDTH / 2
MAX_HEIGHT = HEIGHT / 2
MIN_HEIGHT = -HEIGHT / 2

SCREEN = turtle.Screen()
SCREEN.bgcolor("black")
PEN = Pencil("pen_config.json")

obj_array = [
    Particle(Rect((MIN_WIDTH, MIN_HEIGHT), (MAX_WIDTH, MAX_HEIGHT), color="black")),
    Particle(Circle((0, 280), 30, color="purple"), acceleration=(0, -1)),
]


def setup():
    pass


def update():
    global obj_array
    for obj in obj_array:
        obj.update_velocity()
        obj.update_position()


def show():
    for obj in obj_array:
        obj.draw(PEN)
    turtle.update()


if __name__ == "__main__":
    setup()
    while True:
        update()
        show()
        time.sleep(1 / FPS)

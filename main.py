import time
import turtle
from shapes.circle import Circle
from particle import Particle
from pencil import Pencil

FPS = 10
SCREEN = turtle.getscreen()
PEN = Pencil('pen_config.json')

obj_array = [Particle(Circle((0, 300), 30), acceleration=(0, -10))]

def setup():
    pass

def update():
    global obj_array
    for obj in obj_array:
        obj.update_velocity()
        obj.update_position()

def show():
    SCREEN.clearscreen()
    for obj in obj_array:
        obj.draw(PEN)
        
if __name__ == '__main__':
    setup()
    while True:
        update()
        show()
        time.sleep(1/FPS)
        
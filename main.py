import time
import turtle
from circle import Circle
from pencil import Pencil

s = turtle.getscreen()
pen = Pencil('pen_config.json')
c = Circle(0, 0, 15)

cont = 0

def update():
    global cont, c
    cont += 1
    c = Circle(cont*10, cont*10, cont*10)

def show():
    c.draw(pen)

def setup():
    s.clear()
        
if __name__ == '__main__':
    setup()
    while True:
        update()
        show()
        time.sleep(1)
        
from abc import ABC, abstractmethod
from dataclasses import dataclass
import turtle

from pencil import Pencil


@dataclass
class Coord:
    x: int
    y: int


class Drawable(ABC):
    def __init__(self, x, y):
        self.pos = Coord(x, y)

    @abstractmethod
    def draw():
        ...

    def move_pen(self, pen: Pencil, pos: Coord):
        pen.penup()
        pen.goto(pos.x, pos.y)
        pen.pendown()

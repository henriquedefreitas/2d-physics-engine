from abc import ABC, abstractmethod
from dataclasses import dataclass

from pencil import Pencil


@dataclass
class Coord:
    x: int
    y: int


class Drawable(ABC):
    def __init__(self, coord: tuple):
        self.pos = coord

    @abstractmethod
    def draw():
        ...

    def move_pen(self, pen: Pencil, pos: tuple):
        pen.penup()
        pen.goto(pos[0], pos[1])
        pen.pendown()

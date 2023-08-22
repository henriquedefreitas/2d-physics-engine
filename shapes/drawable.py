from abc import ABC, abstractmethod
from dataclasses import dataclass

from pencil import Pencil


class Drawable(ABC):
    def __init__(self, coord: tuple, color="white"):
        self.pos = coord
        self.color = color

    @abstractmethod
    def draw():
        ...

    def move_pen(self, pen: Pencil, pos: tuple):
        pen.penup()
        pen.goto(pos)
        pen.pendown()

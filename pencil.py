import json
from turtle import Turtle


class Pencil(Turtle):
    def __init__(self, config_file):
        super().__init__()
        with open(config_file, "r") as file:
            config = json.load(file)
        self.pen(config)

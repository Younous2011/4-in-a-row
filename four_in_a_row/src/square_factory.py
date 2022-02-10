from .square import Square
from .position import Position

class SquareFactory:
    def __init__(self):
        pass

    def create(self, position:Position, side:int):
        return Square(position, side)
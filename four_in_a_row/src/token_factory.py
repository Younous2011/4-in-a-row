from .letter import Letter
from .circle import Circle
from .token import Token
from .position import Position
from .color import Color

class TokenFactory:
    def __init__(self):
        pass

    def create(self, id:int, radius:int, color:Color, color2:Color, letter:str, p_edge:float = 4 / 5):
        position = Position(radius, radius)
        large_circle = Circle(radius, color, position)
        medium_circle = Circle(int(radius * p_edge), color2, position)
        t_letter = Letter(position, letter, radius*2, color)
        return Token(position, large_circle, medium_circle, id, t_letter)
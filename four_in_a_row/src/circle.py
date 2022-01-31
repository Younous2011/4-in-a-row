from position import Position
from color import Color

class Circle:
    """
        Cette class permet de définir et de manipuler un cercle
    """

    def __init__(self, radius:int, color:Color, position:Position):
        self.radius = radius
        self.color = color
        self.position = position
    
    def set_position(self, position:Position):
        self.position = position

    def get_position(self) -> Position:
        return self.position

    def get_color(self) -> Color:
        return self.color

    def get_radius(self) -> int:
        return self.radius
from .text_interface import TextInterface
from .color import WHITE, Color
from .position import Position

class Alert(TextInterface):
    def __init__(
        self,
        position:Position,
        message:str,
        size:int,
        color:Color,
        background_color:Color,
        side:int, 
        length:int, 
        height:int
    ):
        self.side = side
        self.length = length
        self.height = height
        rect_dim = (side * self.length, side * self.height * 0.5)
        super().__init__(position, message, size, color, background_color, rect_dim)
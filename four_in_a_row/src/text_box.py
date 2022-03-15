from .position import Position
from .color import Color
from .text_interface import TextInterface

class TextBox(TextInterface):
    def __init__(
        self,
        position:Position, 
        text:str, 
        size:int, 
        color:Color,
        background_color:Color,
        rect_dim:tuple,
        alpha:int = 255, 
        font_str:str = None
    ):
        super().__init__(position, text, size, color, background_color, rect_dim, alpha, font_str)
import pygame

from .text_interface import TextInterface
from .position import Position
from .color import Color

class Button(TextInterface):
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
    
    def click(self):
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            return "restart"

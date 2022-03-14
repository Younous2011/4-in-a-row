from .position import Position
from .color import Color
from .text_interface import TextInterface

import pygame
from pygame import Surface

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

    def blit_in(self, screen:Surface):
        screen.blit(self.surface, (self.position.x, self.position.y))

    def update(self, text:str):
        self.text = text
        self.make()
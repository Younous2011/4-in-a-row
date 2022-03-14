from .position import Position
from .color import Color

import pygame
from pygame import Surface

class TextInterface:
    def __init__(
        self,
        position:Position, 
        text:str, 
        size:int, 
        color:Color,
        bacground_color:Color,
        rect_dim:tuple,
        alpha:int = 255, 
        font_str:str = None
    ):
        self.text = text
        self.size = size
        self.color = color
        self.background_color = bacground_color
        self.rect_dim = rect_dim
        self.alpha = alpha
        self.font_str = font_str
        self.position = position
        self.make()
    
    def make(self):
        self.surface = pygame.Surface(self.rect_dim)
        self.surface.fill(self.background_color.get())
        self.font = pygame.font.Font(self.font_str, self.size)
        self.text = self.font.render(self.text, True, self.color.get(), None)
        self.text.set_alpha(self.alpha)
        self.textRect = self.text.get_rect()
        self.textRect.center = self.position.get_position()
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.position.x, self.position.y, self.rect_dim[0], self.rect_dim[1])

    def click(self):
        print("text interface clicked")
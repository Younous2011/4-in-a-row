from pygame import Surface
from .position import Position
from .color import Color

import pygame.gfxdraw

class Circle:
    
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

    def draw(self, screen:Surface):
        pygame.gfxdraw.filled_circle(screen, self.position.get_x(), self.position.get_y(), self.radius, self.color.get())
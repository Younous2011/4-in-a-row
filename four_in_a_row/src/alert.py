from turtle import position
import pygame
from pygame import Surface

from .color import WHITE, Color
from .position import Position
from .text_box import TextBox

class Alert:
    def __init__(self, side:int, length:int, height:int, message:str):
        self.side = side
        self.length = length
        self.height = height
        self.message = message
        self.surface = pygame.Surface((self.side * self.length, self.side * self.height))
        self.alert = TextBox(Position(0, 0), self.message, 100, WHITE, Color(255, 194, 133), (200, 100))

    def blit_in(self, screen:Surface):
        position = Position(50, 50)
        screen.blit(self.surface, position.get_position())

    def click(self):
        pass

    def update(self):
        self.surface.fill((255, 194, 133))
        self.alert.blit_in(self.surface)
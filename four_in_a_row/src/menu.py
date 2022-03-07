import pygame
from pygame import Surface

from .color import WHITE, Color
from .button import Button
from .position import Position

class Menu:
    def __init__(self, side:int, length:int, height:int):
        self.side = side
        self.length = length
        self.height = height
        self.surface = pygame.Surface((self.side * self.length, self.side * self.height))
        self.button = Button(Position(length / 2 * side - 80, 100), "Rejouer", 50, WHITE, Color(255, 194, 133), (160, 60))

    def blit_in(self, screen:Surface):
        position = Position(0, 0)
        screen.blit(self.surface, position.get_position())

    def click(self):
        self.button.click()

    def update(self):
        self.surface.fill((255, 194, 133))
        self.button.blit_in(self.surface)
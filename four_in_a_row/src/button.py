import click
import pygame
from pygame import Surface

from .position import Position
from .color import Color

class Button:
    def __init__(self, position:Position, letter:str, size:int, color:Color, alpha:int = 255, font_str:str = None):
        self.letter = letter
        self.size = size
        self.color = color
        self.alpha = alpha
        self.font_str = font_str
        self.position = position
        self.make()

    def make(self):
        self.surface = pygame.Surface((100, 30))
        self.font = pygame.font.Font(self.font_str, self.size)
        self.text = self.font.render(self.letter, True, self.color.get(), None)
        self.text.set_alpha(self.alpha)
        self.textRect = self.text.get_rect()
        self.textRect.center = self.position.get_position()
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(0, 0, 100, 30)

    def blit_in(self, screen:Surface):
        screen.blit(self.surface, (self.position.x, self.position.y))

    def click(self, p:Position):
        if self.rect.collidepoint(p.x, p.y):
            print("clicked")

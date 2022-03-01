from turtle import position
import pygame
from pygame import Surface

from four_in_a_row.src.position import Position

class Menu:
    def __init__(self, side:int, length:int, height:int):
        self.side = side
        self.length = length
        self.height = height
        self.surface = pygame.Surface((self.side * self.length, self.side * self.height))

    def blit_in(self, screen:Surface):
        position = Position(0, 0)
        screen.blit(self.surface, position.get_position())

    def update(self):
        self.surface.fill((255, 194, 133))
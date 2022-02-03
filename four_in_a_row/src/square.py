from four_in_a_row.src.color import BLUE
from .position import Position

from pygame import Surface
import pygame.gfxdraw
import pygame

class Square:
    def __init__(self, position:Position, side:int):
        self.position = position
        self.side = side
        self.rect = pygame.Rect(position.get_x(), position.get_y(), side, side)

    def draw(self, screen:Surface):
        pygame.gfxdraw.box(screen, self.rect, BLUE.get())

BLUE_POSITION = Position(200, 200)
BLUE_SQUARE = Square(BLUE_POSITION, 190)
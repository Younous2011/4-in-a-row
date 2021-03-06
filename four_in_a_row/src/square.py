from .circle import Circle
from .color import BLUE, BLACK
from .position import Position

from pygame import Surface
import pygame.gfxdraw
import pygame

class Square:
    def __init__(self, position:Position, side:int):
        self.position = position
        self.side = side
        self.rect = pygame.Rect(0, 0, side, side)
        self.circle = Circle(int(side // 2 * 90/100), BLACK, Position(side // 2, side//2))
        # self.rect.center = position.get_position()
        self.draw()

    def draw(self):
        size = (self.side, self.side)
        self.surface = pygame.Surface(size)
        self.surface.set_colorkey(BLACK.get())
        pygame.gfxdraw.box(self.surface, self.rect, BLUE.get())
        self.circle.draw(self.surface)

    def blit_in(self, screen:Surface):
        screen.blit(self.surface, self.position.get_position())


BLUE_POSITION = Position(100, 100)
BLUE_SQUARE = Square(BLUE_POSITION, 200)
# Import local Class
from .color import RED, RED_DARK, YELLOW, YELLOW_DARK, BLACK
from .position import Position
from .circle import Circle
from .letter import Letter

from pygame.surface import Surface
import pygame



class Token:
    def __init__(self, position:Position, circle1:Circle, circle2:Circle, id:int, letter:Letter):
        self.position = position
        self.circle1 = circle1
        self.circle2 = circle2
        self.id = id
        self.letter = letter
        self.draw()

    def draw(self):
        radius = self.circle1.get_radius()
        size = (radius*2 + 1, radius*2 + 1)
        self.surface = pygame.Surface(size)
        self.surface.set_colorkey(BLACK.get())
        self.circle1.draw(self.surface)
        self.circle2.draw(self.surface)
        self.letter.draw(self.surface)
    
    def set_position(self, position:Position):
        self.position = position
        """ self.circle1.set_position(position)
        self.circle2.set_position(position)
        self.letter.set_position(position) """

    def blit_in(self, screen:Surface):
        screen.blit(self.surface, self.position.get_top_left_position(self.circle1.radius))


RED_RAYON = 75



RED_POSITION = Position(RED_RAYON, RED_RAYON)
RED_LARGE_CIRCLE = Circle(RED_RAYON, RED, RED_POSITION)
RED_MEDIUM_CIRCLE = Circle(int(RED_RAYON * 4 / 5), RED_DARK, RED_POSITION)
RED_LETTER = Letter(RED_POSITION, "R", 100, RED)
RED_TOKEN = Token(RED_POSITION, RED_LARGE_CIRCLE, RED_MEDIUM_CIRCLE, 1, RED_LETTER)

YELLOW_RADIUS = 75

YELLOW_POSITION = Position(YELLOW_RADIUS, YELLOW_RADIUS)
YELLOW_LARGE_CIRCLE = Circle(YELLOW_RADIUS, YELLOW, YELLOW_POSITION)
YELLOW_MEDIUM_CIRCLE = Circle(int(YELLOW_RADIUS * 4 / 5), YELLOW_DARK, YELLOW_POSITION)
YELLOW_LETTER = Letter(YELLOW_POSITION, "Y", 100, YELLOW)
YELLOW_TOKEN = Token(YELLOW_POSITION, YELLOW_LARGE_CIRCLE, YELLOW_MEDIUM_CIRCLE, 1, YELLOW_LETTER)
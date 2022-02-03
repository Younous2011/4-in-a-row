# Import local Class
from four_in_a_row.src.color import RED, RED_DARK, YELLOW, YELLOW_DARK
from .position import Position
from .circle import Circle
from .letter import Letter

from pygame.surface import Surface



class Token:
    def __init__(self, position:Position, circle1:Circle, circle2:Circle, id:int, letter:Letter):
        self.position = position
        self.circle1 = circle1
        self.circle2 = circle2
        self.id = id
        self.letter = letter

    def draw(self, screen:Surface):
        self.circle1.draw(screen)
        self.circle2.draw(screen)
        self.letter.draw(screen)
        
    def set_position(self, position:Position):
        self.position = position
        self.circle1.set_position(position)
        self.circle2.set_position(position)
        self.letter.set_position(position)


RED_POSITION = Position(250, 250)
RED_LARGE_CIRCLE = Circle(95, RED, RED_POSITION)
RED_MEDIUM_CIRCLE = Circle(75, RED_DARK, RED_POSITION)
RED_LETTER = Letter(RED_POSITION, "R", 100, RED)
RED_TOKEN = Token(RED_POSITION, RED_LARGE_CIRCLE, RED_MEDIUM_CIRCLE, 1, RED_LETTER)

YELLOW_POSITION = Position(100, 100)
YELLOW_LARGE_CIRCLE = Circle(95, YELLOW, YELLOW_POSITION)
YELLOW_MEDIUM_CIRCLE = Circle(75, YELLOW_DARK, YELLOW_POSITION)
YELLOW_LETTER = Letter(YELLOW_POSITION, "Y", 100, YELLOW)
YELLOW_TOKEN = Token(YELLOW_POSITION, YELLOW_LARGE_CIRCLE, YELLOW_MEDIUM_CIRCLE, 1, YELLOW_LETTER)
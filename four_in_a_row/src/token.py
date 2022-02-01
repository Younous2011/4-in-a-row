# Import local Class
from position import Position
from circle import Circle
from pygame.surface import Surface



class Token:
    def __init__(self, position:Position, circle1:Circle, circle2:Circle, id:int, letter:str):
        self.position = position
        self.circle1 = circle1
        self.circle2 = circle2
        self.id = id
        self.letter = letter

    def draw(self, screen:Surface):
        pass
        

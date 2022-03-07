
from pygame import Surface
import pygame

from .color import BLACK
from .position import Position
from .square_factory import SquareFactory

class Grill:
    def __init__(self, side:int, nb_lignes:int, nb_colonnes:int, position:Position, translation:int):
        self.side = side
        self.nb_lignes = nb_lignes
        self.nb_colonnes = nb_colonnes
        self.position = position
        self.translation = translation
        self.ls = []
        for j in range(nb_lignes):
            for i in range(nb_colonnes):
                p = Position(side * i, side * j)
                s = SquareFactory().create(p, side)
                self.ls.append(s)
        
        self.draw()

    def draw(self):
        self.surface = pygame.Surface((self.side * self.nb_colonnes, self.side * self.nb_lignes))
        self.surface.set_colorkey(BLACK.get())
        for s in self.ls:
            s.blit_in(self.surface)

    def blit_in(self, screen:Surface):
        screen.blit(self.surface, self.position.get_position())
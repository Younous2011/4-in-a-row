from .token import Token
from .position import Position
from .color import BLACK

import pygame
from pygame import Surface

class GrillToken:
    def __init__(self, side:int, nb_lignes:int, nb_colonnes:int, position:Position):
        self.side = side
        self.nb_lignes = nb_lignes
        self.nb_colonnes = nb_colonnes
        self.position = position
        self.l_grill = self.side * self.nb_lignes
        self.L_grill  = self.side * nb_colonnes
        self.surface = pygame.Surface((self.l_grill, self.L_grill))
        self.surface.set_colorkey(BLACK.get())

    def blit_in(self, screen:Surface):
        screen.blit(self.surface, self.position.get_position())

    def add_token(self, token:Token, i:int, j:int):
        p = Position().get_position_token(i, j, self.side, self.L_grill)
        token.set_position(p)
        token.blit_in(self.surface)
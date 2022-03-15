import pygame
from pygame import Surface

from .text_box import TextBox
from .color import MENU_COLOR, WHITE, Color
from .button import Button
from .position import Position

class Menu:
    def __init__(self, side:int, length:int, height:int, joueur1:str, joueur2:str):
        self.side = side
        self.length = length
        self.height = height
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.surface = pygame.Surface((self.side * self.length, self.side * self.height))
        self.button = Button(Position(length / 2 * side - 70, 100), "Rejouer", 55, WHITE, Color(255, 194, 133), (160, 60))
        self.score_player1 = TextBox(Position(length / 2 * side - 70, 350), f"{joueur1} : 0", 30, WHITE, Color(255, 194, 133), (200, 60))
        self.score_player2 = TextBox(Position(length / 2 * side - 70, 400), f"{joueur2} : 0", 30, WHITE, Color(255, 194, 133), (160, 60))

    def blit_in(self, screen:Surface):
        position = Position(0, 0)
        screen.blit(self.surface, position.get_position())

    def click(self):
        action = self.button.click()
        return action

    def update(self):
        self.surface.fill(MENU_COLOR.get())
        self.button.blit_in(self.surface)
        self.score_player1.blit_in(self.surface)
        self.score_player2.blit_in(self.surface)
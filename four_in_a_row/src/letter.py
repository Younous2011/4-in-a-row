from .color import Color
from .position import Position
from pygame.surface import Surface

# Import pygame
import pygame

class Letter:
    def __init__(self, position:Position, letter:str, size:int, color:Color, alpha:int = 255, font:str = None):
        self.letter = letter
        self.size = size
        self.color = color
        self.alpha = alpha
        self.font = font
        self.position = position

    def make(self):
        # Lecture de la police
        self.font = pygame.font.Font(self.font, self.size)

        # Preparation du texte
        self.text = self.font.render(self.letter, True, self.color.get(), None)

        self.text.set_alpha(self.alpha)

        # Recupération de l'emplacement du texte et paramètrage de la position
        self.textRect = self.text.get_rect()
        self.textRect.center = self.position.get_position()

    def set_position(self, position:Position):
        self.position = position
        self.textRect.center = self.position.get_position()

    def draw(self, screen:Surface):
        screen.blit(self.text, self.textRect)

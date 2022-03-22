import pygame

from .position import Position
from .color import Color
from .text_interface import TextInterface

class TextInput(TextInterface):
    def __init__(
        self,
        position:Position, 
        size:int, 
        color:Color,
        background_color:Color,
        rect_dim:tuple,
        alpha:int = 255, 
        font_str:str = None
    ):
        text = ""
        super().__init__(position, text, size, color, background_color, rect_dim, alpha, font_str)
        
        self.active=False
    
    def on_event(self, events=None):
        if events is None:
            events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.active = True
                else:
                    self.active = False

            if event.type == pygame.KEYDOWN and self.active:
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
    
                    # get text input from 0 to -1 i.e. end.
                    self.text_str = self.text_str[:-1]
    
                # Unicode standard is used for string
                # formation
                else:
                    self.text_str += event.unicode
        
                self.make()
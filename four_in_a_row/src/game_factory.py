import pygame

from .position import Position
from .grill import Grill
from .grill_token import GrillToken
from .player_factory import PlayerFactory
from .game import Game
from .menu import Menu
from .color import *

class GameFactory:
    def __init__(self):
        pass

    def create(self, side:int, nb_rows:int, nb_columns:int, name_player1:str, name_player2:str):
        translation = 3
        p = Position(translation * side, side)
        g = Grill(side, nb_rows, nb_columns, p, translation)
        gt = GrillToken(side, nb_rows, nb_columns, p)
        player1 = PlayerFactory().create(name_player1, side // 2, RED, RED_DARK)
        player2 = PlayerFactory().create(name_player2, side // 2, YELLOW, YELLOW_DARK)
        screen = pygame.display.set_mode([nb_columns * side + translation * side, nb_rows * side + side])
        menu = Menu(side, translation, nb_rows + 1, name_player1, name_player2)
        game = Game(nb_rows, nb_columns, player1, player2, gt, g, menu, screen)

        return game
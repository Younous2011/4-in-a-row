import pygame

from .position import Position
from .grill import Grill
from .grill_token import GrillToken
from .player_factory import PlayerFactory
from .game import Game
from .menu import Menu
from .color import *
from .conf import Conf

class GameFactory:
    def __init__(self):
        pass

    def create(self, conf:Conf, name_player1:str, name_player2:str) -> Game:
        translation = 3
        p = Position(translation * conf.side, conf.side)
        g = Grill(conf.side, conf.nb_rows, conf.nb_columns, p, translation)
        gt = GrillToken(conf.side, conf.nb_rows, conf.nb_columns, p)
        player1 = PlayerFactory().create(name_player1, conf.side // 2, RED, RED_DARK)
        player2 = PlayerFactory().create(name_player2, conf.side // 2, YELLOW, YELLOW_DARK)
        screen = pygame.display.set_mode([conf.nb_columns * conf.side + translation * conf.side, conf.nb_rows * conf.side + conf.side])
        menu = Menu(conf.side, translation, conf.nb_rows + 1, name_player1, name_player2)
        game = Game(conf, player1, player2, gt, g, menu, screen)

        return game
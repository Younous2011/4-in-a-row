from .position import Position
from .grill import Grill
from .grill_token import GrillToken
from .player_factory import PlayerFactory
from .game import Game

from .color import *

class GameFactory:
    def __init__(self):
        pass

    def create(self, side:int, nb_rows:int, nb_columns:int, name_player1:str, name_player2:str):
        p = Position(0, side)
        g = Grill(side, nb_rows, nb_columns, p)
        gt = GrillToken(side, nb_rows, nb_columns, p)
        player1 = PlayerFactory().create(name_player1, side // 2, RED, RED_DARK)
        player2 = PlayerFactory().create(name_player2, side // 2, YELLOW, YELLOW_DARK)
        game = Game(nb_rows, nb_columns, player1, player2, gt, g)

        return game
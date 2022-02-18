import numpy as np

from .token import Token
from .player import Player
from .position import Position
from .grill_token import GrillToken

class Game:

    def __init__(self, nb_lignes:int, nb_colonnes:int, player1:Player, player2:Player, grill_token:GrillToken):
        self.nb_lignes = nb_lignes
        self.nb_colonnes = nb_colonnes
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.grill_token = grill_token
        self.grill = np.zeros((nb_lignes, nb_colonnes), dtype=int)
        self.nb_token_column = np.zeros(nb_colonnes, dtype=int)

    def add_token(self, token:Token, column:int):
        token_id = token.id
        row = self.nb_token_column[column]
        self.grill[row, column] = token_id
        self.nb_token_column[column] += 1
        print(self.grill)

    def get_next_row(self, column:int):
        return self.nb_token_column[column]

    def swipe_player(self):
        if self.current_player.token.id == 1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def click(self, x:int):
        column = Position(x, 0).get_column(self.grill_token.side)
        row = self.get_next_row(column)
        if row < self.nb_lignes:
            self.grill_token.add_token(self.current_player.token, row, column)
            self.add_token(self.current_player.token, column)
            self.swipe_player()

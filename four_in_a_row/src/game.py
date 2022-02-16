from curses.textpad import rectangle
from socket import gaierror
import weakref
import numpy as np
from sklearn.metrics import jaccard_score

from .token import Token
from .player import Player

class Game:
    def __init__(self, nb_lignes:int, nb_colonnes:int, player1:Player, player2:Player):
        self.nb_lignes = nb_lignes
        self.nb_colonnes = nb_colonnes
        self.player1 = player1
        self.player2 = player2
        self.grill = np.zeros((nb_lignes, nb_colonnes))
        self.nb_token_column = np.zeros(nb_lignes)

    def add_token(self, token:Token, column:int):
        token_id = token.id
        row = self.nb_token_column[column]
        # self.grill[row, column] = token_id
        self.nb_token_column[column] += 1

    def get_next_row(self, column:int):
        return self.nb_token_column[column]
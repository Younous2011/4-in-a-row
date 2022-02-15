import numpy as np
from .player import Player

class Game:
    def __init__(self, nb_lignes:int, nb_colonnes:int, player1:Player, player2:Player):
        self.nb_lignes = nb_lignes
        self.nb_colonnes = nb_colonnes
        self.player1 = player1
        self.player2 = player2
        self.grill = np.zeros((nb_lignes, nb_colonnes))
        self.nb_token_column = np.zeros(nb_lignes)

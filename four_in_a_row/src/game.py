import numpy as np

from .token import Token
from .player import Player
from .position import Position
from .grill_token import GrillToken

class Game:

    def __init__(self, nb_lignes:int, nb_colonnes:int, player1:Player, player2:Player, grill_token:GrillToken, n_rows:int = 4):
        self.nb_lignes = nb_lignes
        self.nb_colonnes = nb_colonnes
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.grill_token = grill_token
        self.grill = np.zeros((nb_lignes, nb_colonnes), dtype=int)
        self.nb_token_column = np.zeros(nb_colonnes, dtype=int)
        self.n_rows = n_rows

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
            print(f"full : {self.check_full()}")
            print(f"{self.current_player.name} a gagné {self.check_grill()} !")
            self.swipe_player()

    def check_grill(self):
        b = self.check_rows() or self.check_columns() or self.check_diagonales_left() or self.check_diagonales_right()
        return b
    
    def check_rows(self):
        id = self.current_player.token.id
        grill = self.grill
        j = 0
        count_id = 0
        while j < self.nb_lignes and count_id < self.n_rows:
            i = 0
            while i < self.nb_colonnes and count_id < self.n_rows:
                if grill[j][i] == id:
                    count_id += 1
                else:
                    count_id = 0
                
                i+=1
            j+=1
        return count_id == self.n_rows

    def check_columns(self):
        id = self.current_player.token.id
        grill = self.grill
        i = 0
        count_id = 0
        while i < self.nb_colonnes and count_id < self.n_rows:
            j = 0
            while j < self.nb_lignes and count_id < self.n_rows:
                if grill[j][i] == id:
                    count_id += 1
                else:
                    count_id = 0
                
                j+=1
            i+=1
        return count_id == self.n_rows

    def check_diagonales_right(self):
        id = self.current_player.token.id
        grill = self.grill
        j = 0
        four_in_a_row = False
        while j < self.nb_lignes and four_in_a_row == False:
            i = 0
            while i < self.nb_colonnes and j + self.n_rows - 1 < self.nb_lignes and i + self.n_rows - 1 < self.nb_colonnes and four_in_a_row == False:
                k = 0
                four_in_a_row = True
                while k < self.n_rows and four_in_a_row:
                    if grill[j + k][i + k] != id:
                        four_in_a_row = False
                    k+=1
                i += 1
            j += 1
        return four_in_a_row

    def check_diagonales_left(self):
        id = self.current_player.token.id
        grill = self.grill
        j = 0
        four_in_a_row = False
        while j < self.nb_lignes and four_in_a_row == False:
            i = 0 
            while i < self.nb_colonnes and j + self.n_rows - 1 < self.nb_lignes and four_in_a_row == False:
                if i - (self.n_rows - 1) >= 0:
                    k = 0
                    four_in_a_row = True
                    while k < self.n_rows:
                        if grill[j + k][i - k] != id:
                            four_in_a_row = False
                        k+=1
                i += 1
            j += 1
        return four_in_a_row

    def check_full(self):
        full = True
        grill = self.grill
        for i in range(len(grill)):
            for j in range(len(grill[0])):
                if grill[i][j] == 0:
                    full = False

        return full
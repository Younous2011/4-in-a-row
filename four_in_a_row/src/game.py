import numpy as np
from pygame import Surface
import pygame

from .conf import Conf
from .alert import Alert
from .menu import Menu
from .color import MENU_COLOR, WHITE
from .grill import Grill
from .token import Token
from .player import Player
from .position import Position
from .grill_token import GrillToken

class Game:

    def __init__(
            self,
            conf:Conf,
            player1:Player, 
            player2:Player, 
            grill_token:GrillToken, 
            grill_box:Grill,
            menu:Menu,
            screen:Surface
        ):

        self.nb_lignes = conf.nb_rows
        self.nb_colonnes = conf.nb_columns
        self.player1 = player1
        self.player2 = player2
        self.game_count_won = {
            self.player1.token.id: 0,
            self.player2.token.id: 0
        }
        self.current_player = player1
        self.grill_token = grill_token
        self.grill = np.zeros((self.nb_lignes, self.nb_colonnes), dtype=int)
        self.nb_token_column = np.zeros(self.nb_colonnes, dtype=int)
        self.grill_box = grill_box
        self.menu = menu
        self.screen = screen
        self.n_set = conf.n_set
        self.n_rows = conf.n_rows_in_a_row
        self.end = False
        self.alert = None

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
        column = Position(x, 0).get_column(self.grill_token.side, self.grill_box.translation)
        row = self.get_next_row(column)
        if row < self.nb_lignes and self.end == False and column >= 0:
            self.grill_token.add_token(self.current_player.token, row, column)
            self.add_token(self.current_player.token, column)
            self.end = self.check_grill()
            if self.end:
                self.game_count_won[self.current_player.token.id] += 1
                self.menu.score_player1.update(f"{self.player1.name} : {self.game_count_won[self.player1.token.id]}")
                self.menu.score_player2.update(f"{self.player2.name} : {self.game_count_won[self.player2.token.id]}")

            if self.game_count_won[self.current_player.token.id] == self.n_set:
                print(f"{self.current_player.name} a gagné !")
                self.alert = Alert(Position(520, 360), f"{self.current_player.name} a gagné !", 60, WHITE, MENU_COLOR, self.grill_box.side, 3, 1)
            self.swipe_player()

        action = self.menu.click()
        if action == "restart":
            self.restart()

    def check_grill(self):
        b = self.check_rows() or self.check_columns() or self.check_diagonales_left() or self.check_diagonales_right()
        return b
    
    def check_rows(self):
        id = self.current_player.token.id
        grill = self.grill
        j = 0
        count_id = 0
        print(self.nb_lignes, self.nb_colonnes)
        while j < self.nb_lignes and count_id < self.n_rows:
            i = 0
            count_id = 0
            while i < self.nb_colonnes and count_id < self.n_rows:
                if grill[j][i] == id:
                    count_id += 1
                else:
                    count_id = 0
                
                print(j, i, count_id)
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

    def update(self):
        self.screen.fill(WHITE.get())
        self.menu.update()
        self.menu.blit_in(self.screen)
        x, y = pygame.mouse.get_pos()
        x = max(x, self.grill_box.translation * self.grill_box.side + self.grill_box.side // 2)
        x = min(x, self.grill_box.side * self.nb_colonnes + self.grill_box.translation * self.grill_box.side - self.grill_box.side // 2)
        new_pos = Position(x, self.grill_token.side // 2)
        self.current_player.token.set_position(new_pos)
        self.current_player.token.blit_in(self.screen)
        self.grill_token.blit_in(self.screen)
        self.grill_box.blit_in(self.screen)
        if self.alert:
            self.alert.blit_in(self.screen)

    def restart(self):
        self.end = False
        self.grill_token.restart()
        self.grill = np.zeros((self.nb_lignes, self.nb_colonnes), dtype=int)
        self.nb_token_column = np.zeros(self.nb_colonnes, dtype=int)
        if self.alert is not None:
            self.alert = None
            self.game_count_won = {
                self.player1.token.id: 0,
                self.player2.token.id: 0
            }
            self.menu.score_player1.update(f"{self.player1.name} : {self.game_count_won[self.player1.token.id]}")
            self.menu.score_player2.update(f"{self.player2.name} : {self.game_count_won[self.player2.token.id]}")
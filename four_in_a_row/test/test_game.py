import pygame

# init pygame
pygame.init()

# import tests
import unittest

# import local
from four_in_a_row.src.game import Game
from four_in_a_row.src.player import Player
from four_in_a_row.src.token import YELLOW_TOKEN, Token
from four_in_a_row.src.position import Position
from four_in_a_row.src.circle import Circle
from four_in_a_row.src.letter import Letter
from four_in_a_row.src.color import RED_DARK, RED
from four_in_a_row.src.conf import Conf

# Create Constants
RED_RAYON = 60
RED_POSITION = Position(RED_RAYON, RED_RAYON)
RED_LARGE_CIRCLE = Circle(RED_RAYON, RED, RED_POSITION)
RED_MEDIUM_CIRCLE = Circle(int(RED_RAYON * 4 / 5), RED_DARK, RED_POSITION)
RED_LETTER = Letter(RED_POSITION, "R", 100, RED)
RED_TOKEN = Token(RED_POSITION, RED_LARGE_CIRCLE, RED_MEDIUM_CIRCLE, 1, RED_LETTER)



class TestGame(unittest.TestCase):
    def test_check_grill_first_line(self):
        conf = Conf(6, 7)
        player1 = Player(None, RED_TOKEN)
        player2 = Player(None, YELLOW_TOKEN)
        g = Game(conf, player1, player2, None, None, None, None)

        g.grill = [
            [1, 1, 1, 1, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]

        self.assertTrue(g.check_grill())
    
    def test_check_grill_second_row(self):
        conf = Conf(6, 7)
        player1 = Player(None, RED_TOKEN)
        player2 = Player(None, YELLOW_TOKEN)
        g = Game(conf, player1, player2, None, None, None, None)

        g.grill = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]

        self.assertTrue(g.check_grill())
    
    def test_check_grill_third_row(self):
        conf = Conf(6, 7)
        player1 = Player(None, RED_TOKEN)
        player2 = Player(None, YELLOW_TOKEN)
        g = Game(conf, player1, player2, None, None, None, None)

        g.grill = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1]
        ]

        self.assertTrue(g.check_grill())

    def test_check_grill_last_column(self):
        conf = Conf(6, 7)
        player1 = Player(None, RED_TOKEN)
        player2 = Player(None, YELLOW_TOKEN)
        g = Game(conf, player1, player2, None, None, None, None)

        g.grill = [
            [0, 0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]

        self.assertTrue(g.check_grill())
    
    def test_check_grill_first_column(self):
        conf = Conf(6, 7)
        player1 = Player(None, RED_TOKEN)
        player2 = Player(None, YELLOW_TOKEN)
        g = Game(conf, player1, player2, None, None, None, None)

        g.grill = [
            [1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]

        self.assertTrue(g.check_grill())

    def test_check_grill_second_column(self):
        conf = Conf(6, 7)
        player1 = Player(None, RED_TOKEN)
        player2 = Player(None, YELLOW_TOKEN)
        g = Game(conf, player1, player2, None, None, None, None)

        g.grill = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0]
        ]

        self.assertTrue(g.check_grill())

    def test_check_grill_third_column(self):
        conf = Conf(6, 7)
        player1 = Player(None, RED_TOKEN)
        player2 = Player(None, YELLOW_TOKEN)
        g = Game(conf, player1, player2, None, None, None, None)

        g.grill = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0]
        ]

        self.assertTrue(g.check_grill())

    def test_check_grill_last_column(self):
        conf = Conf(6, 7)
        conf = Conf(6, 7)
        player1 = Player(None, RED_TOKEN)
        player2 = Player(None, YELLOW_TOKEN)
        g = Game(conf, player1, player2, None, None, None, None)

        g.grill = [
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]

        self.assertTrue(g.check_grill())

    def test_check_grill_first_diagonale_left(self):
        conf = Conf(6, 7)
        player1 = Player(None, RED_TOKEN)
        player2 = Player(None, YELLOW_TOKEN)
        g = Game(conf, player1, player2, None, None, None, None)

        g.grill = [
            [1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]

        self.assertTrue(g.check_grill())

    def test_check_grill_second_diagonale_left(self):
        conf = Conf(6, 7)
        player1 = Player(None, RED_TOKEN)
        player2 = Player(None, YELLOW_TOKEN)
        g = Game(conf, player1, player2, None, None, None, None)

        g.grill = [
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]

        self.assertTrue(g.check_grill())

    def test_check_grill_first_diagonale_right(self):
        conf = Conf(6, 7)
        player1 = Player(None, RED_TOKEN)
        player2 = Player(None, YELLOW_TOKEN)
        g = Game(conf, player1, player2, None, None, None, None)

        g.grill = [
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]

        self.assertTrue(g.check_grill())

    def test_check_grill_second_diagonale_right(self):
        conf = Conf(6, 7)
        player1 = Player(None, RED_TOKEN)
        player2 = Player(None, YELLOW_TOKEN)
        g = Game(conf, player1, player2, None, None, None, None)

        g.grill = [
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]

        self.assertTrue(g.check_grill())

    def test_check_false_grill_second_row(self):
        conf = Conf(6, 7)
        player1 = Player(None, RED_TOKEN)
        player2 = Player(None, YELLOW_TOKEN)
        g = Game(conf, player1, player2, None, None, None, None)

        g.grill = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]

        self.assertFalse(g.check_grill())

    def test_check_false_grill_second_diagonale_right(self):
        conf = Conf(6, 7)
        player1 = Player(None, RED_TOKEN)
        player2 = Player(None, YELLOW_TOKEN)
        g = Game(conf, player1, player2, None, None, None, None)

        g.grill = [
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]

        self.assertFalse(g.check_grill())

    def test_check_false_grill_first_diagonale_left(self):
        conf = Conf(6, 7)
        player1 = Player(None, RED_TOKEN)
        player2 = Player(None, YELLOW_TOKEN)
        g = Game(conf, player1, player2, None, None, None, None)

        g.grill = [
            [1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]

        self.assertFalse(g.check_grill())

    def test_check_false_grill_nmp(self):
        conf = Conf(5, 8)
        player1 = Player(None, RED_TOKEN)
        player2 = Player(None, YELLOW_TOKEN)
        g = Game(conf, player1, player2, None, None, None, None)

        g.grill = [
            [2, 1, 1, 1, 2, 1, 1, 1],
            [1, 1, 2, 0, 0, 0, 0, 0],
            [2, 2, 2, 0, 0, 0, 0, 0],
            [2, 2, 0, 0, 0, 0, 0, 0],
            [2, 1, 0, 0, 0, 0, 0, 0]
        ]
        print("errrrrror")
        print(g.check_rows())
        self.assertFalse(g.check_grill())

    def test_check_grill_first_row_change_n_row(self):
        conf = Conf(3, 4)
        player1 = Player(None, RED_TOKEN)
        player2 = Player(None, YELLOW_TOKEN)
        g = Game(conf, player1, player2, None, None, None, None)

        g.grill = [
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        self.assertTrue(g.check_grill())

    def test_check_full_true(self):
        conf = Conf(3, 4)
        player1 = Player(None, RED_TOKEN)
        player2 = Player(None, YELLOW_TOKEN)
        g = Game(conf, player1, player2, None, None, None, None)

        g.grill = [
            [1, 2, 1, 1],
            [1, 1, 1, 2],
            [2, 2, 2, 2]
        ]

        self.assertTrue(g.check_full())

    def test_check_full_false(self):
        conf = Conf(3, 4)
        player1 = Player(None, RED_TOKEN)
        player2 = Player(None, YELLOW_TOKEN)
        g = Game(conf, player1, player2, None, None, None, None)

        g.grill = [
            [1, 2, 1, 1],
            [1, 1, 0, 2],
            [2, 2, 2, 2]
        ]

        self.assertFalse(g.check_full())
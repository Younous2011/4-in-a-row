import unittest
from four_in_a_row.src.position import Position

class TestPosition(unittest.TestCase):

    def test_get_column_1(self):
        p = Position(10, 0)
        column = p.get_column(100, 0)
        self.assertEqual(column, 0)

    def test_get_column_2(self):
        p = Position(115, 0)
        column = p.get_column(100, 0)
        self.assertEqual(column, 1)

    def test_get_column_3(self):
        p = Position(620, 5)
        column = p.get_column(100, 0)
        self.assertEqual(column, 6)
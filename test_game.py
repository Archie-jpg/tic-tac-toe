import unittest
import pytest
from tic_tac_toe import Game, Result, Board

class TestCheckWinner(unittest.TestCase):
    def test_winning_row(self):
        """Check that if there is three in a row in a row, a winner is detected"""
        for row in range(3):
            board: Board = Board()
            board.grid[row] = ["O","O","O"]
            self.assertEqual(board.get_current_result("O"), Result.WIN)
            
    def test_winning_column(self):
        """If there is a three in a row in a column, a winner is detected"""
        for col in range(3):
            board: Board = Board()
            for row in range(3):
                board.grid[row][col] = "O"
            self.assertEqual(board.get_current_result("O"), Result.WIN)
            
    def test_winning_forward_diagonal(self):
        """If there is a three in a row in the forward diagonal, a winner is detected"""
        board: Board = Board()
        board.grid = [["O"," "," "],
                    [" ","O"," "],
                    [" "," ","O"]]
        self.assertEqual(board.get_current_result("O"), Result.WIN)
        
    def test_winning_backward_diagonal(self):
        """If there is a three in a row in the backward diagonal, a winnder is detected"""
        board: Board = Board()
        board.grid = [[" "," ","O"],
                    [" ","O"," "],
                    ["O"," "," "]]
        self.assertEqual(board.get_current_result("O"), Result.WIN)
        
    def test_draw(self):
        """If all spots are filled, a result of draw is returned"""
        board: Board = Board()
        board.grid = [["O","X","O"],
                    ["O","X","X"],
                    ["X","O","O"]]
        self.assertEqual(board.get_current_result("O"), Result.DRAW)
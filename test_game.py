import unittest
import pytest
from tic_tac_toe import Game

class TestCheckWinner(unittest.TestCase):
    def test_winning_row(self):
        """Check that if there is three in a row in a row, a winner is detected"""
        for row in range(3):
            game: Game = Game()
            game.grid[row] = ["O","O","O"]
            self.assertTrue(game.check_winner())
            
    def test_winning_column(self):
        """If there is a three in a row in a column, a winner is detected"""
        for col in range(3):
            game: Game = Game()
            for row in range(3):
                game.grid[row][col] = "O"
            self.assertTrue(game.check_winner())
            
    def test_winning_forward_diagonal(self):
        """If there is a three in a row in the forward diagonal, a winner is detected"""
        game = Game()
        game.grid = [["O"," "," "],
                    [" ","O"," "],
                    [" "," ","O"]]
        self.assertTrue(game.check_winner())
        
    def test_winning_backward_diagonal(self):
        """If there is a three in a row in the backward diagonal, a winnder is detected"""
        game = Game()
        game.grid = [[" "," ","O"],
                    [" ","O"," "],
                    ["O"," "," "]]
        self.assertTrue(game.check_winner())
from enum import Enum
from typing import NoReturn

class Result(Enum):
    UNFINISHED = "Unfinished"
    WIN = "Win"
    DRAW = "Draw"
    
class Board():
    grid: tuple[tuple]
    
    def __init__(self):
        self.grid = [[" "," "," "],
                    [" "," "," "],
                    [" "," "," "]]
        
    def valid_spot(self, row: int, col: int) -> NoReturn:
        """Check that the place the X or O is to be placed is on the grid and not taken

        Args:
            row (int): Row to put marker on, must be between 0 and 2
            col (int): Column to put marker on, must be between 0 and 2
            
        Raises:
            ValueError: If the spot chosen is either not on the grid or already taken
        """
        if row > 2 or row < 0:
            raise ValueError("Row chosen must be within grid")
        elif col > 2 or col < 0:
            raise ValueError("Col chosen must be within grid")
        elif self.grid[row][col] != " ":
            raise ValueError("This spot has already been taken")

    def place_marker(self, symbol: str, row: int, col: int) -> bool:
        """Takes in a row and column, and places a marker at that spot if possible. Prints out an error message if it was not possible

        Args:
            symbol (str): Symbol to be placed on the board
            row (int): Row to place marker in the grid
            col (int): Column to place marker in the grid

        Returns:
            bool: Returns True if the marker was placed, otherwise returns False
        """
        try:
            self.valid_spot(row=row, col=col)
            self.grid[row][col] = symbol
            return True
        except ValueError as e:
            print(e)
            return False
        
    def check_row(self, symbol: str, row: int) -> bool:
        """Checks whether or not there is a three in a row in the given row

        Args:
            row (int): Index of row to check

        Returns:
            bool: True if there is three in a row, false otherwise
        """
        for col in range(3):
            if self.grid[row][col] != symbol:
                return False
        return True
    
    def check_column(self, symbol: str, col: int) -> bool:
        """Checks if there is three in a row in the given column
        
        Args:
            col (int): Index of the column to check
            
        Returns:
            bool: True if there is three in a row, false otherwise"""
        for row in range(3):
            if self.grid[row][col] != symbol:
                return False
        return True
    
    def check_forward_diagonal(self, symbol: str, start_row: int, start_col: int) -> bool:
        """Checks if there is three in a row along a forward diagonal

        Args:
            start_row (int): Index of row of top diagonal square
            start_col (int): Index of column of top diagonal square
        """
        for i in range(3):
            if self.grid[start_row+i][start_col+i] != symbol:
                return False
        return True
    
    def check_backward_diagonal(self, symbol: str, start_row: int, start_col: int) -> bool:
            """Checks if there is three in a row along a backward diagonal
    
            Args:
                start_row (int): Index of row of top diagonal square
                start_col (int): Index of column of top diagonal square
            """
            for i in range(3):
                if self.grid[start_row+i][start_col-i] != symbol:
                    return False
            return True
        
    def grid_full(self) -> bool:
        """Checks if all avalible squares have been filled, meaning there is no winner

        Returns:
            bool: True if all sqaures contain a marker, false otherwise
        """
        pass
                            
    def check_for_winner(self, symbol: str) -> Result:
        """Checks if the symbol given has managed to get three in a row

        Returns:
            bool: True if the there is 3 in a row, col or a diagonal of the given symbol, false otherwise
        """
        # check rows and columns for a win
        for i in range(3):
            if self.check_row(symbol, i):
                return Result.WIN
            if self.check_column(symbol, i):
                return Result.WIN
        # Check diagonals
        if self.check_forward_diagonal(symbol, 0, 0):
            return Result.WIN
        elif self.check_backward_diagonal(symbol, 0,2):
            return Result.WIN
        if self.grid_full():
            return Result.DRAW
        return Result.UNFINISHED


class Game():
    go: str
    board: Board
    
    def __init__(self):
        self.go = "O"
        self.board = Board()

    def display_grid(self):
        """Uses print statements to display the current state of the grid"""
        print(" " * 4, end="")
        for i in range(3):
            print(f"{i}", end=" " * 3)
        print()
        for row in range(3):
            print(f"{row}", end=" | ")
            for col in range(3):
                print(f"{self.grid[row][col]}", end=" | ")
            print()
            print("-" * 15)
            
    def get_grid_ref(self, grid_ref: str) -> tuple[int, int]:
        """Check that the grid reference is valid, returning the row and column if it is

        Args:
            grid_ref (str): Two numbers that are the requested row and column

        Returns:
            tuple[int, int]: Returns the row and column of the grid reference
            
        Raises:
            ValueError: Occurs if the grid reference is not valid
        """
        if len(grid_ref) != 2:
            raise ValueError("Grid ref should be two didgits")
        elif not grid_ref[0].isnumeric() or not grid_ref[1].isnumeric():
            raise ValueError("Grid ref should be made up of two numbers")
        else:
            return (int(grid_ref[0]), int(grid_ref[1]))
        
    def swap_go(self) -> NoReturn:
        """Switchs who's go it currently is (if go is X, swap to O, otherwise swap to X)"""
        if self.go == "X":
            self.go = "O"
        else:
            self.go = "X"
            
    def play_turn(self) -> str:
        """Get current players input on where to place their marker until they choose a valid space

        Returns:
            str: If a the current player wins, returns their symbol
                otherwise, returns ""
        """
        marker_placed = False
        print(f"{self.go}'s turn")
        self.display_grid()
        print("Where would you like to place your marker?")
        while not marker_placed:
            grid_ref = input(": ")
            try:
                col, row = self.get_grid_ref(grid_ref)
                marker_placed = self.board.place_marker(self.go, row, col)
            except ValueError as e:
                print(e)
        result = self.board.check_for_winner(self.go)
        if result == Result.WIN:
            return f"{self.go} WINS!"
        elif result == Result.DRAW:
            return f"DRAW!"
        else:
            self.swap_go()
            return ""
        

class GameVsComputer(Game):
    def computer_turn(self):
        pass
        
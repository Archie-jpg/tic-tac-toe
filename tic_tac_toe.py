from typing import NoReturn

class Game():
    grid = [[" "," "," "],
            [" "," "," "],
            [" "," "," "]]
    go = "O"

    def print_grid(self):
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
            
    def valid_spot(self, row: int, col: int) -> str:
        """Check that the place the X or O is to be placed is on the grid and not taken

        Args:
            row (int): Row to put marker on, must be between 0 and 2
            col (int): Column to put marker on, must be between 0 and 2
        
        Returns:
            str: "" if the spot is valid, otherwise contains the reason why the marker cannot be placed there
        """
        if row > 2 or row < 0:
            return "Row chosen must be within grid"
        elif col > 2 or col < 0:
            return "Col chosen must be within grid"
        elif self.grid[row][col] != " ":
            return "This spot has already been taken"
        else:
            return ""
        
    def swap_go(self) -> NoReturn:
        """Switchs who's go it currently is (if go is X, swap to O, otherwise swap to X)"""
        if self.go == "X":
            self.go = "O"
        else:
            self.go = "X"
            
    def place_marker(self, row: int, col: int) -> bool:
        """Checks that marker can be placed in grid reference given, placing it there if it can and changing the go to the other player

        Args:
            row (int): Row to place marker in the grid
            col (int): Column to place marker in the grid

        Returns:
            bool: Returns True if the marker was placed, otherwise returns False
        """
        error = self.valid_spot()
        if error != "":
            print(error)
            return False
        else:
            self.grid[row][col] = self.go
            self.swap_go()
            return True
        
    def play_turn(self) -> NoReturn:
        """Get current players input on where to place their marker until they choose a valid space

        Returns:
            NoReturn: _description_
        """
        
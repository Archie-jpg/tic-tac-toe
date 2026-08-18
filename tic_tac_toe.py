from typing import NoReturn

class Game():
    grid = [[" "," "," "],
            [" "," "," "],
            [" "," "," "]]
    go = "O"

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
        
        
    def swap_go(self) -> NoReturn:
        """Switchs who's go it currently is (if go is X, swap to O, otherwise swap to X)"""
        if self.go == "X":
            self.go = "O"
        else:
            self.go = "X"
            
    def place_marker(self, grid_ref: str) -> bool:
        """Takes the grid ref and places a marker at that spot if possible. Prints out an error message if it was not possible

        Args:
            row (int): Row to place marker in the grid
            col (int): Column to place marker in the grid

        Returns:
            bool: Returns True if the marker was placed, otherwise returns False
        """
        try:
            col, row = self.get_grid_ref(grid_ref)
            self.valid_spot(row=row, col=col)
            self.grid[row][col] = self.go
            return True
        except ValueError as e:
            print(e)
            return False
        
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
            marker_placed = self.place_marker(grid_ref)
        if self.check_winner():
            return self.go
        else:
            self.swap_go()
            return ""
        
    def check_winner(self) -> bool:
        """Checks if the current player has managed to get three in a row

        Returns:
            bool: True if the current player has managed 3 in a row, false otherwise
        """
        # check rows
        for row in range(3):
            for col in range(3):
                if self.grid[row][col] != self.go:
                    winner = False
                    break
                else:
                    winner = True
                    continue
            if winner:
                return True
        for col in range(3):
            for row in range(3):
                if self.grid[row][col] != self.go:
                    winner = False
                    break
                else:
                    winner = True
                    continue
            if winner:
                return True
        for diagonal in range(3):
            if self.grid[diagonal][diagonal] != self.go:
                winner = False
                break
            else:
                winner = True
                continue
        if winner:
            return True
        for diagonal in range(3):
            if self.grid[diagonal][2-diagonal] != self.go:
                winner = False
                break
            else:
                winner = True
                continue
        if winner:
            return True
        return False
        
        
        
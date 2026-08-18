import sys
from tic_tac_toe import Game

def main():
    game = Game()
    game.print_grid()
    input()
    
def play_game():
    game = Game()

if __name__ == "__main__":
    sys.exit(main())
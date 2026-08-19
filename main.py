import sys
from tic_tac_toe import Game

def main():
    play_game()
    
def play_game():
    game = Game()
    result = ""
    while result == "":
        result = game.play_turn()
    game.display_grid()
    print(result)

if __name__ == "__main__":
    sys.exit(main())
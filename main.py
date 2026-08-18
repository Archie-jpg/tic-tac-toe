import sys
from tic_tac_toe import Game

def main():
    play_game()
    
def play_game():
    game = Game()
    winner = ""
    while winner == "":
        winner = game.play_turn()
    game.display_grid()
    print(f"{winner} WINS!")

if __name__ == "__main__":
    sys.exit(main())
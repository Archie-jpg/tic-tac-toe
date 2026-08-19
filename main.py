import sys
from tic_tac_toe import Game, GameVsComputer

def main():
    print("Welcome to Tic Tac Toe")
    print("Do you want to")
    print("1) Play a two player game")
    print("2) Play against the computer")
    option = input(": ")
    if option == "1":
        game: Game = Game()
    elif option == "2":
        game: Game = GameVsComputer()
    game.play_game()
    

if __name__ == "__main__":
    sys.exit(main())
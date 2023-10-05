from game import TicTacToe
import player
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


def play(game, x_player, o_player):
    game.display_state_index()

    letter = 'x'
    while game.is_empty():
        if letter == 'o':
            spot = o_player.get_move(game)
        else: 
            spot = x_player.get_move(game)

        if game.move(spot, letter):
            print(f"{letter} makes a move to spot {spot}")
            game.display_state()
            print()

            if game.current_winner:
                print(f"{letter} WONS!")
                return letter
            
            letter = 'o' if letter == 'x' else 'x'

    print("It's a TIE")


def main():
    game = TicTacToe()
    x_player = SmartComputerPlayer('x')
    o_player = SmartComputerPlayer('o')
    play(game, x_player, o_player)

if __name__ == '__main__':
    main()
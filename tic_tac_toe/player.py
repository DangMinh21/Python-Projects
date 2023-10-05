import math
import random
import time

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_spot = False
        spot = None
        while not valid_spot:
            spot = input(f"{self.letter} turn. Get a spot (0->9): ")
            try:
                spot = int(spot)
                if spot not in game.available_moves():
                    raise ValueError
                valid_spot = True
                
            except ValueError:
                print("This spot is INVALID, get another spot!")
        return spot
    
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        return random.choice(game.available_moves())

class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            return random.choice(game.available_moves())
        
        else:
            time.sleep(1)
            return self.minimax(game, self.letter)['position']
        
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'o' if player == 'x' else 'x'

        # check if previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': (state.num_empty_spots() + 1) \
                    if other_player == max_player else -(state.num_empty_spots() + 1)}
        elif not state.is_empty():
            return {'position': None, 'score': 0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            state.move(possible_move, player)
            simulate_score = self.minimax(state, other_player)

            state.state[possible_move] = ' '
            state.current_winner = None
            simulate_score['position'] = possible_move

            if player == max_player:
                if simulate_score['score'] > best['score']:
                    best = simulate_score
            else:
                if simulate_score['score'] < best['score']:
                    best = simulate_score

        return best

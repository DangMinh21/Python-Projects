class TicTacToe():
    def __init__(self):
        self.state = [' ' for _ in range(9)]
        self.current_winner = None

    def display_state(self):
        print('|---|---|---|')
        for row in [self.state[3*i : 3*i + 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
            print('|---|---|---|')

    @staticmethod
    def display_state_index():
        index = [str(i) for i in range(9)]
        print('|---|---|---|')

        for row in [index[3*i : 3*i + 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
            print('|---|---|---|')

    def move(self, index, letter):
        if self.state[index] == ' ':
            self.state[index] = letter
            if self.check_winner(index, letter):
                self.current_winner = letter
            return True
        return False

    def check_winner(self, index, letter):
        #check row
        row_idx = index // 3
        row = self.state[3*row_idx : 3 * row_idx + 3]
        if all([r == letter for r in row]):
            return True
        
        #check col
        col_idx = index % 3
        col = [self.state[3*i + col_idx] for i in range(3)]
        if all([c == letter for c in col]):
            return True
        
        # check diagonal index: [0, 4, 8], [2, 4, 6]
        if not (index % 2):
            diag_1 = [self.state[i] for i in [0, 4, 8]]
            if all([letter == d1 for d1 in diag_1]):
                return True
            
            diag_2 = [self.state[i] for i in [2, 4, 6]]
            if all([letter == d2 for d2 in diag_2]):
                return True
        return False
    
    def is_empty(self):
        return ' ' in self.state
    
    def num_empty_spots(self):
        return self.state.count(' ')
    
    def available_moves(self):
        return [int(i) for i, x in enumerate(self.state) if x == ' ']
    

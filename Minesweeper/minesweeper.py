import random

class Minesweeper:
    def __init__(self, size, no_bomb):
        self.size = size
        self.no_bomb = no_bomb
        self.board = self.init_board()
        self.dugs = set()


    def init_board(self):
        # create empty board
        board = [[' ' for _ in range(self.size)] for _ in range(self.size)]

        # set bomb location randomly
        bomb_locations = random.sample(range(self.size**2 -1), k=self.no_bomb)
        for loc in bomb_locations:
            board[loc % self.size][loc // self.size] = '*'

        # assign value to each spot that have no bomb, value is number of around neighboor that have bomb
        for r in range(self.size):
            for c in range(self.size):
                if board[r][c] == '*':
                    continue
                board[r][c] = self.assign_value(board, r, c)

        return board
    
    def assign_value(self, board, row, col):
        no_neighboor_bombs = 0
        for r in range(max(0, row-1), min(self.size-1, row+1) + 1):
            for c in range(max(0, col-1), min(self.size-1, col+1) + 1):
                if r == row and c == col:
                    continue
                if board[r][c] == '*':
                    no_neighboor_bombs += 1

        return no_neighboor_bombs

    def dig(self, x, y):
        self.dugs.add((x, y))

        # location has bomb
        if self.board[x][y] == '*': 
            return False
        
        # location's neighboors have bomb 
        elif self.board[x][y] > 0: 
            return True
        
        # location's neighboors have no bomb, continue dig around
        for r in range(max(0, x-1), min(self.size-1, x+1) + 1):
            for c in range(max(0, y-1), min(self.size-1, y+1) + 1):
                if (r, c) not in self.dugs:
                    self.dig(r, c)
        return True
        
    
    def play(self):
        # enter location
        flag = True
        while len(self.dugs) < (self.size**2 - self.no_bomb) and flag:
            self.show_current_state()
            x, y = map(int, input(f'Enter (x, y): ').split(' '))
            if x < 0 or x > self.size - 1 or y < 0 or y > self.size - 1:
                print(f"{x, y} is not valid")
                continue
            
            flag = self.dig(x, y)

        if flag:
            print("Congratuation, you Win !!!")
        else:
            print("GAME OVER, GOOD LUCK !!")
            self.show_board()

    def show_current_state(self):
        current_state = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        for (r, c) in self.dugs:
            current_state[r][c] = self.board[r][c]

        print(f"     {'   '.join([str(i) for i in range(self.size)])} ")
        print(f"  {'=' * 42}")
        for i,row in enumerate(current_state):
            str_row = [str(e) for e in row]
            print(f"{i} || {' | '.join(str_row)} |")
            print(f"  {'-' * 42}")
        

    def show_board(self):
        print(f"    {'   '.join([str(i) for i in range(self.size)])} ")
        print(f"  {'=' * 42}")
        for i, row in enumerate(self.board):
            str_row = [str(e) for e in row]
            print(f"{i} || {' | '.join(str_row)} |")
            print(f"  {'-' * 42}")



        

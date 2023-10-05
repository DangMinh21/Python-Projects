import random

class RPSGame: 

    def __init__(self) -> None:
        self.option = ('r', 'p', 's')

    def is_win(self, user_choice, computer_choice):
        if user_choice == 'r' and computer_choice == 's' or \
            user_choice == 's' and computer_choice == 'p' or\
            user_choice == 'p' and computer_choice == 'r':
            return True
        return False

    def play(self):
        # user choose
        user_choice = input("Enter your choice < rock(R), paper(P), scissors(S) > : ").lower()
        while(user_choice not in self.option):
            print('your choice is not valid')
            user_choice = input("Enter your choice < rock(R), paper(P), scissors(S) > : ").lower()

        # computer choose
        computer_choice = random.choice(['r', 'p', 's'])

        # rule for win
        if self.is_win(user_choice, computer_choice):
            print("Congraduation, You WON!")
        
        elif user_choice == computer_choice:
            print("your's TIED")
        else:
            print("You Lose, good luck!")

        
def main():
    game = RPSGame()

    flag = ''
    while flag != 'q':
        game.play()
        flag = input("Enter (q) or (Q) to out: ").lower()


if __name__ == "__main__":
    main()
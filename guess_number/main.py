import random


class GuessNumber():
    def __init__(self, lower_bound: int = -1000, upper_bound: int = 1000, maximun_guess: int = 10) -> None:        
        self.__lower_bound = lower_bound
        self.__upper_bound = upper_bound
        self.__maximun_guess = maximun_guess
        
    @property
    def lower_bound(self):
        return self.__lower_bound
    
    @lower_bound.setter
    def lower_bound(self, value):
        self.__lower_bound = value

    @property
    def upper_bound(self):
        return self.__upper_bound
    
    @upper_bound.setter
    def upper_bound(self, value):
        self.__upper_bound = value

    @property
    def maximun_guess(self):
        return self.__maximun_guess
    
    @maximun_guess.setter
    def maximun_guess(self, value):
        self.__maximun_guess = value

    def __repr__(self) -> str:
        return f"Guess game: Lower {self.lower_bound}, upper {self.upper_bound}, maximun guess {self.maximun_guess}"

    def play(self):
        # b1: randomly generate a number in range of lower bound and upper bound
        target = random.randint(self.lower_bound, self.upper_bound)

        count = 1
        # b2: user guess a number
        guess = int(input("Guess a number: "))

        while (guess != target):

            #b3: if Guess number wrong, turn back b2
            if guess < target:
                print("Your number's less than the target")
            elif guess > target:
                print("Your number's greater than the target")

            # check maximun guess, if gain maximun guess, finish
            count += 1
            if count == self.maximun_guess:
                print(f"Game OVER - target is {target}")
                break

            guess = int(input("Guess a number: "))

        #b4: if guess number equal to target, finish
        if guess == target:
            print("Congratuation, you WIN!")
            print(f"the number of guess is {count} time.")


def main():

    lower = int(input("Enter lower bound: "))
    upper = int(input("Enter upper bound: "))
    max_guess = int(input("Enter maximun of guess: "))

    assert lower <= upper, "Lower bound must less than or equal to upper bound"

    game = GuessNumber(lower, upper, max_guess)
    game.play()


if __name__ == "__main__":
    main()



import random
import string


class hangman_game:
    def __init__(self, collections) -> None:
        self.collections = collections
        self.characters = string.ascii_uppercase


    def play(self):
        target_word = list(random.choice(self.collections).upper())
        target_word_ = target_word[:]
        maximin_guess = len(target_word) + 2
        string_state = list(target_word_[0] + '_' * (len(target_word) - 1))
        target_word[0] = '-'
        guessed_letters = []

        while maximin_guess and string_state != target_word_:
            print(f"The letters you guessed {guessed_letters}")
            print(''.join(string_state))

            letter = ''
            while(True):
                letter = input(f"Remain {maximin_guess} times, Guess a letter of word: ").upper()
                if letter in self.characters:
                    break
                print("The letter is not valid, try again")

            guessed_letters.append(letter)
            
            if letter in target_word:
                idx = target_word.index(letter)
                string_state[idx] = target_word[idx]
                target_word[idx] = '_'

            maximin_guess -= 1

        if string_state == target_word_:
            print("Congraguation, you Win!")

        else:
            print("You lose, good luck!")

        print(f"Answer: --> {''.join(target_word_)}")


def main():
    with open('words.txt', 'r') as f:
        lines = f.read()
        animals = lines.split('\n')
    game = hangman_game(animals)
    game.play()
    

if __name__ == "__main__":
    main()
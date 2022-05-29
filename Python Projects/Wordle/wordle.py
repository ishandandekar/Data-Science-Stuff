import random
from rich import print
import os

with open("words.txt", "r") as f:
    words = tuple(f.readlines())


class wordle:
    def __init__(self) -> None:
        self.word = random.choice(words)[:-2]
        self.num_guesses = 0
        self.guess_dict = {
            0: [" "]*5,
            1: [" "]*5,
            2: [" "]*5,
            3: [" "]*5,
            4: [" "]*5,
            5: [" "]*5
        }

    def print_board(self):
        os.system("cls")
        for guess in self.guess_dict.values():
            print(" | ".join(guess))
            print("==============")

    def user_inp(self):
        user_input = input("Enter a 5 letter word: ")
        while len(user_input) != 5:
            user_input = input("Not valid! Enter a 5 letter word: ")
        user_input = user_input.lower()

        for index, ch in enumerate(user_input):
            if ch in self.word:
                if ch == self.word[index]:
                    ch = f"[green]{ch}[/]"  # green
                else:
                    ch = f"[yellow]{ch}[/]"  # yellow
            self.guess_dict[self.num_guesses][index] = ch

        self.num_guesses += 1
        return user_input

    def play(self):
        while True:
            self.print_board()
            user_guess = self.user_inp()
            if user_guess == self.word:
                self.print_board()
                print(f"You won !!!\nThe word was {self.word}")
                break

            if self.num_guesses > 5:
                self.print_board()
                print(f"You lost! :,(\nThe word was {self.word}")
                break


def main():
    game = wordle()
    game.play()


if __name__ == '__main__':
    main()

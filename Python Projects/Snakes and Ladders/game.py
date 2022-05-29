import random
import os
import time
import sys


class Snakes_and_Ladders:
    def __init__(self):
        self.nbrs = {}
        self.vertices = self.nbrs.keys()
        for i in range(0, 100, 1):
            self._add_relation(i, i+1)
        # Ladders
        self._add_relation(1, 38)
        self._add_relation(4, 14)
        self._add_relation(9, 31)
        self._add_relation(21, 42)
        self._add_relation(28, 84)
        self._add_relation(51, 67)
        self._add_relation(72, 91)
        self._add_relation(80, 99)

        # Snakes
        self._add_relation(17, 7)
        self._add_relation(62, 19)
        self._add_relation(54, 34)
        self._add_relation(87, 36)
        self._add_relation(64, 60)
        self._add_relation(93, 73)
        self._add_relation(95, 75)
        self._add_relation(98, 79)
        os.system('cls')
        print("Hello and welcome to Snakes and Ladders")
        time.sleep(1)
        print("A very weird way to snakes and ladders on CLI right?")
        time.sleep(1)
        print("That too on game built with 'Python', I mean what a coincidence!")
        time.sleep(1)
        print("Nevermind, Let's start the game!\nHappy playing :D")
        time.sleep(1)
        self.number_of_players = int(
            input("Enter the number of players: "))
        self.player_pos = []
        for i in range(self.number_of_players):
            self.player_pos.append(0)
        print("\nLoading the game...")
        self._start_game()

    def _start_game(self):
        dice = list(range(1, 7, 1))
        printable_sentences = ["It's Player {}'s chance",
                               "It's Player {}'s turn to play"]
        os.system("cls")
        print("The game board has been set-up as shown in the image")
        from PIL import Image
        with Image.open("Template.png") as im:
            im.show()
        while 100 not in self.player_pos:
            for i in range(self.number_of_players):
                print(random.choice(printable_sentences).format(i+1))
                time.sleep(0.5)
                print("Rolling the dice...")
                number_of_jumps = random.choice(dice)
                print(f"The dice says you to move {number_of_jumps} places")
                self._move_player(
                    number_of_jumps=number_of_jumps, player_number=i+1)
                input()

    def _move_player(self, number_of_jumps, player_number):
        initial_position = self.player_pos[player_number-1]
        new_pos = initial_position+number_of_jumps
        if new_pos >= 100:
            print(
                f"Congratulations Player {player_number}!!!\nYou won the game!!!")
            sys.exit("Woohoo!!!\nSee you guys later")
        if len(self.nbrs[new_pos]) == 2:
            new_pos = list(self.nbrs[new_pos])[-1]
        self.player_pos[player_number-1] = new_pos

        if self._endgame():
            print(
                f"Congratulations Player {player_number}!!!\nYou won the game!!!")
            sys.exit("Woohoo!!!\nSee you guys later")
        else:
            print(f"Player {player_number} has been moved to {new_pos}")

    def _endgame(self):
        if 100 in self.player_pos:
            return True
        return False

    def _add_relation(self, vertex, edge):
        if vertex not in self.vertices:
            self.nbrs[vertex] = set()
            self.nbrs[vertex].add(edge)
        else:
            self.nbrs[vertex].add(edge)

    def print_edges(self, vertex):
        print(self.nbrs[vertex])


def main():
    client = Snakes_and_Ladders()


# Testing the game
if __name__ == '__main__':
    main()

# game.py
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import random
import string

class Game:
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        if not word:
            return False

        for char in word:
            if char in self.grid:
                continue
            else:
                return False
        return True

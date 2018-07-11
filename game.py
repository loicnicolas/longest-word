# game.py
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import random
import string
import requests

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
        return self.__check_dictionary(word)

    #@staticmethod
    def __check_dictionary(self, word):
        req = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        response = req.json()
        return response['found']


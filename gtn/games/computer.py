from random import randint

from .base import BaseGame
from ..constants import (
    COMPUTER_GAME,
    NUMBERS_RANGE,
)


class ComputerGame(BaseGame):
    NAME = COMPUTER_GAME

    def __init__(self):
        self.number_to_guess = randint(NUMBERS_RANGE[0], NUMBERS_RANGE[-1])

    def validate_input(self):
        try:
            # Validates that the input value is an integer and it's in the
            # allowed range,
            validated_input = int(input())
            if validated_input not in NUMBERS_RANGE:
                raise ValueError
            return validated_input
        except ValueError:
            print('Sorry, that\'s not a valid number, try again')

    def check_guess(self, guess):
        if guess < self.number_to_guess:
            print('Nope, my number is higher!')
            return False
        elif guess > self.number_to_guess:
            print('Nope, my number is lower!')
            return False
        print('Yeah! my number is {}'.format(self.number_to_guess))
        return True

    def play(self):
        print('Hello human! I am thinking of a number between {} and {}'.format(
            NUMBERS_RANGE[0], NUMBERS_RANGE[-1]
        ))
        while True:
            validated_guess = self.validate_input()
            if validated_guess is None:
                continue

            is_guess_valid = self.check_guess(validated_guess)
            if is_guess_valid:
                break

from random import randint

from .base import BaseGame
from ..constants import (
    HUMAN_GAME,
    NUMBERS_RANGE,
    LOWER,
    HIGHER,
    VALID_HUMAN_GAME_INPUTS,
)
from ..exceptions import LieException


class HumanGame(BaseGame):
    NAME = HUMAN_GAME

    def __init__(self):
        self.highest_number = NUMBERS_RANGE[-1]
        self.lowest_number = NUMBERS_RANGE[0]

    def _check_stored_limits(self):
        """Verifies that the stored limits are in the range and
        don\'t overlap each other.
        """
        return (self.lowest_number < self.highest_number and
                self.highest_number > self.lowest_number and
                self.lowest_number in NUMBERS_RANGE and
                self.highest_number in NUMBERS_RANGE)

    def validate_input(self):
        result = input()
        # Checks if the input is an allowed value.
        if result in VALID_HUMAN_GAME_INPUTS:
            return result
        print('Sorry, that\'s not a valid input, valid inputs are: {}'.format(
            ', '.join(VALID_HUMAN_GAME_INPUTS)
        ))

    def check_guess(self, guess):
        print('Is it your number {}?'.format(guess))
        result = self.validate_input()
        if result is None:
            return False
        if result == LOWER:
            # If the result is greater than the expected, we replace the highest
            # value of the range with the given guess (without including it).
            self.highest_number = guess - 1
            return False
        elif result == HIGHER:
            # If the result is lower than the expected, we replace the lowest
            # value of the range with the given guess (without including it).
            self.lowest_number = guess + 1
            return False
        print('Yeah! Your number is {}'.format(guess))
        return True

    def play(self):
        print('Hello human! I\'ll try to guess your number between {} and {}'.format(
            NUMBERS_RANGE[0], NUMBERS_RANGE[-1]
        ))
        while True:
            if not self._check_stored_limits():
                # If the user lies with his number, the game ends.
                raise LieException('Did you lie to me??? I\'m very disappointed...')
            guess = randint(self.lowest_number, self.highest_number)
            guessed = self.check_guess(guess)
            if guessed:
                # If the user guess the number, the game ends.
                return

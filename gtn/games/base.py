from abc import (
    ABCMeta,
    abstractmethod,
)


class BaseGame(object):
    """Base abstract class for Guess The Number game."""

    __metaclass__ = ABCMeta

    NAME = None

    @classmethod
    def check_game_name(cls, name):
        """Checks if the given name match with the NAME of the Game class.

        Args:
            name (str): Game's name

        Returns:
            (bool): Name matches with Game's name.
        """
        return cls.NAME == name

    @abstractmethod
    def validate_input(self):
        """Sanitizes input from the user.

        Returns:
            (object|None): Returns the input value if it pass the validation,
            otherwise returns None.
        """
        pass

    @abstractmethod
    def check_guess(self, guess):
        """Checks if the guess number match with the selected number.

        Args:
            guess (int): Assumption about the selected number.

        Returns:
            (bool): Returns True if the guess was correct, otherwise returns False.
        """
        pass

    @abstractmethod
    def play(self):
        """Starts the game.

        Iterates in a while clause until the guess matches with the selected number.
        """
        pass

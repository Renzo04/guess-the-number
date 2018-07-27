from .computer import ComputerGame
from .human import HumanGame


GAMES = [ComputerGame, HumanGame]


def get_guess_game(name):
    """Retrieves a Game instance if the provided name match.

    Args:
        name (str): Game's name

    Returns:
        (ComputerGame|HumanGame|None): If the name matches with some
        Game's variation, returns that Game's instance, otherwise returns
        None.
    """
    for game in GAMES:
        if game.check_game_name(name):
            return game()

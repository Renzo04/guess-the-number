from unittest.mock import patch

from gtn.games import get_guess_game
from gtn.constants import (
    COMPUTER_GAME,
    NUMBERS_RANGE,
)


GAME = get_guess_game(COMPUTER_GAME)


def test_check_correct_guess():
    selected_number = GAME.number_to_guess
    assert GAME.check_guess(selected_number) is True


def test_check_wrong_guess():
    selected_number = GAME.number_to_guess
    wrong_numbers = [number for number in NUMBERS_RANGE if number != selected_number]
    for wrong_guess in wrong_numbers:
        assert GAME.check_guess(wrong_guess) is False


@patch('builtins.input')
def test_validate_correct_input(mock_input):
    mock_input.return_value = NUMBERS_RANGE[-1]

    assert GAME.validate_input() == NUMBERS_RANGE[-1]


@patch('builtins.input', return_value='wronginput')
def test_validate_not_integer_input(mock_input):
    assert GAME.validate_input() is None


@patch('builtins.input')
def test_validate_integer_not_in_range_input(mock_input):
    mock_input.return_value = NUMBERS_RANGE[-1] + 2

    assert GAME.validate_input() is None


@patch('gtn.games.computer.randint')
@patch('builtins.input')
def test_play_with_happy_ending(mock_input, randint_mock):
    randint_mock.return_value = 20
    guesses = [
        15,
        50,
        30,
        25,
        'wrongvalue',
        22,
        20,
    ]

    mock_input.side_effect = guesses
    GAME = get_guess_game(COMPUTER_GAME)

    assert GAME.play() is None

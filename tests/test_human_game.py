from unittest.mock import patch

import pytest

from gtn.constants import (
    HUMAN_GAME,
    NUMBERS_RANGE,
    MATCH,
    HIGHER,
    LOWER,
    VALID_HUMAN_GAME_INPUTS,
)
from gtn.exceptions import LieException
from gtn.games import get_guess_game


@patch('builtins.input', return_value=MATCH)
def test_check_correct_guess(mock_input):
    GAME = get_guess_game(HUMAN_GAME)

    guess = 20

    assert GAME.check_guess(guess) is True


@patch('builtins.input', return_value=LOWER)
def test_check_high_guess(mock_input):
    GAME = get_guess_game(HUMAN_GAME)
    guess = 20

    assert GAME.check_guess(guess) is False
    assert GAME.highest_number == guess - 1
    assert GAME.lowest_number == NUMBERS_RANGE[0]


@patch('builtins.input', return_value=HIGHER)
def test_check_low_guess(mock_input):
    GAME = get_guess_game(HUMAN_GAME)
    guess = 20

    assert GAME.check_guess(guess) is False
    assert GAME.lowest_number == guess + 1
    assert GAME.highest_number == NUMBERS_RANGE[-1]


@patch('builtins.input', return_value='wronginput')
def test_check_guess_with_invalid_input(mock_input):
    GAME = get_guess_game(HUMAN_GAME)
    guess = 20

    assert GAME.check_guess(guess) is False
    assert GAME.lowest_number == NUMBERS_RANGE[0]
    assert GAME.highest_number == NUMBERS_RANGE[-1]


@patch('builtins.input')
def test_validate_correct_input(mock_input):
    GAME = get_guess_game(HUMAN_GAME)

    for valid_input in VALID_HUMAN_GAME_INPUTS:
        mock_input.return_value = valid_input
        assert GAME.validate_input() == valid_input


@patch('builtins.input', return_value='wronginput')
def test_validate_not_allowed_input(mock_input):
    GAME = get_guess_game(HUMAN_GAME)

    assert GAME.validate_input() is None


@patch('gtn.games.human.randint')
@patch('builtins.input')
def test_play_with_happy_ending(mock_input, randint_mock):
    predictions = [
        25,
        26,
        30,
    ]
    inputs = [
        HIGHER,
        HIGHER,
        MATCH,
    ]

    randint_mock.side_effect = predictions
    mock_input.side_effect = inputs

    GAME = get_guess_game(HUMAN_GAME)

    assert GAME.play() is None


@patch('gtn.games.human.randint')
@patch('builtins.input')
def test_play_with_user_lie(mock_input, randint_mock):
    predictions = [
        25,
        26,
    ]
    inputs = [
        HIGHER,
        LOWER,
    ]

    randint_mock.side_effect = predictions
    mock_input.side_effect = inputs

    GAME = get_guess_game(HUMAN_GAME)

    with pytest.raises(LieException):
        GAME.play()


@patch('gtn.games.human.randint')
@patch('builtins.input')
def test_play_with_lower_limit_out_of_range(mock_input, randint_mock):
    predictions = [
        NUMBERS_RANGE[0]
    ]
    inputs = [
        LOWER,
    ]

    randint_mock.side_effect = predictions
    mock_input.side_effect = inputs

    GAME = get_guess_game(HUMAN_GAME)

    with pytest.raises(LieException):
        GAME.play()


@patch('gtn.games.human.randint')
@patch('builtins.input')
def test_play_with_higher_limit_out_of_range(mock_input, randint_mock):
    predictions = [
        NUMBERS_RANGE[-1],
    ]
    inputs = [
        HIGHER,
    ]

    randint_mock.side_effect = predictions
    mock_input.side_effect = inputs

    GAME = get_guess_game(HUMAN_GAME)

    with pytest.raises(LieException):
        GAME.play()

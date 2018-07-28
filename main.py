from gtn.constants import HUMAN_GAME, COMPUTER_GAME
from gtn.exceptions import LieException
from gtn.games import get_guess_game


print('Welcome to Guess the Number!!')
print('First you must select your preferred game.')
print('The availables games are:')
print('\t{}) The human game, the computer will try to guess your number'.format(HUMAN_GAME))
print('\t{}) The computer game, you have to try to guess the computer\'s number'.format(COMPUTER_GAME))

while True:
    selected_game = input('Select the game that you want to play: ')

    game = get_guess_game(selected_game)
    if game is None:
        print('The option is not valid, please select a valid option.')
        continue
    break

try:
    game.play()
except LieException as e:
    print(e)
    print('You lose! You can\'t cheat!!')
else:
    print('Thanks for playing!')

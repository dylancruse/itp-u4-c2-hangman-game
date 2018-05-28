from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['Cats', 'Swimming', 'Music', 'Reddit', 'Zelda']


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException("List cannot be empty")
    return random.choice(list_of_words)


def _mask_word(word):
    pass


def _uncover_word(answer_word, masked_word, character):
    pass


def guess_letter(game, letter):
    pass


def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game

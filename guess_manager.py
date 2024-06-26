from enum import Enum
from collections import Counter

CHAR_PLACEHOLDER = "-"


class GuessResult(Enum):
    RETRY = 0
    CORRECT_NO_WIN = 1
    INCORRECT = 2
    WIN = 3


class GuessManager:

    def __init__(self, target_word):
        self.target_word = target_word
        self.chars_counter = Counter(char for char in target_word.word if char.isalpha())
        self.guessed_chars = [0] * len(range(ord('a'), ord('z') + 1))

    def player_guess(self, player, character):
        if not character.isalpha() or len(character) != 1:
            print(f"Illegal characters entered ({character}), please try again\n")
            return GuessResult.RETRY

        guessed_char = character.lower()
        guessed_char_idx = normalize_character(guessed_char)
        if self.guessed_chars[guessed_char_idx]:
            print(f"Character ({character}) was already entered, please try again\n")
            return GuessResult.RETRY

        self.guessed_chars[guessed_char_idx] = 1
        char_count = self.chars_counter[guessed_char]
        if char_count == 0:
            return GuessResult.INCORRECT

        player.add_score(char_count)
        self.chars_counter[guessed_char] = 0

        if any(value > 0 for value in self.chars_counter.values()):
            return GuessResult.CORRECT_NO_WIN

        return GuessResult.WIN

    def get_word_printed(self):
        guessed_word = ''
        for char in self.target_word.word:
            if char.isspace() or self.guessed_chars[normalize_character(char)]:
                guessed_word += char
            else:
                guessed_word += CHAR_PLACEHOLDER
        return guessed_word

    def get_guessed_characters(self):
        list_guessed = []
        for char_index, was_guessed in enumerate(self.guessed_chars):
            if was_guessed:
                list_guessed.append(chr(ord('a') + char_index))
        return ', '.join(list_guessed)


def normalize_character(char):
    return ord(char) - ord('a')

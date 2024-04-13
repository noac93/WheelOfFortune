import json
import random

from gameword import GameWord

DEFAULT_WORDS_NUM = 10


class WordGenerator:

    def __init__(self, words_file, words_num=DEFAULT_WORDS_NUM):
        self.wordList = import_num_words_from_file(words_file, words_num)
        self.remainingWords = self.wordList

    def get_word(self):
        if not self.remainingWords:
            return None
        word = random.choice(self.wordList)
        self.remainingWords.remove(word)
        return word


def import_num_words_from_file(words_file, num_words):
    try:
        with open(words_file) as fd:
            file_data = json.load(fd)
            word_entries = file_data["words"]
            words = [GameWord(entry["word"].lower(), entry["category"]) for entry in get_random_words(word_entries, num_words)]
            return words
    except FileNotFoundError:
        print("Words file doesn't exist")
        raise


def get_random_words(all_words, num_words):
    if len(all_words) == num_words:
        return all_words
    random.shuffle(all_words)
    return all_words[:num_words]
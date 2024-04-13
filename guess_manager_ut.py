import pytest
from guess_manager import GuessManager, GuessResult
from gameword import GameWord
from player import Player


class TestGuessManager:

    @pytest.fixture
    def setup(self):
        target_word = GameWord(word='example', category='UTs')
        player = Player(name='Player1')
        return GuessManager(target_word), player

    def test_player_guess_correct(self, setup):
        guess_manager_instance, player = setup
        assert guess_manager_instance.player_guess(player=player, character='e') == GuessResult.CORRECT_NO_WIN

    def test_player_guess_incorrect(self, setup):
        guess_manager_instance, player = setup
        assert guess_manager_instance.player_guess(player=player, character='z') == GuessResult.INCORRECT

    def test_player_guess_retry(self, setup):
        guess_manager_instance, player = setup
        guess_manager_instance.guessed_chars = [1] * 26
        assert guess_manager_instance.player_guess(player=player, character='a') == GuessResult.RETRY

    def test_get_word_printed(self, setup):
        guess_manager_instance, player = setup
        guess_manager_instance.guessed_chars = [0] * 26
        assert guess_manager_instance.get_word_printed() == "-------"

    def test_get_guessed_characters(self, setup):
        guess_manager_instance, player = setup
        guess_manager_instance.guessed_chars = [1] * 26
        assert guess_manager_instance.get_guessed_characters() == 'a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z'

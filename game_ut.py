import pytest
from game import Game


class TestGame:

    @pytest.fixture
    def game(self):
        return Game('words.json', num_words=10, player_names=['Player1', 'Player2'])

    def test_game_initialization(self, game):
        assert game.wordGenerator is not None
        assert len(game.players) == 2
        assert game.numPlayers == 2

    def test_get_winning_players(self, game):
        game.players[0].score = 10
        game.players[1].score = 5
        assert game.get_winning_players() == ['Player1']

    def test_print_game_over(self, game, capsys):
        game.print_game_over()
        captured = capsys.readouterr()
        assert "Game Over" in captured.out

    def test_print_winners(self, game, capsys):
        game.players[0].score = 10
        game.players[1].score = 5
        game.print_winners()
        captured = capsys.readouterr()
        assert "Winning Player: Player1" in captured.out

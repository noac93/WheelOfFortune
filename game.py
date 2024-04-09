import guess_manager
from player import Player
from word_generator import WordGenerator

default_player_names = ['Player1', 'Player2', 'Player3']


class Game:

    def __init__(self, words_file, num_words=-1, player_names=None):
        if player_names is None:
            player_names = default_player_names
        self.wordGenerator = WordGenerator(words_file, int(num_words))
        self.players = [Player(playerName) for playerName in player_names]
        self.numPlayers = len(self.players)

    def play_game(self):
        player_index = 0
        while True:
            target_word = self.wordGenerator.get_word()
            if not target_word:
                self.print_game_over()
                return
            print("##################################")
            print(f'Category: {target_word.category}')
            guess_manager_instance = guess_manager.GuessManager(target_word)
            print_word_on_board(guess_manager_instance)
            while True:
                guess_result = self.handle_turn(guess_manager_instance, player_index)
                print_word_on_board(guess_manager_instance)
                self.print_scores()
                if guess_result == guess_manager.GuessResult.WIN:
                    break
                elif guess_result == guess_manager.GuessResult.INCORRECT:
                    player_index = (player_index + 1) % self.numPlayers

    def handle_turn(self, guess_manager_instance, player_index):
        user_guess = input(f"{self.players[player_index].name}, enter your guess: ")
        return guess_manager_instance.player_guess(player=self.players[player_index], character=user_guess)

    def print_scores(self):
        score_string = 'Scores:\n'
        for player in self.players:
            score_string += f"{player.name} | {player.score}\n"
        print(score_string)

    def print_game_over(self):
        print('\nGame Over')
        self.print_winners()

    def print_winners(self):
        self.print_scores()
        winning_players = self.get_winning_players()
        if len(winning_players) == len(self.players):
            print("RESULT: TIE")
            return
        print(f"Winning Player{'s' if len(winning_players) > 1 else ''}: {','.join(winning_players)}")

    def get_winning_players(self):
        max_score = max(self.players, key=lambda player: player.score).score
        winning_players = [player.name for player in self.players if player.score == max_score]
        return winning_players


def print_word_on_board(guess_manager_instance):
    print(f"Word: {guess_manager_instance.get_word_printed()}")
    guessed_chars = guess_manager_instance.get_guessed_characters()
    print(f"Already guessed characters: {guessed_chars}") if len(guessed_chars) > 0 else ''

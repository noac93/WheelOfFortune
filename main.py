from game import Game
import sys


def main():
    if len(sys.argv) < 2:
        print('Error: No words file path provided')
        return

    words_file = sys.argv[1]
    num_words = 10
    player_names = None

    if len(sys.argv) >= 3:
        try:
            num_words = int(sys.argv[2])
        except ValueError:
            print('Invalid number of words provided. Using default value (10).')

    if len(sys.argv) >= 4:
        player_names = sys.argv[3:]

    game = Game(words_file, num_words, player_names)
    game.play_game()


if __name__ == '__main__':
    main()



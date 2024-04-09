from game import Game
import sys


def main():
    arguments = sys.argv[1:]
    num_args = len(arguments)
    if num_args == 3:
        game = Game(arguments[0], arguments[1], arguments[2])
    if num_args == 2:
        game = Game(arguments[0], arguments[1])
    elif num_args == 1:
        game = Game(arguments[0])
    else:
        print('No words file path provided')
        return
    game.play_game()


if __name__ == '__main__':
    main()



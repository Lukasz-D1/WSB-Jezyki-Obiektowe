from controllers.controller import Controller
from argparse import ArgumentParser


def main():
    parser = ArgumentParser(description='Jezyki obietkowe - zadanie 2. Celem zadania bylo stworzenie '
                                        'symulacji automatu komorkowego "Game of Life". W kontrolerze '
                                        'zdefiniowano parametry NUM_ROWS, NUM_COLS, SIZE_OF_CELL '
                                        'oznaczajace kolejno liczbe wierszy, liczbe kolumn oraz wielkosc komorki '
                                        'uzywanej w grze. Zaleca sie modyfikowac te wartosci aby uzyskac '
                                        'mniejsza/wieksza plansze z uwzglednieniem warunku, '
                                        'ze okno gry ma wielkosc 500x500 px. Domyslnie ustawiono 50|50|10.')
    parser.add_argument('--entry_point',
                        dest='entry_point',
                        type=str,
                        choices=['glider', 'random'],
                        default='random',
                        help='Ustaw glider jesli chcesz sprawdzic dzialanie typowego glidera z gry w zycie.'
                             ' Domyslnie random.')

    args = parser.parse_args()
    entry_point = args.entry_point  # glider | random

    cnt = Controller()
    cnt.app(entry_point)


if __name__ == '__main__':
    main()

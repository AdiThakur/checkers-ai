from sys import argv
from typing import *


def main() -> None:
    pass


if __name__ == "__main__":

    if len(argv) != 3:
        print("Usage: python3 checkers.py <input_file> <output_file>")
        exit()

    main(
        input_filename=argv[1],
        output_filename=argv[2],
    )

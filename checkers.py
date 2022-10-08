from sys import argv
from typing import *


Grid = List[List[int]]
Cord = Tuple[int, int]


class State:

    id: str
    grid: Grid
    parent: Optional['State']

    def __init__(self, grid: Grid, parent: Optional['State'] = None) -> None:
        self.grid = grid
        self.parent = parent
        self._generate_id()

    def get_successors(self) -> List['State']:
        pass

    def _generate_id(self) -> None:
        self.id = ""
        for row in self.grid:
            for col in row:
                self.id += col


def generate_grid(filename: str)-> Grid:

    grid = []

    with open(filename) as input_file:
        for row in input_file.readlines():
            grid.append([char for char in row.strip()])

    return grid


def main(input_filename: str, output_filename:str) -> None:
    board = generate_grid(input_filename)


if __name__ == "__main__":

    if len(argv) != 3:
        print("Usage: python3 checkers.py <input_file> <output_file>")
        exit()

    main(
        input_filename=argv[1],
        output_filename=argv[2],
    )

from copy import deepcopy
from sys import argv
from typing import *


DIM = 8
EMPTY = '.'
MAX = 'r'
MIN = 'b'


Grid = List[List[str]]
Coord = Tuple[int, int]

# Assuming that our AI (red player) starts from bottom of board, and enemy AI (black player) starts from top


class State:

    id: str
    grid: Grid
    is_max_turn: bool

    def __init__(self, grid: Grid, is_max_turn: bool) -> None:
        self.grid = grid
        self.is_max_turn = is_max_turn
        self._generate_id()

    def get_successors(self) -> List['State']:

        if self.is_max_turn:
            color = 'r'
            move_direction = -1
        else:
            color = 'b'
            move_direction = 1

        for row in range(self.grid):
            for col in range(self.grid[row]):

                piece = self.grid[row][col]

                if piece.lower() != color:
                    continue
                # if piece == color:
                    # self.get_moves((row, col), move_direction, [1])
                # King
                # else:
                    # self.get_moves((row, col), move_direction, [-1, 1])

    def _jump_move(self, grid: Grid, pos: Coord, depth: int = 0) -> List[Grid]:

        row, col = pos
        piece_to_move = grid[row][col]
        row_deltas = self._get_row_deltas(piece_to_move)

        moves = []

        for row_delta in row_deltas:
            for col_delta in [-1, 1]:

                n_row = row + row_delta
                n_col = col + col_delta

                if n_row not in range(DIM) or n_col not in range(DIM):
                    continue
                if grid[n_row][n_col] == EMPTY:
                    continue
                if grid[n_row][n_col] == piece_to_move:
                    continue

                # Jump opportunity
                jump_row = pos[0] + (2 * row_delta)
                jump_col = pos[1] + (2 * col_delta)

                if jump_row not in range(DIM) or jump_col not in range(DIM):
                    continue
                if grid[jump_row][jump_col] != EMPTY:
                    continue

                # Jump can be made
                new_move = self._swap_pieces(grid, pos, (jump_row, jump_col))
                new_move[n_row][n_col] = EMPTY
                moves += self._jump_move(new_move, (jump_row, jump_col), depth + 1)

        if len(moves):
            return moves
        if depth > 0:
            return [grid]
        return []

    def _get_row_deltas(self, piece: str) -> List[int]:
        if piece == MAX:
            return [-1]
        elif piece == MIN:
            return [1]
        else:
            return [-1, 1]

    def _swap_pieces(self, grid: Grid, old_pos: Coord, new_pos: Coord) -> Grid:

        copied_grid = deepcopy(grid)
        copied_grid[new_pos[0]][new_pos[1]] = grid[old_pos[0]][old_pos[1]]
        copied_grid[old_pos[0]][old_pos[1]] = EMPTY

        return copied_grid

    def _generate_id(self) -> None:
        self.id = ""
        for row in self.grid:
            for col in row:
                self.id += col


def basic_utility(state: State) -> int:

    max_count = 0
    min_count = 0

    for row in state.grid:
        for piece in row:
            if piece.lower() == MAX:
                max_count += 1
                if piece.isupper():
                    max_count += 1
            elif piece.lower() == MIN:
                min_count += 1
                if piece.isupper():
                    min_count += 1

    return (max_count - min_count)


def generate_grid(filename: str) -> Grid:

    grid = []

    with open(filename) as input_file:
        for row in input_file.readlines():
            grid.append([char for char in row.strip()])

    return grid


def main(input_filename: str, output_filename: str) -> None:
    initial_grid = generate_grid(input_filename)
    initial_state = State(initial_grid, True)


if __name__ == "__main__":

    if len(argv) != 3:
        print("Usage: python3 checkers.py <input_file> <output_file>")
        exit()

    main(
        input_filename=argv[1],
        output_filename=argv[2],
    )

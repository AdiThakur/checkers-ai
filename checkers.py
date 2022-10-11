from copy import deepcopy
from math import inf
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
    piece_color: str
    grid: Grid
    is_max_turn: bool

    def __init__(self, grid: Grid, is_max_turn: bool) -> None:
        self.grid = grid
        self.is_max_turn = is_max_turn
        self._generate_id()
        if self.is_max_turn:
            self.piece_color = MAX
        else:
            self.piece_color = MIN

    def get_successors(self) -> List[Grid]:

        normal_moves = []
        jump_moves = []

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):

                if self.grid[row][col].lower() != self.piece_color:
                    continue

                jump_moves.extend(self._jump_move(self.grid, (row, col)))

                # Mandatory Captures; if a capture can be performed, no point in
                # exploring non-capture moves
                if len(jump_moves) == 0:
                    normal_moves.extend(self._normal_move(self.grid, (row, col)))

        if len(jump_moves):
            return jump_moves
        else:
            return normal_moves

    def get_piece_count(self) -> Tuple[int, int]:

        max_count = 0
        min_count = 0

        for row in self.grid:
            for piece in row:
                if piece.lower() == MAX:
                    max_count += 1
                elif piece.lower() == MIN:
                    min_count += 1

        return (max_count, min_count)

    def _normal_move(self, grid: Grid, pos: Coord) -> List[Grid]:

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
                    new_move = self._swap_pieces_on_copy(grid, pos, (n_row, n_col))
                    moves.append(new_move)

        return moves

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
                new_move = self._swap_pieces_on_copy(grid, pos, (jump_row, jump_col))
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

    def _swap_pieces_on_copy(self, grid: Grid, old_pos: Coord, new_pos: Coord) -> Grid:

        copied_grid = deepcopy(grid)
        copied_grid[new_pos[0]][new_pos[1]] = grid[old_pos[0]][old_pos[1]]
        copied_grid[old_pos[0]][old_pos[1]] = EMPTY

        self._try_promotion(copied_grid, new_pos)

        return copied_grid

    def _try_promotion(self, grid: Grid, pos: Coord) -> None:

        row, col = pos
        piece = grid[row][col]

        if piece == MIN and row == DIM - 1:
            grid[row][col] = MIN.upper()
        if piece == MAX and row == 0:
            grid[row][col] = MAX.upper()

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


def is_game_over(state: State) -> bool:
    max_pieces, min_pieces = state.get_piece_count()
    return max_pieces == 0 or min_pieces == 0

def df_minimax(curr_state: State, depth_limit: int) -> Tuple[int, State]:

    best_move: Optional[State] = None
    best_util = -inf if curr_state.is_max_turn else inf
    curr_util = basic_utility(curr_state)

    if depth_limit == 0 or is_game_over(curr_state):
        return curr_util, best_move

    successors = curr_state.get_successors()

    if len(successors) == 0:
        return curr_util, best_move

    for successor in successors:

        s_state = State(successor, not (curr_state.is_max_turn))
        s_util, _ = df_minimax(s_state, depth_limit - 1)

        if curr_state.is_max_turn:
            if s_util > best_util:
                best_util = s_util
                best_move = s_state
        else:
            if s_util < best_util:
                best_util = s_util
                best_move = s_state

    return best_util, best_move


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

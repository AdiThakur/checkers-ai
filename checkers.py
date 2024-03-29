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


class State:

    piece_color: str
    grid: Grid
    is_max_turn: bool

    def __init__(self, grid: Grid, is_max_turn: bool) -> None:
        self.grid = grid
        self.is_max_turn = is_max_turn
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
                    normal_moves.extend(self._normal_move((row, col)))

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

    def _normal_move(self, pos: Coord) -> List[Grid]:

        row, col = pos
        piece_to_move = self.grid[row][col]
        row_deltas = self._get_row_deltas(piece_to_move)

        moves = []

        for row_delta in row_deltas:
            for col_delta in [-1, 1]:

                n_row = row + row_delta
                n_col = col + col_delta

                if n_row not in range(DIM) or n_col not in range(DIM):
                    continue
                if self.grid[n_row][n_col] == EMPTY:
                    grid_after_move = self._swap_pieces_on_copy(self.grid, pos, (n_row, n_col))
                    self._try_promotion(grid_after_move, (n_row, n_col))
                    moves.append(grid_after_move)

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
                if grid[n_row][n_col].lower() == piece_to_move.lower():
                    continue

                # Jump opportunity
                jump_row = row + (2 * row_delta)
                jump_col = col + (2 * col_delta)

                if jump_row not in range(DIM) or jump_col not in range(DIM):
                    continue
                if grid[jump_row][jump_col] != EMPTY:
                    continue

                # Jump can be made
                grid_after_move = self._swap_pieces_on_copy(grid, pos, (jump_row, jump_col))
                grid_after_move[n_row][n_col] = EMPTY

                # Cannot continue jumps after promotion
                if self._try_promotion(grid_after_move, (jump_row, jump_col)):
                    moves.append(grid_after_move)
                else:
                    moves += self._jump_move(grid_after_move, (jump_row, jump_col), depth + 1)

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

        return copied_grid

    def _try_promotion(self, grid: Grid, pos: Coord) -> bool:

        row, col = pos
        piece = grid[row][col]

        if piece == MIN and row == DIM - 1:
            grid[row][col] = MIN.upper()
            return True
        if piece == MAX and row == 0:
            grid[row][col] = MAX.upper()
            return True

        return False


def basic_utility(grid: Grid) -> int:

    max_count = 0
    min_count = 0

    for row in grid:
        for piece in row:
            if piece.lower() == MAX:
                max_count += 1
                if piece.isupper():
                    max_count += 1
            elif piece.lower() == MIN:
                min_count += 1
                if piece.isupper():
                    min_count += 1

    return max_count - min_count


def get_num_safe_pieces(grid: Grid, piece: str) -> int:

    if piece == MAX:
        rows = cols = range(DIM)
    else:
        rows = cols = range(DIM - 1, -1, -1)

    num_safe_pieces = 0

    for row in rows:
        for col in cols:

            curr_piece = grid[row][col].lower()

            if curr_piece == EMPTY:
                continue
            if curr_piece != piece:
                return num_safe_pieces
            if curr_piece == piece:
                num_safe_pieces += 1

    return num_safe_pieces


def safe_pieces_heuristic(state: State):
    return get_num_safe_pieces(state.grid, MAX) - get_num_safe_pieces(state.grid, MIN)


def is_game_over(state: State) -> bool:
    max_pieces, min_pieces = state.get_piece_count()
    return max_pieces == 0 or min_pieces == 0


def alpha_beta(
    curr_state: State, alpha: int, beta: int, depth_limit: int
) -> Tuple[int, Optional[State]]:

    best_move: Optional[State] = None
    best_util = -inf if curr_state.is_max_turn else inf
    curr_util = basic_utility(curr_state.grid)

    if depth_limit == 0 or is_game_over(curr_state):
        return curr_util, best_move

    successors = curr_state.get_successors()
    successors.sort(key=basic_utility)

    if len(successors) == 0:
        return curr_util, best_move

    for successor in successors:

        s_state = State(successor, not (curr_state.is_max_turn))
        s_util, _ = alpha_beta(s_state, alpha, beta, depth_limit - 1)

        if curr_state.is_max_turn:
            if s_util > best_util:
                best_util = s_util
                best_move = s_state
            if best_util >= beta:
                return best_util, best_move
            alpha = max(best_util, alpha)
        else:
            if s_util < best_util:
                best_util = s_util
                best_move = s_state
            if best_util <= alpha:
                return best_util, best_move
            beta = min(best_util, beta)

    return best_util, best_move


def generate_grid(filename: str) -> Grid:

    grid = []

    with open(filename) as input_file:
        for row in input_file.readlines():
            grid.append([char for char in row.strip()])

    return grid


def write_best_move(filename: str, best_move: Optional[State]) -> None:

    if best_move is None:
        return

    with open(filename, mode='w') as output_file:
        for row in best_move.grid:
            row_str = ""
            for col in row:
                row_str += col
            output_file.write(row_str + "\n")


def main(input_filename: str, output_filename: str) -> None:
    initial_state = State(generate_grid(input_filename), True)
    _, best_move = alpha_beta(initial_state, -inf, inf, depth_limit=10)
    write_best_move(output_filename, best_move)


if __name__ == "__main__":

    if len(argv) != 3:
        print("Usage: python3 checkers.py <input_file> <output_file>")
        exit()

    main(
        input_filename=argv[1],
        output_filename=argv[2],
    )

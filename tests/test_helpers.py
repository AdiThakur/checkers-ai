import unittest
from checkers import *


class TestGenerateGrid(unittest.TestCase):
    def test_proper_format_generates_correct_grid(self):
        expected_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "b", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "R"],
            [".", ".", "b", ".", "b", ".", ".", "."],
            [".", ".", ".", "b", ".", ".", ".", "r"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "r", ".", ".", ".", "."],
            [".", ".", ".", ".", "B", ".", ".", "."],
        ]
        puzzle_file_name = "test_inputs/puzzle1.txt"

        result = generate_grid(puzzle_file_name)

        self.assertEqual(expected_grid, result)


class TestSafePiecesHeuristic(unittest.TestCase):
    def test_no_pieces(self):
        grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]
        state = State(grid, True)

        value = safe_pieces_heuristic(state)

        self.assertEqual(0, value)

    def test_only_max(self):
        grid = [
            [".", ".", ".", ".", ".", "R", ".", "."],
            [".", ".", "r", ".", "r", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "r"],
            [".", "r", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "r", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]
        state = State(grid, True)

        value = safe_pieces_heuristic(state)

        self.assertEqual(6, value)
    
    def test_only_min(self):
        grid = [
            [".", ".", ".", ".", ".", "B", ".", "."],
            [".", ".", "b", ".", "b", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "b"],
            [".", "b", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "b", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]
        state = State(grid, True)

        value = safe_pieces_heuristic(state)

        self.assertEqual(-6, value)

    def test_does_not_consider_kings(self):
        grid = [
            [".", ".", ".", ".", ".", "R", ".", "."],
            [".", ".", "r", ".", "r", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "b", ".", "b", ".", ".", "."],
            [".", ".", ".", "b", ".", ".", ".", "r"],
            [".", "r", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "r", ".", ".", ".", "."],
            [".", ".", "B", ".", "b", ".", ".", "."],
        ]
        state = State(grid, True)

        value = safe_pieces_heuristic(state)

        self.assertEqual(1, value)


class TestAlphaBeta(unittest.TestCase):
    def test_min_picks_lowest_util_successor_depth_1(self):
        grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "b", ".", ".", ".", "."],
            [".", ".", "R", ".", "r", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]
        expected_grid_fragment = [
            [".", "b", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]

        initial_state = State(grid, False)
        best_util, best_move = alpha_beta(initial_state, -inf, inf, depth_limit=2)

        self.assertEqual(0, best_util)
        self.assertEqual(expected_grid_fragment, best_move.grid[-3:])

    def test_king_prefers_multi_jump(self):
        grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "b", ".", "b", ".", "."],
            [".", ".", ".", ".", "R", ".", ".", "."],
            [".", ".", ".", "b", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "b", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]
        expected_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "b", ".", "b", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "R", ".", ".", "."],
        ]

        initial_state = State(grid, True)
        best_util, best_move = alpha_beta(initial_state, -inf, inf, depth_limit=5)

        self.assertEqual(0, best_util)
        self.assertEqual(expected_grid, best_move.grid)

    def test_king_doesnt_fall_for_trap(self):
        grid = [
            [".", "b", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "b", ".", ".", ".", "."],
            [".", ".", ".", ".", "R", ".", ".", "."],
            [".", ".", ".", "b", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]
        expected_grid = [
            [".", "b", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "b", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "R", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]

        initial_state = State(grid, True)
        best_util, best_move = alpha_beta(initial_state, -inf, inf, depth_limit=5)

        self.assertEqual(0, best_util)
        self.assertEqual(expected_grid[-4:], best_move.grid[-4:])

    def test_no_successors_returns_none(self):
        grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "b", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]

        initial_max_state = State(grid, True)
        best_max_util, best_max_move = alpha_beta(initial_max_state, -inf, inf, depth_limit=5)

        initial_min_state = State(grid, False)
        best_min_util, best_min_move = alpha_beta(initial_min_state, -inf, inf, depth_limit=5)

        self.assertEqual(-1, best_max_util)
        self.assertIsNone(best_max_move)
        self.assertEqual(-1, best_min_util)
        self.assertIsNone(best_min_move)

    def test_solution(self):
        grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "b", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "R"],
            [".", ".", "b", ".", "b", ".", ".", "."],
            [".", ".", ".", "b", ".", ".", ".", "r"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "r", ".", ".", ".", "."],
            [".", ".", ".", ".", "B", ".", ".", "."],
        ]
        expected_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "b", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "R"],
            [".", ".", "b", ".", "b", ".", "r", "."],
            [".", ".", ".", "b", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "r", ".", ".", ".", "."],
            [".", ".", ".", ".", "B", ".", ".", "."],
        ]

        initial_state = State(grid, True)
        _, best_alpha_beta_move = alpha_beta(initial_state, -inf, inf, depth_limit=8)

        self.assertEqual(expected_grid, best_alpha_beta_move.grid)


if __name__ == "__main__":
    unittest.main()

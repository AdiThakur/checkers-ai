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
        puzzle_file_name = "puzzle1.txt"

        result = generate_grid(puzzle_file_name)

        self.assertEqual(expected_grid, result)


class TestBasicUtility(unittest.TestCase):
    def test_some_max_and_min(self):
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

        state = State(grid, True)
        utility = basic_utility(state)

        self.assertEqual(-2, utility)
    
    def test_no_max_some_min(self):
        grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "b", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "b", ".", "b", ".", ".", "."],
            [".", ".", ".", "b", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "B", ".", ".", "."],
        ]

        state = State(grid, True)
        utility = basic_utility(state)

        self.assertEqual(-6, utility)

    def test_some_max_no_min(self):
        grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "r", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "r", ".", "r", ".", ".", "."],
            [".", ".", ".", "r", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "R", ".", ".", "."],
        ]

        state = State(grid, True)
        utility = basic_utility(state)

        self.assertEqual(6, utility)


class TestMinimax(unittest.TestCase):
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
        best_util, best_move = df_minimax(initial_state, 2)

        self.assertEqual(0, best_util)
        self.assertEqual(expected_grid_fragment, best_move.grid[-3:])

    def test_max_picks_highest_util_successor_depth_1(self):
        grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "B", ".", "b", ".", ".", "."],
            [".", ".", ".", "r", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]
        expected_grid_fragment = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", "r", ".", ".", ".", ".", ".", "."],
        ]

        initial_state = State(grid, True)
        best_util, best_move = df_minimax(initial_state, 1)

        self.assertEqual(0, best_util)
        self.assertEqual(expected_grid_fragment, best_move.grid[:4])

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
        best_util, best_move = df_minimax(initial_state, 5)

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
        best_util, best_move = df_minimax(initial_state, 5)

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
        best_max_util, best_max_move = df_minimax(initial_max_state, 5)

        initial_min_state = State(grid, False)
        best_min_util, best_min_move = df_minimax(initial_min_state, 5)

        self.assertEqual(-1, best_max_util)
        self.assertIsNone(best_max_move)
        self.assertEqual(-1, best_min_util)
        self.assertIsNone(best_min_move)


if __name__ == "__main__":
    unittest.main()
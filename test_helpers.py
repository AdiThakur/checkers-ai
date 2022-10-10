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


if __name__ == "__main__":
    unittest.main()
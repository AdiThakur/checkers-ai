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


if __name__ == "__main__":
    unittest.main()
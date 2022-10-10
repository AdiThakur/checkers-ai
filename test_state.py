import unittest
from checkers import State


# Testing jump abilities of a man (non-King) piece
class TestManJump(unittest.TestCase):
    def test_single_jump_1(self):
        initial_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "b", ".", ".", ".", "."],
            [".", ".", ".", ".", "r", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]
        expected_max_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "r", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]
        expected_min_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "b", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]

        initial_max_state = State(initial_grid, True)
        max_moves = initial_max_state._jump_move(initial_max_state.grid, (4, 4))

        initial_min_state = State(initial_grid, False)
        min_moves = initial_min_state._jump_move(initial_min_state.grid, (3, 3))

        self.assertEqual(expected_max_grid, max_moves[0])
        self.assertEqual(expected_min_grid, min_moves[0])

    def test_single_jump_2(self):
        initial_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "b", ".", "."],
            [".", ".", ".", ".", "r", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]
        expected_max_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "r", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]
        expected_min_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "b", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]

        initial_max_state = State(initial_grid, True)
        max_moves = initial_max_state._jump_move(initial_max_state.grid, (4, 4))

        initial_min_state = State(initial_grid, False)
        min_moves = initial_min_state._jump_move(initial_min_state.grid, (3, 5))

        self.assertEqual(expected_max_grid, max_moves[0])
        self.assertEqual(expected_min_grid, min_moves[0])

    def test_single_jump_3(self):
        initial_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "r", ".", ".", "."],
            [".", ".", ".", "b", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]

        initial_max_state = State(initial_grid, True)
        max_moves = initial_max_state._jump_move(initial_max_state.grid, (4, 4))

        initial_min_state = State(initial_grid, False)
        min_moves = initial_min_state._jump_move(initial_min_state.grid, (5, 3))

        self.assertEqual(0, len(max_moves))
        self.assertEqual(0, len(min_moves))

    def test_single_jump_4(self):
        initial_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "r", ".", ".", "."],
            [".", ".", ".", ".", ".", "b", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]

        initial_max_state = State(initial_grid, True)
        max_moves = initial_max_state._jump_move(initial_max_state.grid, (4, 4))

        initial_min_state = State(initial_grid, False)
        min_moves = initial_min_state._jump_move(initial_min_state.grid, (5, 5))

        self.assertEqual(0, len(max_moves))
        self.assertEqual(0, len(min_moves))

    def test_max_single_jump_left_edge(self):
        initial_grid = [
            ["b", ".", ".", ".", ".", ".", ".", "."],
            [".", "r", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]

        initial_max_state = State(initial_grid, True)
        max_moves = initial_max_state._jump_move(initial_max_state.grid, (1, 1))

        self.assertEqual(0, len(max_moves))

    def test_max_single_jump_right_edge(self):
        initial_grid = [
            [".", ".", ".", ".", ".", ".", ".", "b"],
            [".", ".", ".", ".", ".", ".", "r", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]

        initial_max_state = State(initial_grid, True)
        max_moves = initial_max_state._jump_move(initial_max_state.grid, (1, 6))

        self.assertEqual(0, len(max_moves))

    def test_min_single_jump_left_edge(self):
        initial_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", "b", ".", ".", ".", ".", ".", "."],
            ["r", ".", ".", ".", ".", ".", ".", "."],
        ]

        initial_min_state = State(initial_grid, False)
        min_moves = initial_min_state._jump_move(initial_min_state.grid, (6, 1))

        self.assertEqual(0, len(min_moves))

    def test_min_single_jump_right_edge(self):
        initial_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "b", "."],
            [".", ".", ".", ".", ".", ".", ".", "r"],
        ]

        initial_min_state = State(initial_grid, False)
        min_moves = initial_min_state._jump_move(initial_min_state.grid, (6, 6))

        self.assertEqual(0, len(min_moves))

    def test_max_multi_jump_1(self):
        initial_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "b", ".", "b", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "b", ".", "b", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "b", ".", ".", "."],
            [".", ".", ".", "r", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]

        initial_state = State(initial_grid, True)
        moves = initial_state._jump_move(initial_state.grid, (6, 3))

        self.assertEqual(3, len(moves))

    def test_max_multi_jump_2(self):
        initial_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "b", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "b", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "b", ".", ".", "."],
            [".", ".", ".", "r", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]
        expected_grid = [
            [".", ".", ".", ".", ".", "r", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]

        initial_state = State(initial_grid, True)
        moves = initial_state._jump_move(initial_state.grid, (6, 3))

        self.assertEqual(expected_grid, moves[0])

    def test_min_multi_jump_1(self):
        initial_grid = [
            [".", ".", ".", "b", ".", ".", ".", "."],
            [".", ".", "r", ".", "r", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "r", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "r", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]

        initial_state = State(initial_grid, True)
        moves = initial_state._jump_move(initial_state.grid, (0, 3))

        self.assertEqual(2, len(moves))

    def test_min_multi_jump_2(self):
        initial_grid = [
            [".", ".", ".", "b", ".", ".", ".", "."],
            [".", ".", ".", ".", "r", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "r", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "r", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "r", ".", ".", "."],
        ]
        expected_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "b", ".", "."],
            [".", ".", ".", ".", "r", ".", ".", "."],
        ]

        initial_state = State(initial_grid, True)
        moves = initial_state._jump_move(initial_state.grid, (0, 3))

        self.assertEqual(expected_grid, moves[0])


class TestKingJump(unittest.TestCase):
    def test_max_single_jump_1(self):
        initial_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "b", ".", "b", ".", ".", "."],
            [".", ".", ".", "R", ".", ".", ".", "."],
            [".", ".", "b", ".", "b", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]

        initial_state = State(initial_grid, True)
        moves = initial_state._jump_move(initial_state.grid, (3, 3))

        self.assertEqual(4, len(moves))

    def test_min_single_jump_1(self):
        initial_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "r", ".", "r", ".", ".", "."],
            [".", ".", ".", "B", ".", ".", ".", "."],
            [".", ".", "r", ".", "r", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]

        initial_state = State(initial_grid, False)
        moves = initial_state._jump_move(initial_state.grid, (3, 3))

        self.assertEqual(4, len(moves))

    def test_circular_jump(self):
        initial_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "r", ".", "r", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "r", ".", "r", ".", ".", "."],
            [".", ".", ".", "B", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]
        expected_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "B", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]

        initial_state = State(initial_grid, False)
        moves = initial_state._jump_move(initial_state.grid, (5, 3))

        self.assertEqual(2, len(moves))
        self.assertEqual(expected_grid, moves[0])
        self.assertEqual(expected_grid, moves[1])


if __name__ == "__main__":
    unittest.main()

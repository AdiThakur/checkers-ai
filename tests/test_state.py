import unittest
from checkers import State


class TestGetSuccessors(unittest.TestCase):
    def test_man_edge_cases(self):
        initial_grid = [
            ["r", ".", ".", ".", ".", ".", ".", "r"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["b", ".", ".", ".", ".", ".", ".", "b"],
        ]

        initial_max_state = State(initial_grid, True)
        max_moves = initial_max_state.get_successors()

        initial_min_state = State(initial_grid, True)
        min_moves = initial_min_state.get_successors()

        self.assertEqual(0, len(max_moves))
        self.assertEqual(0, len(min_moves))

    def test_king_edge_cases(self):
        initial_grid = [
            ["R", ".", ".", ".", ".", ".", ".", "R"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["B", ".", ".", ".", ".", ".", ".", "B"],
        ]

        initial_max_state = State(initial_grid, True)
        max_moves = initial_max_state.get_successors()

        initial_min_state = State(initial_grid, True)
        min_moves = initial_min_state.get_successors()

        self.assertEqual(2, len(max_moves))
        self.assertEqual(2, len(min_moves))

    def test_max_single_and_jump_moves(self):
        initial_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "R", ".", ".", ".", ".", "."],
            [".", "b", ".", "b", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "b", ".", ".", ".", "."],
            [".", ".", ".", ".", "r", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]

        initial_state = State(initial_grid, True)
        moves = initial_state.get_successors()

        self.assertEqual(4, len(moves))

    def test_max_mandatory_captures(self):
        initial_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "b", ".", ".", ".", ".", "."],
            [".", ".", ".", "R", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "r", ".", "."],
            [".", ".", "b", ".", ".", ".", ".", "."],
            [".", "r", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]

        initial_state = State(initial_grid, True)
        moves = initial_state.get_successors()

        self.assertEqual(2, len(moves))

    def test_min_mandatory_captures(self):
        initial_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "b", ".", ".", ".", ".", "."],
            [".", ".", ".", "R", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "r", ".", "."],
            [".", ".", "b", ".", ".", ".", ".", "."],
            [".", "r", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]

        initial_state = State(initial_grid, False)
        moves = initial_state.get_successors()

        self.assertEqual(2, len(moves))

    def test_max_promotion(self):
        initial_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", "r", ".", ".", ".", ".", "r", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["b", ".", ".", ".", ".", ".", "b", "."],
        ]

        initial_state = State(initial_grid, True)
        moves = initial_state.get_successors()

        self.assertEqual(4, len(moves))
        for move in moves:
            self.assertTrue("R" in move[0])
            self.assertTrue("B" not in move[7])

    def test_min_promotion(self):
        initial_grid = [
            ["r", ".", ".", ".", ".", ".", ".", "r"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "b", ".", ".", ".", ".", "."],
            [".", "r", ".", ".", ".", ".", "b", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]

        initial_state = State(initial_grid, False)
        moves = initial_state.get_successors()

        self.assertEqual(1, len(moves))
        for move in moves:
            self.assertTrue("B" in move[7])
            self.assertTrue("R" not in move[0])


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
            [".", ".", ".", ".", ".", "R", ".", "."],
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

    def test_min_multi_jump_terminates_when_promoted(self):
        initial_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "b", ".", "."],
            [".", ".", ".", ".", "r", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "r", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "r", ".", "r", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]
        expected_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "r", ".", ".", ".", ".", "."],
            [".", ".", ".", "B", ".", ".", ".", "."],
        ]

        initial_state = State(initial_grid, False)
        moves = initial_state._jump_move(initial_state.grid, (1, 5))

        self.assertEqual(expected_grid, moves[0])

    def test_max_multi_jump_terminates_when_promoted(self):
        initial_grid = [
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "b", ".", "b", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "b", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "b", ".", ".", "."],
            [".", ".", ".", ".", ".", "r", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]
        expected_grid = [
            [".", ".", ".", "R", ".", ".", ".", "."],
            [".", ".", "b", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
        ]

        initial_state = State(initial_grid, True)
        moves = initial_state._jump_move(initial_state.grid, (6, 5))

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

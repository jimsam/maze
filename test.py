import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(num_rows, num_cols)
        self.assertEqual(len(m1._cells), num_rows)
        self.assertEqual(len(m1._cells[0]), num_cols)

    def test_start_end_open_walls(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(num_rows, num_cols)
        self.assertEqual(m1._cells[0][0].has_left_wall, False)
        self.assertEqual(m1._cells[num_rows - 1][num_cols - 1].has_right_wall, False)


if __name__ == "__main__":
    unittest.main()

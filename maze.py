import random
import time

from cell import Cell
from point import Point


class Maze:
    def __init__(self, nums_rows, nums_cols, win=None, seed=None):
        self.nums_rows = nums_cols
        self.nums_cols = nums_rows
        self._win = win
        self._cells = []
        self._create_cells()
        self._found_exit = False
        self.seed = random.seed(seed)
        self._break_walls_r()
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self.nums_cols):
            col = []
            for j in range(self.nums_rows):
                col.append(Cell(Point(i * 50 + 10, j * 50 + 10), self._win))
            self._cells.append(col)
        for i in range(self.nums_cols):
            for j in range(self.nums_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        if i == 0 and j == 0:
            cell.has_top_wall = False
            cell.start_cell = True
        if j == self.nums_rows - 1 and i == self.nums_cols - 1:
            cell.has_bottom_wall = False
            cell.end_cell = True
        cell.draw()
        self._animate()

    def _animate(self, speed=0.03):
        if self._win is not None:
            self._win.redraw()
            time.sleep(speed)

    def _break_walls_r(self, i=0, j=0):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # Top Cell
            if j > 0 and self._cells[i][j - 1].visited == False:
                to_visit.append((i, j - 1))
            # Left Cell
            if i > 0 and self._cells[i - 1][j].visited == False:
                to_visit.append((i - 1, j))
            # Down Cell
            if j < self.nums_rows - 1 and self._cells[i][j + 1].visited == False:
                to_visit.append((i, j + 1))
            # Right Cell
            if i < self.nums_cols - 1 and self._cells[i + 1][j].visited == False:
                to_visit.append((i + 1, j))

            if len(to_visit) == 0:
                self._cells[i][j].draw()
                return
            index_to_visit = random.randrange(len(to_visit))
            new_index = to_visit[index_to_visit]

            if new_index[0] == i + 1:
                self._break_for_right(i, j)
            if new_index[0] == i - 1:
                self._break_for_left(i, j)
            if new_index[1] == j + 1:
                self._break_for_bottom(i, j)
            if new_index[1] == j - 1:
                self._break_for_top(i, j)

            self._break_walls_r(new_index[0], new_index[1])

    def _break_for_top(self, i, j):
        self._cells[i][j].break_wall("top")
        self._cells[i][j - 1].break_wall("down")

    def _break_for_left(self, i, j):
        self._cells[i][j].break_wall("left")
        self._cells[i - 1][j].break_wall("right")

    def _break_for_bottom(self, i, j):
        self._cells[i][j].break_wall("down")
        self._cells[i][j + 1].break_wall("top")

    def _break_for_right(self, i, j):
        self._cells[i][j].break_wall("right")
        self._cells[i + 1][j].break_wall("left")

    def _reset_cells_visited(self):
        for i in range(self.nums_cols):
            for j in range(self.nums_rows):
                self._cells[i][j].visited = False

    def _solve_r(self, i=0, j=0):
        self._animate()
        self._cells[i][j].visited = True

        if self._cells[i][j].end_cell == True:
            print("Found exit!")
            return True

        # Left
        if (
            i > 0
            and self._cells[i - 1][j].visited == False
            and not self._cells[i][j].has_left_wall
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)
        # Up
        if (
            j > 0
            and self._cells[i][j - 1].visited == False
            and not self._cells[i][j].has_top_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        # Right
        if (
            i + 1 < self.nums_cols
            and self._cells[i + 1][j].visited == False
            and not self._cells[i][j].has_right_wall
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        # Down
        if (
            j + 1 < self.nums_rows
            and self._cells[i][j + 1].visited == False
            and not self._cells[i][j].has_bottom_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        return False

    def solve(self):
        self._solve_r()

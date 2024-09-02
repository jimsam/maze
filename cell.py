from line import Line
from point import Point


class Cell:
    def __init__(self, start_point: Point, window=None):
        self._x1 = start_point
        self._x2 = Point(start_point.x + 50, start_point.y)
        self._y1 = Point(start_point.x, start_point.y + 50)
        self._y2 = Point(start_point.x + 50, start_point.y + 50)
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = window
        self.visited = False
        self.start_cell = False
        self.end_cell = False

    def draw(self):
        self._draw_line(
            Line(self._x1, self._x2), "black" if self.has_top_wall else "#d9d9d9"
        )
        self._draw_line(
            Line(self._x2, self._y2), "black" if self.has_right_wall else "#d9d9d9"
        )
        self._draw_line(
            Line(self._x1, self._y1), "black" if self.has_left_wall else "#d9d9d9"
        )
        self._draw_line(
            Line(self._y1, self._y2), "black" if self.has_bottom_wall else "#d9d9d9"
        )

    def draw_move(self, cell, undo=False):
        tmp_line = Line(
            Point(self._x1.x + 24, self._x1.y + 24),
            Point(cell._x1.x + 24, cell._x1.y + 24),
        )
        if self._win is not None:
            self._win.draw_line(tmp_line, "red" if undo else "grey")

    def _draw_line(self, line: Line, color):
        if self._win is not None:
            self._win.draw_line(line, color)

    def break_wall(self, directions):
        match directions:
            case "top":
                self.has_top_wall = False
                self.draw()
            case "down":
                self.has_bottom_wall = False
                self.draw()
            case "right":
                self.has_right_wall = False
                self.draw()
            case "left":
                self.has_left_wall = False
                self.draw()

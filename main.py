from maze import Maze
from window import Window


def main():
    win = Window(800, 800)
    maze = Maze(10, 12, win)
    maze.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()

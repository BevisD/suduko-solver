import numpy as np


class Sudoku:
    def __init__(self, cells, box_size=3):
        self.cells = np.array(cells, dtype=np.int8)
        self.n = self.cells.shape[0]
        self.box_size = box_size
        self.solutions = []

    def __str__(self):
        string = ''
        for row in self.cells:
            string += str(row)[1:-1]
            string += '\n'
        return string

    def check_row(self, row):
        return sorted(self.cells[row]) == [i + 1 for i in range(self.n)]

    def check_col(self, col):
        return sorted(self.cells[:, col]) == [i + 1 for i in range(self.n)]

    def check_box(self, row, col):
        return sorted(self.cells[row:row + self.box_size, col:col + self.box_size].flatten()) == [i + 1 for i in
                                                                                                  range(self.n)]

    def check(self):
        if not all([self.check_row(row) for row in range(self.n)]):
            return 0

        if not all([self.check_col(col) for col in range(self.n)]):
            return 0

        for i in range(self.box_size):
            for j in range(self.box_size):
                if not self.check_box(self.box_size * i, self.box_size * j):
                    return 0
        return 1

    def solve(self):
        if self.check():
            print("SOLUTION")
            print(self)
            self.solutions.append(self.cells.copy())
            return

        for row in range(self.n):
            for col in range(self.n):
                cell = self.cells[row][col]
                if cell == 0:
                    for value in range(1, self.n + 1):
                        if value in self.cells[row]:
                            continue
                        if value in self.cells[:, col]:
                            continue

                        box_row = self.box_size * (row // self.box_size)
                        box_col = self.box_size * (col // self.box_size)
                        if value in self.cells[box_row:box_row + self.box_size, box_col:box_col + self.box_size]:
                            continue

                        self.cells[row][col] = value
                        self.solve()
                    self.cells[row][col] = 0
                    return
                else:
                    continue


sudoku = Sudoku([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]])

if __name__ == "__main__":
    sudoku.solve()
    print(len(sudoku.solutions))

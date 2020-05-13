from .cell import Cell


class Board:
    def __init__(self, num_rows, num_cols):
        self._matrix = [[Cell(y, x) for x in range(num_cols)] for y in range(num_rows)]

    @property
    def matrix(self):
        return self._matrix

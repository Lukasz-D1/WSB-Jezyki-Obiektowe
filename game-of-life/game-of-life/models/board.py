from .cell import Cell
from abc import ABC
from random import randint
from .rules import AbstractRules, StaticRules


class AbstractBoard(ABC):
    def __init__(self, num_rows, num_cols):
        self._num_rows = num_rows
        self._num_cols = num_cols

    @property
    def num_rows(self):
        return self._num_rows

    @num_rows.setter
    def num_rows(self, val):
        self._num_rows = val

    @property
    def num_cols(self):
        return self._num_cols

    @num_cols.setter
    def num_cols(self, val):
        self._num_cols = val


class Board(AbstractBoard):
    def __init__(self, num_rows, num_cols, visuals):
        super().__init__(num_rows, num_cols)
        self._matrix = [[Cell(y, x) for x in range(num_cols)] for y in range(num_rows)]
        self._run_game = False
        self._gen = 0
        self._rules = StaticRules()
        self.vis = visuals

    @property
    def run_game(self):
        return self._run_game

    @run_game.setter
    def run_game(self, val):
        self._run_game = val

    @property
    def matrix(self):
        return self._matrix

    def entry_point(self, entry_point):
        if entry_point == 'glider':
            # Entry point (glider):
            self.matrix[0][0].is_alive = True
            self.matrix[1][1].is_alive = True
            self.matrix[1][2].is_alive = True
            self.matrix[2][0].is_alive = True
            self.matrix[2][1].is_alive = True
        else:
            # Entry point (random):
            for i in range(self.num_rows * 4):
                self.matrix[randint(0, self.num_rows - 5)][randint(0, self.num_cols - 5)].is_alive = True

    def game_of_life(self):
        if self._run_game:
            print("Generation: {}".format(self._gen))
            self._gen += 1
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    self._rules.check_neighbourhood(self, self.matrix[i][j].x, self.matrix[i][j].y)
                    if self.matrix[i][j].is_alive:
                        self.vis.update(i * self.vis.size_of_cell, j * self.vis.size_of_cell, 1)
                    else:
                        self.vis.update(i * self.vis.size_of_cell, j * self.vis.size_of_cell, 0)
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    self._rules.decide(self, i, j)


if __name__ == '__main__':
    brd = Board(10, 10)
    print(brd.matrix)

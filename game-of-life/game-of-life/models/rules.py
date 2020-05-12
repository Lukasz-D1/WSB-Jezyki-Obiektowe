from abc import ABC, abstractmethod


class AbstractRules(ABC):
    def __init__(self):
        pass


class Rules(AbstractRules):
    def __init__(self, cell_x, cell_y, board):
        self._cell_x = cell_x
        self._cell_y = cell_y
        self._board = board

    def check_neighbourhood(self):
        cnt = 0

        if self._cell_x != 0:
            if self._cell_y != 0:
                if self._board.matrix[self._cell_x - 1][self._cell_y - 1].is_alive:
                    cnt += 1
            if self._board.matrix[self._cell_x - 1][self._cell_y].is_alive:
                cnt += 1
            if self._cell_y != len(self._board.matrix) - 1:
                if self._board.matrix[self._cell_x - 1][self._cell_y + 1].is_alive:
                    cnt += 1

        if self._cell_y != 0:
            if self._board.matrix[self._cell_x][self._cell_y - 1].is_alive:
                cnt += 1
        if self._cell_y != len(self._board.matrix) - 1:
            if self._board.matrix[self._cell_x][self._cell_y + 1].is_alive:
                cnt += 1

        if self._cell_x != len(self._board.matrix) - 1:
            if self._cell_y != 0:
                if self._board.matrix[self._cell_x + 1][self._cell_y - 1].is_alive:
                    cnt += 1
            if self._board.matrix[self._cell_x + 1][self._cell_y].is_alive:
                cnt += 1
            if self._cell_y != len(self._board.matrix) - 1:
                if self._board.matrix[self._cell_x + 1][self._cell_y + 1].is_alive:
                    cnt += 1
        if self._cell_x == 1 and self._cell_y == 1:
            print(cnt)

        if self._board.matrix[self._cell_x][self._cell_y].is_alive:
            if (cnt < 2) or (cnt > 3):
                self._board.matrix[self._cell_x][self._cell_y].is_alive = False
        else:
            if cnt == 3:
                self._board.matrix[self._cell_x][self._cell_y].is_alive = True

        # if not self._board.matrix[self._cell_x][self._cell_y].is_alive and cnt == 3:
        #     self._board.matrix[self._cell_x][self._cell_y].is_alive = True
        # elif self._board.matrix[self._cell_x][self._cell_y].is_alive and cnt == 2:
        #     self._board.matrix[self._cell_x][self._cell_y].is_alive = True
        # elif self._board.matrix[self._cell_x][self._cell_y].is_alive and cnt == 3:
        #     self._board.matrix[self._cell_x][self._cell_y].is_alive = True
        # else:
        #     self._board.matrix[self._cell_x][self._cell_y].is_alive = False



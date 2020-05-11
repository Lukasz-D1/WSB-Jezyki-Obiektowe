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
                #print(self._cell_x - 1, self._cell_y - 1)
                if self._board.matrix[self._cell_x - 1][self._cell_y - 1].is_alive:
                    cnt += 1
            #print(self._cell_x - 1, self._cell_y)
            if self._board.matrix[self._cell_x - 1][self._cell_y].is_alive:
                cnt += 1
            if self._cell_y != 9:
                #print(self._cell_x - 1, self._cell_y + 1)
                if self._board.matrix[self._cell_x - 1][self._cell_y + 1].is_alive:
                    cnt += 1

        if self._cell_y != 0:
            #print(self._cell_x, self._cell_y - 1)
            if self._board.matrix[self._cell_x][self._cell_y - 1].is_alive:
                cnt += 1
        if self._cell_y != 9:
            #print(self._cell_x, self._cell_y + 1)
            if self._board.matrix[self._cell_x][self._cell_y + 1].is_alive:
                cnt += 1

        if self._cell_x != 9:
            if self._cell_y != 0:
                #print(self._cell_x + 1, self._cell_y - 1)
                if self._board.matrix[self._cell_x + 1][self._cell_y - 1].is_alive:
                    cnt += 1
            #print(self._cell_x + 1, self._cell_y)
            if self._board.matrix[self._cell_x + 1][self._cell_y].is_alive:
                cnt += 1
            if self._cell_y != 9:
                #print(self._cell_x + 1, self._cell_y + 1)
                if self._board.matrix[self._cell_x + 1][self._cell_y + 1].is_alive:
                    cnt += 1
        if self._cell_x == 1 and self._cell_y == 1:
            print(cnt)

        if cnt == 2 or cnt == 3:
            self._board.matrix[self._cell_x][self._cell_y].is_alive = True
            #print('Cell should be alive')
        elif cnt > 2 or cnt < 3:
            self._board.matrix[self._cell_x][self._cell_y].is_alive = False
            #print('Cell should be dead')


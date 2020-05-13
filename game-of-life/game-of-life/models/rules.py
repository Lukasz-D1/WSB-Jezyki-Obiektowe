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


class StaticRules:
    @staticmethod
    def check_neighbourhood(board, i, j):
        cnt = 0

        if i != 0:
            if j != 0:
                if board.matrix[i - 1][j - 1].is_alive:
                    cnt += 1

            if board.matrix[i - 1][j].is_alive:
                cnt += 1

            if j != len(board.matrix) - 1:
                if board.matrix[i - 1][j + 1].is_alive:
                    cnt += 1
        if j != 0:
            if i == 0 and j == 2:
                print('III', i, 'JJJ', j-1, 'ALL', board.matrix[i][j - 1].is_alive)
            if board.matrix[i][j - 1].is_alive:
                if i == 0 and j == 2:
                    print('A')
                cnt += 1
        if j != len(board.matrix) - 1:
            if board.matrix[i][j + 1].is_alive:
                if i == 0 and j == 2:
                    print('B')
                cnt += 1

        if i != len(board.matrix) - 1:
            if j != 0:
                if board.matrix[i + 1][j - 1].is_alive:
                    if i == 0 and j == 2:
                        print('C')
                    cnt += 1
            if board.matrix[i + 1][j].is_alive:
                if i == 0 and j == 2:
                    print('D')
                cnt += 1
            if j != len(board.matrix) - 1:
                if board.matrix[i + 1][j + 1].is_alive:
                    if i == 0 and j == 2:
                        print('E')
                    cnt += 1
        # if i != 0:
        #     if j != 0:
        #         if board.matrix[i - 1][j - 1].is_alive:
        #             cnt += 1
        #     if board.matrix[i - 1][j].is_alive:
        #         cnt += 1
        #     if j != len(board.matrix) - 1:
        #         if board.matrix[i - 1][j + 1].is_alive:
        #             cnt += 1
        #
        # if j != 0:
        #     if board.matrix[i][j - 1].is_alive:
        #         cnt += 1
        # if j != len(board.matrix) - 1:
        #     if board.matrix[i][j + 1].is_alive:
        #         cnt += 1
        #
        # if i != len(board.matrix) - 1:
        #     if j != 0:
        #         if board.matrix[i + 1][j - 1].is_alive:
        #             cnt += 1
        #     if board.matrix[i + 1][j].is_alive:
        #         cnt += 1
        #     if j != len(board.matrix) - 1:
        #         if board.matrix[i + 1][j + 1].is_alive:
        #             cnt += 1

        board.matrix[i][j].cnt = cnt

    @staticmethod
    def decide(board, i, j):
        if board.matrix[i][j].is_alive:
            if (board.matrix[i][j].cnt < 2) or (board.matrix[i][j].cnt > 3):
                board.matrix[i][j].is_alive = False
        else:
            if board.matrix[i][j].cnt == 3:
                board.matrix[i][j].is_alive = True



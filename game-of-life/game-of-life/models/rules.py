from abc import ABC, abstractmethod


class AbstractRules(ABC):
    @staticmethod
    @abstractmethod
    def check_neighbourhood(*args, **kwargs):
        pass

    @staticmethod
    @abstractmethod
    def decide(*args, **kwargs):
        pass


class StaticRules(AbstractRules):
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
            if board.matrix[i][j - 1].is_alive:
                cnt += 1
        if j != len(board.matrix) - 1:
            if board.matrix[i][j + 1].is_alive:
                cnt += 1
        if i != len(board.matrix) - 1:
            if j != 0:
                if board.matrix[i + 1][j - 1].is_alive:
                    cnt += 1
            if board.matrix[i + 1][j].is_alive:
                cnt += 1
            if j != len(board.matrix) - 1:
                if board.matrix[i + 1][j + 1].is_alive:
                    cnt += 1

        board.matrix[i][j].cnt = cnt

    @staticmethod
    def decide(board, i, j):
        if board.matrix[i][j].is_alive:
            if (board.matrix[i][j].cnt < 2) or (board.matrix[i][j].cnt > 3):
                board.matrix[i][j].is_alive = False
        else:
            if board.matrix[i][j].cnt == 3:
                board.matrix[i][j].is_alive = True


if __name__ == '__main__':
    sru = StaticRules()

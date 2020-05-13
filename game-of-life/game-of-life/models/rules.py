from abc import ABC


class AbstractRules(ABC):
    def __init__(self):
        pass


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

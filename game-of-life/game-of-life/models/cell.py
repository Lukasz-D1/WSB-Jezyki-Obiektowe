from abc import ABC, abstractmethod
from .rules import Rules


class AbstractCell(ABC):
    def __init__(self, x, y, board):
        self._is_alive = False
        self._x = x
        self._y = y
        self._rules = Rules(self._x, self._y, board)

    @property
    def is_alive(self):
        return self._is_alive

    @is_alive.setter
    def is_alive(self, val):
        self._is_alive = val

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        self._x = val

    @property
    def y(self):
        return self._y

    @x.setter
    def y(self, val):
        self._y = val

    @property
    def rules(self):
        return self._rules


class Cell(AbstractCell):
    def __init__(self, x, y, board):
        super().__init__(x, y, board)


if __name__ == '__main__':
    cl = Cell(3, 4)
    print(cl.is_alive)

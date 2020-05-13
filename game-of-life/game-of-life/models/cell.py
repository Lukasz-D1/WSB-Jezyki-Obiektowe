from abc import ABC


class AbstractCell(ABC):
    def __init__(self):
        pass


class Cell(AbstractCell):
    def __init__(self, x, y):
        self._is_alive = False
        self._x = x
        self._y = y
        self._cnt = 0

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

    @y.setter
    def y(self, val):
        self._y = val

    @property
    def cnt(self):
        return self._cnt

    @cnt.setter
    def cnt(self, val):
        self._cnt = val


if __name__ == '__main__':
    cl = Cell(3, 4)
    print(cl.is_alive)

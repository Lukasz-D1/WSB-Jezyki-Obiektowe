from functools import wraps


class CountDecorator:
    def __init__(self, func):
        self.__func = func
        self.__cnt = 0
        wraps(self.__func)

    def __call__(self, *args, **kwargs):
        self.__cnt += 1
        print('Function ran {} time(s)'.format(self.__cnt))
        return self.__func(*args, **kwargs)


class FibonacciIter:
    def __init__(self, arg):
        self.__arg = arg
        self.__current = 0
        self.__a = 0
        self.__b = 1
        print('F{} = {}'.format(self.__current, self.__a))

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current == self.__arg:
            raise StopIteration
        self.__current += 1
        if self.__current == 1:
            return 1
        tmp = self.__a + self.__b
        self.__a = self.__b
        self.__b = tmp
        return tmp


@CountDecorator
def f():
    pass


def main():
    obj = FibonacciIter(150)
    it = iter(obj)
    for el in it:
        print(el)
    for i in range(10):
        f()


if __name__ == '__main__':
    main()
from math import sqrt
from functools import wraps


def zad0():
    for el in range(1, 20, 1):
        if not el % 2:
            print(el, end=' ')


def print_building(height, width):
    for h in range(height+1):
        for w in range(width+1):
            if h % height == 0 and w % width == 0:
                print('*', end='')
            elif h % height == 0 and w % width != 0:
                print('-', end='')
            elif h % height != 0 and w % width == 0:
                print('|', end='')
            else:
                print('.', end='')
        print('')


def zad1():
    height = int(input('Give height: '))
    width = int(input('Give width: '))
    print_building(height+1, width+1)


def zad2():
    arr_a = list(range(1, 10, 1))
    print(arr_a)
    print(arr_a[2::3])
    print(arr_a[::-1])
    print(arr_a[-2:1:-2])


def unique_elements(seq):
    # uniq_seq = set(seq)
    buf = set()
    for el in list(seq):
        if el in buf:
            seq.remove(el)
        else:
            buf.add(el)


def zad3():
    seq = [1, 2, 5, 2, 2, 2, 2, 1, 7, 8, 9, 76, 7, 34, 12, 3, 2, 1]
    unique_elements(seq)
    print(seq)


def my_sort(seq, prior):
    flag = False

    def f(arg):
        nonlocal flag
        if arg in prior:
            flag = True
            return 1, arg
        return 0, arg

    seq.sort(key=f)
    print(seq)
    return flag


def zad4():
    seq = [1, 2, 3, 4, 5, 5, 6, 7, 1, 2, 3, 4, 5, 6]
    prior = [1, 2]
    print(my_sort(seq, prior))


def is_prime(number):
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return number > 1


def filter_a(my_list):
    print(list(filter(is_prime, my_list)))


def filter_b(my_list):
    filtered = list(filter(lambda arg: arg > 1, my_list))
    print(list(filter(lambda x: all(map(lambda p: x % p != 0, range(2, x))), filtered)))


def filter_c(my_list):
    filtered = list(filter(lambda arg: arg > 1, my_list))
    print([x for x in filtered if all(x % y != 0 for y in range(2, x))])


def zad5():
    my_list = list(range(10))
    flag = 'c' # a - filter bez lambdy | b - filter i map + lambda | c - list comprehension
    if flag == 'a':
        filter_a(my_list)
    elif flag == 'b':
        filter_b(my_list)
    elif flag == 'c':
        filter_c(my_list)
    else:
        print('unknown')


def fib(arg):
    if arg == 0:
        return 0
    if arg == 1:
        return 1
    return fib(arg-1) + fib(arg-2)


def zad6():
    num = 12  # n-ty wyraz do wygenerowania (F0 = 0)
    print(fib(num))


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Nazwa: ' + func.__name__)
        print("Argumenty:")
        for el in args:
            print(el)
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def suma(a, b):
    return a+b


def zad7():
    suma(4, 7)


def count_decorator(func):
    @wraps(func)
    def count_wrapper(*args, **kwargs):
        count_wrapper.calls += 1
        return func(*args, **kwargs)
    count_wrapper.calls = 0
    return count_wrapper


@count_decorator
def roznica(a, b):
    return a-b


def zad8():
    for i in range(10):
        roznica(4, 3)
    print('Wywolano funkcje ' + str(roznica.calls) + ' razy')


def zad9():
    word_count = 0
    with open('test.txt', 'r', encoding='UTF-8') as fd:
        for el in fd:
            word_count += len(el.split())
        print('Liczba wyrazow w pliku: ' + str(word_count))


if __name__ == '__main__':
    zad0()

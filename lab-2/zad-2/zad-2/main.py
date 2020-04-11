from stack import Stack
from minstack import MinStack


def main():
    stack = MinStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print('Minimalna wartosc na stosie: {}'.format(stack.get_min_value()))


if '__main__' == __name__:
    main()

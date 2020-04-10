from stack import Stack
from minstack import MinStack


def main():
    stack = MinStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.get_min_value())

    while not stack.is_empty():
        print(stack.top())
        stack.pop()


if '__main__' == __name__:
    main()

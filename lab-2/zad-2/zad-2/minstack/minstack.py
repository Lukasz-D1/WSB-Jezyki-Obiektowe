from stack import Stack


class MinStack(Stack):
    def __init__(self):
        super().__init__()

    def get_stack_values(self):
        values = []
        while not self.is_empty():
            values.insert(0, self.top())
            self.pop()
        return values

    def rebuild_stack(self, values):
        for el in values:
            self.push(el)

    def get_min_value(self):
        values = self.get_stack_values()
        stack_min = min(values)
        self.rebuild_stack(values)
        return stack_min

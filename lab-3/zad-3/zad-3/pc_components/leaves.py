from .component import Component


class Disk(Component):
    def __init__(self, comp_id, price):
        super().__init__(comp_id, price, 'disk')

    def get_price(self):
        return self._price


class Motherboard(Component):
    def __init__(self, comp_id, price):
        super().__init__(comp_id, price, 'motherboard')

    def get_price(self):
        return self._price


class Card(Component):
    def __init__(self, comp_id, price):
        super().__init__(comp_id, price, 'card')

    def get_price(self):
        return self._price


if __name__ == '__main__':
    cd = Card(1, 1)
    print(cd.get_price())

from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, comp_id, price, type):
        super().__init__()
        self._id = comp_id
        self._price = price
        self._type = type

    @property
    def id(self):
        return self._id

    @property
    def type(self):
        return self._type

    @abstractmethod
    def get_price(self):
        return self._price

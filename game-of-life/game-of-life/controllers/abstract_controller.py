from abc import ABC, abstractmethod


class AbstractController(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def app(self, entry_point):
        pass

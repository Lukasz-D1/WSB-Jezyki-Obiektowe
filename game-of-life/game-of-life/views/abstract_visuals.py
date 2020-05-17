from abc import ABC, abstractmethod


class AbstractVisuals(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

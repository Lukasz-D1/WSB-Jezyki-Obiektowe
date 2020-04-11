from abc import ABC, abstractmethod


class Step(ABC):
    @abstractmethod
    def __call__(self, img):
        print('Base Step definition')

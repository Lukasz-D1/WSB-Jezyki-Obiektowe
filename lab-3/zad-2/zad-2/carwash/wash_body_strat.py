from abc import ABC, abstractmethod


class BodyAbstractWashStrategy(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def wash(self):
        pass


class BodyHandWashStrategy(BodyAbstractWashStrategy):
    def __init__(self):
        super().__init__()

    def wash(self):
        print("Myje karoserie recznie")


class BodyContactlessStrategy(BodyAbstractWashStrategy):
    def __init__(self):
        super().__init__()

    def wash(self):
        print("Myje karoserie bezdotykowo")

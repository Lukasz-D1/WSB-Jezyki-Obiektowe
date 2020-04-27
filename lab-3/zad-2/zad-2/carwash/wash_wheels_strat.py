from abc import ABC, abstractmethod


class WheelsAbstractWashStrategy(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def wash(self):
        pass


class WheelsHandWashStrategy(WheelsAbstractWashStrategy):
    def __init__(self):
        super().__init__()

    def wash(self):
        print("Myje kola recznie")


class WheelsContactlessStrategy(WheelsAbstractWashStrategy):
    def __init__(self):
        super().__init__()

    def wash(self):
        print("Myje kola bezdotykowo")
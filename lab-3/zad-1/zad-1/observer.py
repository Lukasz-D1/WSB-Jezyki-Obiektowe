from abc import ABC, abstractmethod
import progressbar


class Observer:
    def __init__(self):
        super().__init__()

    @abstractmethod
    def update(self, num):
        pass


class ProgressBarObserver(Observer):
    def __init__(self, max_val):
        super().__init__()
        self.bar = progressbar.ProgressBar(max_value=max_val)

    def update(self, num):
        self.bar.update(num)
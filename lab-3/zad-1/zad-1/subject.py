import time


class Subject:
    def __init__(self, max_val):
        self.__obs_list = []
        self.__cnt = 0
        self.__max_val = max_val

    def add_observer(self, obs):
        self.__obs_list.append(obs)

    def perform(self):
        while self.__cnt != self.__max_val:
            self.__cnt += 1
            self.notify(self.__cnt)
            time.sleep(0.5)

    def notify(self, num):
        for obs in self.__obs_list:
            obs.update(num)

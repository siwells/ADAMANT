from abc import ABCMeta, abstractmethod


class IGameDataCollector(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def collect(self):
        pass

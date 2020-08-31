from abc import ABCMeta, abstractmethod


class IHandler(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def handle(self):
        pass

    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def update_flag(self):
        pass

    @abstractmethod
    def update_collector(self):
        pass

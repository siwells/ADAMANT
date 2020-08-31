from abc import ABCMeta, abstractmethod


class IObservable(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def notify_all(self):
        pass

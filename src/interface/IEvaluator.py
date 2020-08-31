from abc import ABCMeta, abstractmethod


class IEvaluator(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def evaluate(self):
        pass

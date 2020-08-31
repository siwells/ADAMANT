from abc import ABCMeta, abstractmethod


class IGameEndController(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def is_finished(self) -> bool:
        pass

from abc import ABCMeta, abstractmethod


class IInputController(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_input(self):
        pass

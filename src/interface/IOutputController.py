from abc import ABCMeta, abstractmethod


class IOutputController(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def send_output(self):
        pass

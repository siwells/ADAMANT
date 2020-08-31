from abc import ABCMeta, abstractmethod

from helpers.Constants import EMPTY


class IArtifact(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, data_tmp: str = EMPTY):
        self.__data = data_tmp

    @abstractmethod
    def get_id(self) -> int:
        pass

    @abstractmethod
    def identify(self):
        pass

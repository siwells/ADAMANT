from abc import ABCMeta, abstractmethod
from interface import IGameDataCollector


class IGameObserver(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def update(self, i_game_data_collector: IGameDataCollector = None):
        """

        :type i_game_data_collector: IGameDataCollector
        """
        pass

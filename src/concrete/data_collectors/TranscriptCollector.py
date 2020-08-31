from helpers.Constants import EMPTY
from interface.IGameDataCollector import IGameDataCollector
from model.GameStatus import GameStatus


class TranscriptCollector(IGameDataCollector):
    def collect(self, game_status_tmp: GameStatus = None):
        pass

    def __init__(self):
        super().__init__()
        self.__data = EMPTY

from interface.IGameEndController import IGameEndController
from helpers.Constants import *


class GameEndController(IGameEndController):
    finished = False

    def __init__(self):
        super().__init__()

    def is_finished(self, data: str = EMPTY) -> bool:
        if str.upper(data) == EXIT:
            GameEndController.finished = True
        else:
            GameEndController.finished = False

import inspect
import logging

from controllers.LoggingController import LoggingController
from enums.Status import Status
from interface.IEvaluator import IEvaluator
from model.Effect import Effect
from model.GameStatus import GameStatus
from helpers.Constants import *


class StatusEvaluator(IEvaluator):
    @staticmethod
    def evaluate(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        game_status_tmp = StatusEvaluator.__evaluate_status(effect_tmp, game_status_tmp)
        return game_status_tmp

    def __init__(self):
        super().__init__()

    @staticmethod
    def __active(game_status_tmp: GameStatus = None, system_id: str = EMPTY):
        if game_status_tmp.name == system_id:
            game_status_tmp.status = Status.ACTIVE
        return game_status_tmp

    @staticmethod
    def __inactive(game_status_tmp: GameStatus = None, system_id: str = EMPTY):
        if game_status_tmp.name == system_id:
            game_status_tmp.status = Status.INACTIVE
        return game_status_tmp

    @staticmethod
    def __complete(game_status_tmp: GameStatus = None, system_id: str = EMPTY):
        if game_status_tmp.name == system_id:
            game_status_tmp.status = Status.COMPLETE
        return game_status_tmp

    @staticmethod
    def __incomplete(game_status_tmp: GameStatus = None, system_id: str = EMPTY):
        if game_status_tmp.name == system_id:
            game_status_tmp.status = Status.INCOMPLETE
        return game_status_tmp

    @staticmethod
    def __initiate(game_status_tmp: GameStatus = None, system_id: str = EMPTY):
        if game_status_tmp.name == system_id:
            game_status_tmp.status = Status.INITIATE
        return game_status_tmp

    @staticmethod
    def __terminate(game_status_tmp: GameStatus = None, system_id: str = EMPTY):
        if game_status_tmp.name == system_id:
            game_status_tmp.status = Status.TERMINATE
        return game_status_tmp

    __options = {
        "Active":       __active,
        "Inactive":     __inactive,
        "Complete":     __complete,
        "Incomplete":   __incomplete,
        "Initiate":     __initiate,
        "Terminate":    __terminate
    }

    @staticmethod
    def __evaluate_status(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        # verify size of elements in the condition
        if len(effect_tmp.list) == 2:
            status = effect_tmp.list[0]
            system_id = effect_tmp.list[1]
            if status in StatusEvaluator.__options:
                game_status_tmp = StatusEvaluator.__options[status].__func__(game_status_tmp, system_id)
        return game_status_tmp

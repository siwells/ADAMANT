import inspect
import logging

from controllers.LoggingController import LoggingController
from interface.IEvaluator import IEvaluator
from model.Condition import Condition
from model.GameStatus import GameStatus
from helpers.Constants import *


class PlayerEvaluator(IEvaluator):
    @staticmethod
    def evaluate(condition_tmp: Condition = None, game_status_tmp: GameStatus = None):
        evaluated = PlayerEvaluator.__check_player(condition_tmp, game_status_tmp)
        return evaluated

    def __init__(self):
        super().__init__()

    @staticmethod
    def __check_player(condition_tmp: Condition = None, game_status_tmp: GameStatus = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        evaluated_tmp = False
        # verify size of elements in the condition
        if len(condition_tmp.list) == 1:
            player_role = condition_tmp.list[0]
            # TODO don't think this is correct check
            if player_role == game_status_tmp.current_speaker:
                evaluated_tmp = True
        return evaluated_tmp

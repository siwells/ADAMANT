import inspect
import logging

from controllers.LoggingController import LoggingController
from interface.IEvaluator import IEvaluator
from model.Condition import Condition
from model.GameStatus import GameStatus
from helpers.Constants import *


class RelationEvaluator(IEvaluator):
    @staticmethod
    def evaluate(condition_tmp: Condition = None, game_status_tmp: GameStatus = None):
        evaluated = False
        return evaluated

    def __init__(self):
        super().__init__()

    @staticmethod
    def __backing(first_content: str = EMPTY, second_content: str = EMPTY):
        evaluated_tmp = False
        return evaluated_tmp

    @staticmethod
    def __warrant(first_content: str = EMPTY, second_content: str = EMPTY):
        evaluated_tmp = False
        return evaluated_tmp

    __options = {
        "Backing":  __backing,
        "Warrant":  __warrant
    }

    @staticmethod
    def __check_relation(condition_tmp: Condition = None, game_status_tmp: GameStatus = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        evaluated_tmp = False
        # verify size of elements in the condition
        if len(condition_tmp.list) == 3:
            first_content = condition_tmp.list[0]
            condition = condition_tmp.list[1]
            second_content = condition_tmp.list[2]
            if condition in RelationEvaluator.__options:
                evaluated_tmp = RelationEvaluator.__options[condition].__func__(first_content, second_content)
        return evaluated_tmp

import inspect
import logging

from controllers.LoggingController import LoggingController
from interface.IEvaluator import IEvaluator
from model.Effect import Effect
from model.GameStatus import GameStatus
from helpers.Constants import *


class ExternalEffectEvaluator(IEvaluator):
    @staticmethod
    def evaluate(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        game_status_tmp = ExternalEffectEvaluator.__evaluate_external(effect_tmp, game_status_tmp)
        return game_status_tmp

    def __init__(self):
        super().__init__()

    @staticmethod
    def __evaluate_external(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return game_status_tmp

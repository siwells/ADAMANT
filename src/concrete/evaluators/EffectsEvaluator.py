import inspect
import logging

from concrete.evaluators.effects_evaluators.AssignEvaluator import AssignEvaluator
from concrete.evaluators.effects_evaluators.ExternalEffectEvaluator import ExternalEffectEvaluator
from concrete.evaluators.effects_evaluators.MoveEvaluator import MoveEvaluator
from concrete.evaluators.effects_evaluators.StatusEvaluator import StatusEvaluator
from concrete.evaluators.effects_evaluators.StoreEvaluator import StoreEvaluator
from controllers.LoggingController import LoggingController
from interface.IEvaluator import IEvaluator
from model.Effect import Effect
from helpers.Constants import *
from model.GameStatus import GameStatus


class EffectsEvaluator(IEvaluator):
    @staticmethod
    def evaluate(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        effect = str(effect_tmp.name)
        if effect in EffectsEvaluator.__options:
            game_status_tmp = EffectsEvaluator.__options[effect].__func__(effect_tmp, game_status_tmp)
        return game_status_tmp

    def __init__(self):
        super().__init__()

    @staticmethod
    def __move(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        game_status_tmp = MoveEvaluator.evaluate(effect_tmp, game_status_tmp)
        return game_status_tmp

    @staticmethod
    def __store(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        game_status_tmp = StoreEvaluator.evaluate(effect_tmp, game_status_tmp)
        return game_status_tmp

    @staticmethod
    def __status(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        game_status_tmp = StatusEvaluator.evaluate(effect_tmp, game_status_tmp)
        return game_status_tmp

    @staticmethod
    def __assign(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        game_status_tmp = AssignEvaluator.evaluate(effect_tmp, game_status_tmp)
        return game_status_tmp

    @staticmethod
    def __ext_effect(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        game_status_tmp = ExternalEffectEvaluator.evaluate(effect_tmp, game_status_tmp)
        return game_status_tmp

    __options = {
        "Move":         __move,
        "Store":        __store,
        "Status":       __status,
        "Assign":       __assign,
        "ExtEffect":    __ext_effect
    }
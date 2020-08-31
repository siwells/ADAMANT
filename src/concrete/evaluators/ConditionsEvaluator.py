import inspect
import logging

from concrete.evaluators.condition_evaluators.CorrespondsEvaluator import CorrespondsEvaluator
from concrete.evaluators.condition_evaluators.EventEvaluator import EventEvaluator
from concrete.evaluators.condition_evaluators.ExternalConditionEvaluator import ExternalConditionEvaluator
from concrete.evaluators.condition_evaluators.InroleEvaluator import InroleEvaluator
from concrete.evaluators.condition_evaluators.InspectEvaluator import InspectEvaluator
from concrete.evaluators.condition_evaluators.MagnitudeEvaluator import MagnitudeEvaluator
from concrete.evaluators.condition_evaluators.NumTurnsEvaluator import NumTurnsEvaluator
from concrete.evaluators.condition_evaluators.PlayerEvaluator import PlayerEvaluator
from concrete.evaluators.condition_evaluators.RelationEvaluator import RelationEvaluator
from concrete.evaluators.condition_evaluators.SizeEvaluator import SizeEvaluator
from controllers.LoggingController import LoggingController
from interface.IEvaluator import IEvaluator
from model.Condition import Condition
from helpers.Constants import *
from model.GameStatus import GameStatus


class ConditionsEvaluator(IEvaluator):
    @staticmethod
    def evaluate(condition_tmp: Condition = None, game_status_tmp: GameStatus = None):
        """

        :param condition_tmp: Condition
        :param game_status_tmp: GameStatus
        :return: bool
        """
        evaluated = False
        condition_name = str(condition_tmp.name)
        if condition_name in ConditionsEvaluator.__options:
            evaluated = ConditionsEvaluator.__options[condition_name].__func__(condition_tmp, evaluated, game_status_tmp)
        return evaluated

    def __init__(self):
        super().__init__()

    @staticmethod
    def __event(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        evaluated_tmp = EventEvaluator.evaluate(condition_tmp, game_status_tmp)
        return evaluated_tmp

    @staticmethod
    def __inspect(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        evaluated_tmp = InspectEvaluator.evaluate(condition_tmp, game_status_tmp)
        return evaluated_tmp

    @staticmethod
    def __inrole(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        evaluated_tmp = InroleEvaluator.evaluate(condition_tmp, game_status_tmp)
        return evaluated_tmp

    @staticmethod
    def __size(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        evaluated_tmp = SizeEvaluator.evaluate(condition_tmp, game_status_tmp)
        return evaluated_tmp

    @staticmethod
    def __magnitude(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        evaluated_tmp = MagnitudeEvaluator.evaluate(condition_tmp, game_status_tmp)
        return evaluated_tmp

    @staticmethod
    def __numturns(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        evaluated_tmp = NumTurnsEvaluator.evaluate(condition_tmp, game_status_tmp)
        return evaluated_tmp

    @staticmethod
    def __corresponds(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        evaluated_tmp = CorrespondsEvaluator.evaluate(condition_tmp, game_status_tmp)
        return evaluated_tmp

    @staticmethod
    def __relation(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        evaluated_tmp = RelationEvaluator.evaluate(condition_tmp, game_status_tmp)
        return evaluated_tmp

    @staticmethod
    def __player(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        evaluated_tmp = PlayerEvaluator.evaluate(condition_tmp, game_status_tmp)
        return evaluated_tmp

    @staticmethod
    def __external(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        evaluated_tmp = ExternalConditionEvaluator.evaluate(condition_tmp, game_status_tmp)
        return evaluated_tmp

    __options = {
        "Event":        __event,
        "Inspect":      __inspect,
        "Inrole":       __inrole,
        "Size":         __size,
        "Magnitude":    __magnitude,
        "Numturns":     __numturns,
        "Corresponds":  __corresponds,
        "Relation":     __relation,
        "Player":       __player,
        "ExtCondition": __external
    }

import inspect
import logging

from controllers.LoggingController import LoggingController
from interface.IEvaluator import IEvaluator
from model.Condition import Condition
from model.GameStatus import GameStatus
from model.Store import Store
from helpers.Constants import *


class MagnitudeEvaluator(IEvaluator):
    @staticmethod
    def evaluate(condition_tmp: Condition = None, game_status_tmp: GameStatus = None):
        evaluated = MagnitudeEvaluator.__check_magnitude(condition_tmp, game_status_tmp)
        return evaluated

    def __init__(self):
        super().__init__()

    @staticmethod
    def __greater(first_store: Store = None, second_store: Store = None):
        if len(first_store.store) > len(second_store.store):
            evaluated_tmp = True
        else:
            evaluated_tmp = False
        return evaluated_tmp

    @staticmethod
    def __smaller(first_store: Store = None, second_store: Store = None):
        if len(first_store.store) < len(second_store.store):
            evaluated_tmp = True
        else:
            evaluated_tmp = False
        return evaluated_tmp

    @staticmethod
    def __equal(first_store: Store = None, second_store: Store = None):
        if len(first_store.store) == len(second_store.store):
            evaluated_tmp = True
        else:
            evaluated_tmp = False
        return evaluated_tmp

    @staticmethod
    def __non_equal(first_store: Store = None, second_store: Store = None):
        if len(first_store.store) != len(second_store.store):
            evaluated_tmp = True
        else:
            evaluated_tmp = False
        return evaluated_tmp

    __options = {
        "Greater": __greater,
        "Smaller": __smaller,
        "Equal": __equal,
        "!Equal": __non_equal
    }

    @staticmethod
    def __check_magnitude(condition_tmp: Condition = None, game_status_tmp: GameStatus = None):
        evaluated = False
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        # verify size of elements in the condition
        if len(condition_tmp.list) == 5:
            first_store_name = condition_tmp.list[0]
            first_owner_name = condition_tmp.list[1]
            comparator = condition_tmp.list[2]
            second_store_name = condition_tmp.list[3]
            second_owner_name = condition_tmp.list[4]
            first_store = None
            second_store = None
            for store in game_status_tmp.stores:
                if store.name == first_store_name and first_owner_name in store.owner:
                    first_store = store
                elif store.name == second_store_name and second_owner_name in store.owner:
                    second_store = store
            # check if stores are in game
            if first_store is not None and second_store is not None:
                if comparator in MagnitudeEvaluator.__options:
                    evaluated = MagnitudeEvaluator.__options[comparator].__func__(first_store, second_store)
        return evaluated

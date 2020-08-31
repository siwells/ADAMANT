import inspect
import logging

from controllers.LoggingController import LoggingController
from interface.IEvaluator import IEvaluator
from model.Condition import Condition
from model.GameStatus import GameStatus
from helpers.Constants import *
from model.Store import Store


class SizeEvaluator(IEvaluator):
    @staticmethod
    def evaluate(condition_tmp: Condition = None, game_status_tmp: GameStatus = None):
        evaluated = SizeEvaluator.__check_size(condition_tmp, game_status_tmp)
        return evaluated

    def __init__(self):
        super().__init__()

    @staticmethod
    def __check_size(condition_tmp: Condition = None, game_status_tmp: GameStatus = None):
        evaluated = False
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name) + " " + str(condition_tmp.list))
        # verify size of elements in the condition
        if len(condition_tmp.list) == 3:
            first_element = condition_tmp.list[0]
            player_name = condition_tmp.list[1]
            third_element = condition_tmp.list[2]
            # first_element supplied refers to store
            if any(x for x in game_status_tmp.stores if x.name == first_element):
                for store in game_status_tmp.stores:
                    if store.name == first_element and player_name in store.owner:
                        if third_element in SizeEvaluator.__options:
                            evaluated = SizeEvaluator.__options[third_element].__func__(store)
            # first_element supplied refers to legal moves
            elif any(x for x in game_status_tmp.moves if x.name == first_element):
                # TODO verify with Simon what he meant by LegalMoves?
                evaluated = SizeEvaluator.__number(game_status_tmp, third_element)
                pass
        return evaluated

    @staticmethod
    def __empty(player_store_tmp: Store = None):
        if len(player_store_tmp.store) <= 0:
            evaluated_tmp = True
        else:
            evaluated_tmp = False
        return evaluated_tmp

    @staticmethod
    def __non_empty(player_store_tmp: Store = None):
        if len(player_store_tmp.store) > 0:
            evaluated_tmp = True
        else:
            evaluated_tmp = False
        return evaluated_tmp

    @staticmethod
    def __number(game_status_tmp: GameStatus = None, number_tmp: int = -1, player_name_tmp: str = EMPTY):
        if game_status_tmp.available_moves == number_tmp and game_status_tmp.current_speaker == player_name_tmp:
            evaluated_tmp = True
        else:
            evaluated_tmp = False
        return evaluated_tmp

    __options = {
        "Empty": __empty,
        "!Empty": __non_empty
    }

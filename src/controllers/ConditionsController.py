import logging

from concrete.evaluators.ConditionsEvaluator import ConditionsEvaluator
from concrete.evaluators.EffectsEvaluator import EffectsEvaluator
from controllers.LoggingController import LoggingController
from helpers.Helpers import Helpers
from interface.IHandler import IHandler
from model.GameStatus import GameStatus
from enums.HandlerType import HandlerType
from helpers.Constants import *
import pprint

from model.Move import Move


# TODO gather not evaluated and return them
class ConditionsController(IHandler):
    def update_collector(self, game_status_tmp: GameStatus = None):
        game_status_tmp.speakers = game_status_tmp.get_speakers()
        return game_status_tmp

    def update_flag(self):
        pass

    def type(self):
        return HandlerType.PRE_MOVE_CHECK

    def handle(self, game_status_tmp: GameStatus = None):
        game_status_tmp = ConditionsController.evaluate_conditions_controller(game_status_tmp)
        game_status_tmp = self.update_collector(game_status_tmp)
        return game_status_tmp, None

    def __init__(self):
        super().__init__()

    @staticmethod
    def evaluate_conditions_controller(game_status_tmp: GameStatus = None):
        if len(game_status_tmp.mandatory_moves) > 0:
            # check conditions for that move
            for key in game_status_tmp.mandatory_moves:
                game_status_tmp.mandatory_moves[key] = ConditionsController. \
                    __get_interaction_moves_with_failed_conditions(game_status_tmp.mandatory_moves[key],
                                                                   game_status_tmp)
        if len(game_status_tmp.available_moves) > 0:
            # check conditions for that move
            for key in game_status_tmp.available_moves:
                game_status_tmp.available_moves[key] = ConditionsController. \
                    __get_interaction_moves_with_failed_conditions(game_status_tmp.available_moves[key],
                                                                   game_status_tmp)
        return game_status_tmp

    @staticmethod
    def __evaluate_condition(move: Move = None, game_status_tmp: GameStatus = None):
        all_conditions_satisfied = True
        if move is not None:
            for condition in move.conditions:
                # check condition setting all_conditions_satisfied to false if one of them fails
                all_conditions_satisfied = ConditionsEvaluator.evaluate(condition, game_status_tmp)
                if not all_conditions_satisfied:
                    # one of the conditions has not been met - break out
                    break
        return all_conditions_satisfied

    @staticmethod
    def __are_all_conditions_satisfied(move: Move,
                                       game_status_tmp: GameStatus) -> bool:
        all_conditions_satisfied = True
        if len(move.conditions) > 0:
            all_conditions_satisfied = ConditionsController.__evaluate_condition(move, game_status_tmp)
        return all_conditions_satisfied

    @staticmethod
    def __get_interaction_moves_with_failed_conditions(interaction_move_list: [], game_status_tmp: GameStatus) -> []:
        interaction_moves_not_meeting_conditions = []
        if len(interaction_move_list) > 0:
            for interaction_move in interaction_move_list:
                move = Helpers.get_move_from_interaction_move(interaction_move, game_status_tmp)
                if move is not None:
                    if not ConditionsController.__are_all_conditions_satisfied(move, game_status_tmp):
                        interaction_moves_not_meeting_conditions.append(interaction_move)
        return [x for x in interaction_move_list if x not in interaction_moves_not_meeting_conditions]

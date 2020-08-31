import inspect
import logging

from concrete.artifacts.Argument import Argument
from concrete.artifacts.Content import Content
from concrete.artifacts.Locution import Locution
from controllers.LoggingController import LoggingController
from helpers.Helpers import Helpers
from interface.IEvaluator import IEvaluator
from model.Effect import Effect
from model.GameStatus import GameStatus
from helpers.Constants import *
from model.InteractionMove import InteractionMove


class MoveEvaluator(IEvaluator):
    @staticmethod
    def evaluate(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        # game_status_tmp.clear_init_moves_dicts()
        game_status_tmp = MoveEvaluator.__evaluate_move(effect_tmp, game_status_tmp)
        return game_status_tmp

    def __init__(self):
        super().__init__()

    @staticmethod
    def __permit(game_status_tmp: GameStatus = None, data_tmp: {} = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        allowable_move = InteractionMove(moveName=data_tmp['move_name'], artifact=data_tmp['artifact'],
                                         playerName=data_tmp['player'], role=data_tmp['role'])
        if data_tmp['which_move'] in MoveEvaluator.__options:
            game_status_tmp = MoveEvaluator.__options[data_tmp['which_move']].__func__(game_status_tmp, allowable_move,
                                                                                       allowable=True)
        return game_status_tmp

    @staticmethod
    def __mandate(game_status_tmp: GameStatus = None, data_tmp: {} = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        required_move = InteractionMove(moveName=data_tmp['move_name'], artifact=data_tmp['artifact'],
                                        playerName=data_tmp['player'], role=data_tmp['role'])
        if data_tmp['which_move'] in MoveEvaluator.__options:
            game_status_tmp = MoveEvaluator.__options[data_tmp['which_move']].__func__(game_status_tmp, required_move,
                                                                                       allowable=False)
        return game_status_tmp

    @staticmethod
    def __next(game_status_tmp: GameStatus = None, interaction_move: InteractionMove = None, allowable: bool = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        if allowable:
            game_status_tmp.available_moves[NEXT].append(interaction_move)
        else:
            game_status_tmp.mandatory_moves[NEXT].append(interaction_move)
        return game_status_tmp

    @staticmethod
    def __not_next(game_status_tmp: GameStatus = None, interaction_move: InteractionMove = None,
                   allowable: bool = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        if allowable:
            game_status_tmp.available_moves[NOT_NEXT].append(interaction_move)
        else:
            game_status_tmp.mandatory_moves[NOT_NEXT].append(interaction_move)
        return game_status_tmp

    @staticmethod
    def __future(game_status_tmp: GameStatus = None, interaction_move: InteractionMove = None, allowable: bool = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        if allowable:
            game_status_tmp.available_moves[FUTURE].append(interaction_move)
        else:
            game_status_tmp.mandatory_moves[FUTURE].append(interaction_move)
        return game_status_tmp

    @staticmethod
    def __not_future(game_status_tmp: GameStatus = None, interaction_move: InteractionMove = None,
                     allowable: bool = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        if allowable:
            game_status_tmp.available_moves[NOT_FUTURE].append(interaction_move)
        else:
            game_status_tmp.mandatory_moves[NOT_FUTURE].append(interaction_move)
        return game_status_tmp

    __options = {
        "Permit": __permit,
        "Mandate": __mandate,
        "Next": __next,
        "!Next": __not_next,
        "Future": __future,
        "!Future": __not_future
    }

    @staticmethod
    def __evaluate_move(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        # verify size of elements in the condition
        if len(effect_tmp.list) >= 3:
            permit_mandate = effect_tmp.list[0]
            which_move = effect_tmp.list[1]
            move_name = effect_tmp.list[2]
            fourth_element = None
            artifact = None
            player = None
            role = None
            if len(effect_tmp.list) == 4:
                fourth_element = effect_tmp.list[3]
                if Helpers.is_player(game_status_tmp, fourth_element):
                    player = fourth_element
                elif Helpers.is_role(game_status_tmp, fourth_element):
                    role = fourth_element
                if player is None and role is None:
                    artifact = fourth_element
            elif len(effect_tmp.list) == 5:
                artifact = effect_tmp.list[3]
                player_or_role = effect_tmp.list[4]
                if Helpers.is_player(game_status_tmp, player_or_role):
                    player = fourth_element
                elif Helpers.is_role(game_status_tmp, player_or_role):
                    role = fourth_element
            data = {'permit_mandate': permit_mandate, 'which_move': which_move, 'move_name': move_name,
                    'artifact': artifact, 'player': player, 'role': role}
            if permit_mandate in MoveEvaluator.__options:
                game_status_tmp = MoveEvaluator.__options[permit_mandate].__func__(game_status_tmp, data)
        return game_status_tmp


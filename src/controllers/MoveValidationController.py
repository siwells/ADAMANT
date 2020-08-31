import logging

from concrete.GameEndController import GameEndController
from controllers.LoggingController import LoggingController
from exception.ExceptionHandler import ExceptionHandler
from interface.IHandler import IHandler
from enums.HandlerType import HandlerType
from model.GameStatus import GameStatus
from helpers.Constants import *
from controllers.MoveController import MoveController


class MoveValidationController(IHandler):
    def update_collector(self, game_status_tmp: GameStatus = None):
        if game_status_tmp.last_interaction_move:
            game_status_tmp = game_status_tmp.assign_speaker_assign_listener()
            game_status_tmp.speakers = game_status_tmp.get_speakers()
            game_status_tmp.current_speaker = game_status_tmp.last_interaction_move.playerName
            game_status_tmp.set_last_move_by_name(game_status_tmp.last_interaction_move.moveName)
            game_status_tmp.past_moves.append(game_status_tmp.last_interaction_move)
            game_status_tmp.set_did_move_flag(game_status_tmp.current_speaker)
            game_status_tmp.remove_interaction_move_from_moves(game_status_tmp.last_interaction_move)
            game_status_tmp.initial_turn = False
            game_status_tmp.clear_init_moves_dicts()
        else:
            LoggingController.logger.warning(
                "game_status_tmp.last_interaction_move: None\n\tLast move could not be parsed")
            GameEndController.finished = True
        return game_status_tmp

    def update_flag(self):
        pass

    def type(self):
        return HandlerType.POST_MOVE_CHECK

    def handle(self, game_status_tmp: GameStatus = None):
        valid = MoveValidationController.__validate(game_status_tmp)
        if not valid:
            details = {"player_expected": game_status_tmp.get_speakers(),
                       "player_got": game_status_tmp.last_interaction_move.playerName,
                       "moves_expected": {"mandatory": [x.moveName for x in game_status_tmp.mandatory_moves[NEXT]],
                                          "available": [x.moveName for x in game_status_tmp.available_moves[NEXT]]},
                       "move_got": game_status_tmp.last_interaction_move.moveName}
            return None, ExceptionHandler("INVALID_MOVE", 400, payload=details)
        game_status_tmp = self.update_collector(game_status_tmp)
        self.update_flag()
        LoggingController.logger.debug("Handling in: " + str(type(self)))
        return game_status_tmp, None

    def __init__(self):
        super().__init__()

    @staticmethod
    def __validate(game_status_tmp: GameStatus = None):
        valid = False
        if game_status_tmp.last_interaction_move:
            # check mandatory moves first
            if len(game_status_tmp.mandatory_moves) > 0:
                # check by move_id
                for key in game_status_tmp.mandatory_moves:
                    for interaction_move in game_status_tmp.mandatory_moves[key]:
                        if key in [NOT_NEXT,
                                   NOT_FUTURE] and interaction_move.moveName == game_status_tmp.last_interaction_move.moveName:
                            valid = False
                            break
                        if interaction_move.moveName == game_status_tmp.last_interaction_move.moveName:
                            # need to check if Speaker or player_name correct just to be sure
                            if game_status_tmp.last_interaction_move.playerName in game_status_tmp.speakers:
                                valid = True
                                break
                    if valid:
                        break
            # check available moves
            if len(game_status_tmp.available_moves) > 0:
                # check by move_id
                for key in game_status_tmp.available_moves:
                    for interaction_move in game_status_tmp.available_moves[key]:
                        if key in [NOT_NEXT,
                                   NOT_FUTURE] and interaction_move.moveName == game_status_tmp.last_interaction_move.moveName:
                            valid = False
                            break
                        if interaction_move.moveName == game_status_tmp.last_interaction_move.moveName:
                            # need to check if Speaker or player_name correct just to be sure
                            if game_status_tmp.last_interaction_move.playerName in game_status_tmp.speakers:
                                valid = True
                                break
                    if valid:
                        break
        return valid

import inspect
import logging

from controllers.LoggingController import LoggingController
from interface.IEvaluator import IEvaluator
from model.Condition import Condition
from model.GameStatus import GameStatus
from helpers.Constants import *


class InroleEvaluator(IEvaluator):
    @staticmethod
    def evaluate(condition_tmp: Condition = None, game_status_tmp: GameStatus = None):
        evaluated = InroleEvaluator.__check_inrole(condition_tmp, game_status_tmp)
        return evaluated

    def __init__(self):
        super().__init__()

    @staticmethod
    def __check_inrole(condition_tmp: Condition = None, game_status_tmp: GameStatus = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        match = False
        # check number of parameters supplied
        if len(condition_tmp.list) == 1:
            parameter = condition_tmp.list[0]
            player = game_status_tmp.players.get_player_by_name(parameter)
            if player is not None:
                if player.name in game_status_tmp.get_speakers():
                    match = True
                else:
                    match = False
            else:
                match = True
                speakers = game_status_tmp.get_speakers()
                for speaker in speakers:
                    player = game_status_tmp.players.get_player_by_name(speaker)
                    role = parameter
                    if role not in player.roles:
                        match = False
                        break
        return match

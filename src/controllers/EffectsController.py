import inspect
import logging
import logging.config

from concrete.evaluators.EffectsEvaluator import EffectsEvaluator
from controllers.LoggingController import LoggingController
from interface.IHandler import IHandler
from enums.HandlerType import HandlerType
from model.Effect import Effect
from model.GameStatus import GameStatus
from helpers.Constants import *


class EffectsController(IHandler):

    def update_collector(self, game_status_tmp: GameStatus = None):
        return game_status_tmp

    def update_flag(self):
        pass

    def type(self):
        return HandlerType.POST_MOVE_CHECK

    def __init__(self):
        super().__init__()

    def handle(self, game_status_tmp: GameStatus = None):
        if game_status_tmp is None:
            return game_status_tmp, None
        game_status_tmp = EffectsController.__evaluate_effects(game_status_tmp)
        game_status_tmp = self.update_collector(game_status_tmp)
        self.update_flag()
        return game_status_tmp, None

    @staticmethod
    def __evaluate_effects(game_status_tmp: GameStatus):
        if game_status_tmp.last_move:
            if len(game_status_tmp.last_move.effects) > 0:
                for effect in game_status_tmp.last_move.effects:
                    if effect.name in EffectsController.__options:
                        effect = EffectsController.__options[effect.name].__func__(effect, game_status_tmp)
                        game_status_tmp = EffectsEvaluator.evaluate(effect, game_status_tmp)
        return game_status_tmp

    @staticmethod
    def __move(effect_tmp: Effect, game_status_tmp: GameStatus):
        player_name = game_status_tmp.last_interaction_move.playerName
        role = game_status_tmp.last_interaction_move.role
        artifact = game_status_tmp.last_interaction_move.artifact
        length = len(effect_tmp.list)
        if length == 4:
            effect_tmp.list[3] = artifact
        elif length == 5:
            effect_tmp.list[3] = artifact
            if player_name is not None and player_name != EMPTY:
                effect_tmp.list[4] = player_name
            elif role is not None and role != EMPTY:
                effect_tmp.list[4] = role
        return effect_tmp

    @staticmethod
    def __store(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        effect_tmp.list[1] = game_status_tmp.last_interaction_move.artifact
        game_store = effect_tmp.list[2]
        player_name = game_status_tmp.last_interaction_move.playerName
        role = game_status_tmp.last_interaction_move.role
        player_or_role = EMPTY
        found = False
        for store in game_status_tmp.stores:
            if store.name == game_store:
                for owner in store.owner:
                    if owner == player_name:
                        player_or_role = player_name
                        found = True
                        break
                    elif owner == role:
                        player_or_role = role
                        found = True
                        break
                if found:
                    break
        effect_tmp.list[3] = player_or_role
        return effect_tmp

    @staticmethod
    def __status(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        LoggingController.logger.debug(("Evaluating: " + str(inspect.currentframe().f_code.co_name)))
        # this implementation is only needed if ever contents of 'status' would change
        return effect_tmp

    @staticmethod
    def __assign(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        LoggingController.logger.debug(("Evaluating: " + str(inspect.currentframe().f_code.co_name)))
        # this implementation is only needed if ever contents of 'status' would change
        return effect_tmp

    @staticmethod
    def __ext_effect(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        LoggingController.logger.debug(("Evaluating: " + str(inspect.currentframe().f_code.co_name)))
        # this implementation is only needed if ever contents of 'status' would change
        return effect_tmp

    __options = {
        "Move": __move,
        "Store": __store,
        "Status": __status,
        "Assign": __assign,
        "ExtEffect": __ext_effect
    }

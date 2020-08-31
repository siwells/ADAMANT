import logging

from concrete.GameEndController import GameEndController
from controllers.LoggingController import LoggingController
from controllers.OutputController import OutputController
from enums.Status import Status
from interface.IGameDataCollector import IGameDataCollector
from interface.IHandler import IHandler
from model.GameStatus import GameStatus
from controllers.ConditionsController import ConditionsController
from controllers.EffectsController import EffectsController
from controllers.StoreController import StoreController
from controllers.RulesController import RulesController
from controllers.MoveController import MoveController
from controllers.MoveValidationController import MoveValidationController
from controllers.TranscriptController import TranscriptController
from helpers.Constants import *
from model.Game import Game
from controllers.TurnsController import TurnsController


class GameStatusCollector(IGameDataCollector):
    def collect(self, i_handler: IHandler = None):
        err = None
        if i_handler is None:
            # TODO differentiate between HandlerTypes
            for handler in self.__handlers:
                self.game_status, err = handler.handle(self.game_status)
                if self.game_status is None and err is not None:
                    return self.game_status, err
                self.game_status.evaluate_game_status()
        else:
            if isinstance(i_handler, IHandler):
                self.game_status = i_handler.handle(self.game_status)
                self.game_status.evaluate_game_status()
        if self.game_status.status == Status.TERMINATE:
            GameEndController.finished = True
        return self.game_status, err

    def __init__(self, game_tmp: Game = None, game_status: GameStatus = None, dialogueId: str = None):
        super().__init__()
        if game_status is not None:
            self.game_status = game_status
        else:
            self.game_status = GameStatus(game_tmp, dialogueId=dialogueId)
        self.__turns_controller = TurnsController()
        self.__conditions_controller = ConditionsController()
        self.__effects_controller = EffectsController()
        self.__store_controller = StoreController()
        self.__rules_controller = RulesController()
        self.__output_controller = OutputController()
        self.__move_controller = MoveController()
        self.__move_validation_controller = MoveValidationController()
        self.__transcript_controller = TranscriptController()
        self.__handlers = [self.__turns_controller, self.__rules_controller, self.__conditions_controller,self.__move_controller, self.__move_validation_controller, self.__effects_controller,
                           self.__store_controller, self.__transcript_controller, self.__output_controller
                           ]

    def __get_game_status(self) -> GameStatus:
        return self.__game_status

    def __set_game_status(self, game_status_tmp: GameStatus = None):
        self.__game_status = game_status_tmp

    game_status = property(__get_game_status, __set_game_status, None)

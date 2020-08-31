import logging

from controllers.LoggingController import LoggingController
from interface.IHandler import IHandler
from enums.HandlerType import HandlerType
from model.GameStatus import GameStatus
from helpers.Constants import *
import pprint


class StoreController(IHandler):
    def update_collector(self, game_status_tmp: GameStatus = None):
        return game_status_tmp

    def update_flag(self):
        pass

    def type(self):
        return HandlerType.POST_MOVE_CHECK

    def __init__(self):
        super().__init__()

    def handle(self, game_status_tmp: GameStatus = None):
        game_status_tmp = self.update_collector(game_status_tmp)
        self.update_flag()
        self.__log_details(game_status_tmp)
        return game_status_tmp, None

    def __log_details(self, game_status_tmp: GameStatus = None):
        logger = ''
        logger += ("Handling in: " + str(type(self))) + "\n"
        for store in game_status_tmp.stores:
            logger += pprint.pformat(vars(store)) + "\n"
            for artifact in store.store:
                logger += pprint.pformat(vars(artifact)) + "\n"
        LoggingController.logger.debug(logger)

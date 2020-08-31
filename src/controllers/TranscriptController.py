import logging
import logging.config

from flask import json

from Application import db_controller
from controllers.LoggingController import LoggingController
from interface.IHandler import IHandler
from enums.HandlerType import HandlerType
from model.GameStatus import GameStatus
from helpers.Constants import *
from serializers.Serializer import GameStatusSerializer


class TranscriptController(IHandler):
    def update_collector(self, game_status_tmp: GameStatus = None):
        dId = str(game_status_tmp.id)
        game_status_db = db_controller.session.query(GameStatus).filter_by(id=dId).first()
        serialized = GameStatusSerializer().serialize(game_status_tmp)
        game_status_tmp.gameStatusSerialized = json.dumps(serialized)
        if game_status_db is None:
            db_controller.session.add(game_status_tmp)
            db_controller.session.commit()
            return game_status_tmp
        # else update db model
        game_status_db.gameStatusSerialized = game_status_tmp.gameStatusSerialized
        db_controller.session.add(game_status_db)
        db_controller.session.commit()
        return game_status_tmp

    def update_flag(self):
        pass

    def type(self):
        return HandlerType.POST_MOVE_CHECK

    def handle(self, game_status_tmp: GameStatus = None):
        game_status_tmp = self.update_collector(game_status_tmp)
        self.update_flag()
        LoggingController.logger.debug("Handling in: " + str(type(self)))
        return game_status_tmp, None

    def __init__(self):
        super().__init__()

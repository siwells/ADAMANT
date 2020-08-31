from concrete.data_collectors.MoveCollector import MoveCollector
from controllers.LoggingController import LoggingController
from enums.HandlerType import HandlerType
from helpers import Constants
from interface.IHandler import IHandler
from model.GameStatus import GameStatus
from model.InteractionMove import InteractionMove
from serializers.Serializer import InteractionMoveSerializer


class MoveController(IHandler):
    def update_collector(self, game_status_tmp: GameStatus = None):
        """
        This only updates current speaker and last interaction move,
        last_move should only be updated after validation in MoveValidationController
        :param game_status_tmp:
        :return: GameStatus
        """
        if self.__interaction_move is not None:
            game_status_tmp.current_speaker = self.__interaction_move.playerName
            game_status_tmp.last_interaction_move = self.__interaction_move
        else:
            LoggingController.logger.warning("Most likely json invalid format or id returned none")
            raise Exception(Constants.WRONG_MESSAGE_FORMAT)
        return game_status_tmp

    def update_flag(self):
        pass

    def type(self):
        return HandlerType.MOVE

    def handle(self, game_status_tmp: GameStatus = None):
        move_str = self.__move_collector.collect()
        self.__interaction_move = self.__parse_move(move_str)
        game_status_tmp = self.update_collector(game_status_tmp)
        self.update_flag()
        return game_status_tmp, None

    def __init__(self):
        super().__init__()
        self.__move_collector = MoveCollector()
        self.__interaction_move = None

    @staticmethod
    def __parse_move(move_str: dict = None) -> InteractionMove:
        # decode json and create Move
        if type(move_str) is not dict:
            LoggingController.logger.warning("Invalid JSON format: " + str(move_str))
            raise Exception(400, Constants.WRONG_MESSAGE_FORMAT, move_str)
        else:
            move = InteractionMoveSerializer().deserialize(move_str)
        return move

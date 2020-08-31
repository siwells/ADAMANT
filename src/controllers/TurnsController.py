import logging

from concrete.GameEndController import GameEndController
from controllers.LoggingController import LoggingController
from enums.Ordering import Ordering
from enums.Status import Status
from interface.IHandler import IHandler
from helpers.Constants import *
from model.GameStatus import GameStatus
from enums.HandlerType import HandlerType
from enums.Magnitude import Magnitude
import controllers.GameController


class TurnsController(IHandler):
    def update_collector(self, game_status_tmp: GameStatus = None):
        game_status_tmp.new_turn = self.__evaluate_next_player_by_turns(game_status_tmp)
        game_status_tmp.speakers = game_status_tmp.get_speakers()
        if game_status_tmp.all_players_did_move:
            game_status_tmp.turns_counter += 1
        if game_status_tmp.turns.max is not None:
            if game_status_tmp.turns_counter >= game_status_tmp.turns.max:
                game_status_tmp.status = Status.TERMINATE
                GameEndController.finished = True
        return game_status_tmp

    def update_flag(self):
        pass

    def handle(self, game_status_tmp: GameStatus = None):
        game_status_tmp = self.update_collector(game_status_tmp)
        self.update_flag()
        LoggingController.logger.debug("Handling in: " + str(type(self)))
        LoggingController.logger.debug("Next player: " + str(game_status_tmp.new_turn))
        return game_status_tmp, None

    def type(self):
        return HandlerType.PRE_MOVE_CHECK

    def __init__(self):
        super().__init__()
        self.__multiple_moves_count = 0
        self.__initial = True

    def __get_turns_count(self) -> int:
        return self.__multiple_moves_count

    multiple_moves_count = property(__get_turns_count, None, None)

    def __turn_count_increment(self):
        self.__multiple_moves_count += 1

    # TODO in Ordering.LIBERAL there has to be a way to evaluate who is the next speaker
    def __evaluate_next_player_by_turns(self, game_status_tmp: GameStatus = None) -> bool:
        new_turn = False
        if controllers.GameController.GameController.game.turns.magnitude == Magnitude.SINGLE:
            new_turn = True
            if game_status_tmp.turns.ordering == Ordering.STRICT:
                game_status_tmp = game_status_tmp.assign_speaker_assign_listener()
            elif game_status_tmp.turns.ordering == Ordering.LIBERAL:
                # TODO implement Ordering.LIBERAL
                pass
        elif controllers.GameController.GameController.game.turns.magnitude == Magnitude.MULTIPLE:
            if game_status_tmp.max_moves_per_turn is not None:
                if self.multiple_moves_count >= game_status_tmp.max_moves_per_turn:
                    new_turn = True
                    if game_status_tmp.turns.ordering == Ordering.STRICT:
                        game_status_tmp = game_status_tmp.assign_speaker_assign_listener()
                    elif game_status_tmp.turns.ordering == Ordering.LIBERAL:
                        # TODO implement Ordering.LIBERAL
                        pass
                    self.__multiple_moves_count = 0
                else:
                    new_turn = False
                    self.__turn_count_increment()
            elif game_status_tmp.last_interaction_move is not None:
                if game_status_tmp.last_interaction_move.final:
                    new_turn = True
                    if game_status_tmp.turns.ordering == Ordering.STRICT:
                        game_status_tmp = game_status_tmp.assign_speaker_assign_listener()
                    elif game_status_tmp.turns.ordering == Ordering.LIBERAL:
                        # TODO implement Ordering.LIBERAL
                        pass
                else:
                    new_turn = False
        if game_status_tmp.all_players_did_move:
            self.__initial = False
        return new_turn

    def __assign_speaker_assign_listener(self, game_status_tmp: GameStatus = None):
        if game_status_tmp.last_interaction_move is None:
            return game_status_tmp
        next_player = game_status_tmp.get_next_player_name_from_the_list(game_status_tmp.last_interaction_move.playerName)
        if next_player is None:
            return game_status_tmp
        for player in game_status_tmp.players.list:
            if next_player == player.name:
                if SPEAKER not in player.roles:
                    if LISTENER in player.roles:
                        player.roles.remove(LISTENER)
                    player.roles.append(SPEAKER)
            else:
                if LISTENER not in player.roles:
                    if SPEAKER in player.roles:
                        player.roles.remove(SPEAKER)
                    player.roles.append(LISTENER)
        return game_status_tmp

import uuid

from sqlalchemy import Column, String

from model.Game import Game
from model.InteractionMove import InteractionMove
from model.Move import Move
from enums.Role import Role
from helpers.Constants import *
from enums.Status import Status
from settings.db_settings import Base


class GameStatus(Game, Base):

    __tablename__ = "GameStatus"

    id = Column(String, primary_key=True)
    dialogueId = Column(String)
    gameStatusSerialized = Column(String)

    def __init__(self, game_template: Game = None, id: str = None, dialogueId: str = None, turns_counter=0,
                 new_turn=False, initial_turn=True, speakers=None, current_speaker=EMPTY,
                 last_interaction_move=None, last_move=None,
                 available_moves=None,
                 mandatory_moves=None, past_moves=None,
                 all_players_did_move=False, status=None):
        super().__init__()
        if id is None:
            self.id = str(uuid.uuid4())
        else:
            self.id = id
        self.dialogueId = dialogueId
        self.__turns_counter = turns_counter
        self.__new_turn = new_turn
        self.__initial_turn = bool(initial_turn)
        if speakers is None:
            self.speakers = []
        else:
            self.speakers = speakers
        self.__current_speaker = current_speaker
        self.__last_interaction_move = last_interaction_move
        self.__last_move = last_move
        if available_moves is None:
            self.available_moves = {NEXT: [], NOT_NEXT: [], FUTURE: [], NOT_FUTURE: []}
        else:
            self.available_moves = available_moves
        if mandatory_moves is None:
            self.mandatory_moves = {NEXT: [], NOT_NEXT: [], FUTURE: [], NOT_FUTURE: []}
        else:
            self.mandatory_moves = mandatory_moves
        if past_moves is None:
            self.past_moves = []
        else:
            self.past_moves = past_moves
        self.__all_players_did_move = all_players_did_move
        self.__status = status
        if game_template is not None:
            self.name = game_template.name
            self.stores = game_template.stores
            self.turns = game_template.turns
            self.players = game_template.players
            self.roles = game_template.roles
            self.principles = game_template.principles
            self.moves = game_template.moves

    def set_game_template(self, game_template: Game):
        self.name = game_template.name
        self.stores = game_template.stores
        self.turns = game_template.turns
        self.players = game_template.players
        self.roles = game_template.roles
        self.principles = game_template.principles
        self.moves = game_template.moves

    def __set_new_turn(self, new_turn_tmp: bool = False):
        self.__new_turn = new_turn_tmp

    def __get_new_turn(self) -> bool:
        return self.__new_turn

    def __set_speakers(self, speakers_tmp: [] = None):
        self.__speakers = speakers_tmp

    def __get_speakers(self) -> []:
        return self.__speakers

    def __get_current_speaker(self) -> str:
        return self.__current_speaker

    def __set_current_speaker(self, speaker_tmp: str = None):
        self.__current_speaker = speaker_tmp

    def __get_current_speaker_moves(self) -> {}:
        return self.__available_moves

    def __set_current_speaker_moves(self, current_speaker_moves_tmp: {} = None):
        self.__available_moves = current_speaker_moves_tmp

    def __set_initial_turn(self, initial_tmp: bool = None):
        self.__initial_turn = initial_tmp

    def __get_initial_turn(self) -> bool:
        return self.__initial_turn

    def __set_all_players_did_move(self, flag_tmp: bool = None):
        self.__all_players_did_move = flag_tmp

    def __get_all_players_did_move(self) -> bool:
        return self.__all_players_did_move

    def __get_turns_counter(self) -> int:
        return self.__turns_counter

    def __set_turns_counter(self, counter_tmp: int = 0):
        self.__turns_counter = counter_tmp

    def __set_last_interaction_move(self, last_move_tmp: InteractionMove = None):
        self.__last_interaction_move = last_move_tmp

    def __get_last_interaction_move(self) -> InteractionMove:
        return self.__last_interaction_move

    def __set_last_move(self, last_move_tmp: Move = None):
        self.__last_move = last_move_tmp

    def __get_last_move(self) -> Move:
        return self.__last_move

    def __set_status(self, status_tmp: Status = None):
        self.__status = status_tmp

    def __get_status(self) -> Status:
        return self.__status

    def __get_mandatory_moves(self) -> {}:
        return self.__mandatory_moves

    def __set_mandatory_moves(self, mandatory_moves_tmp: {} = None):
        self.__mandatory_moves = mandatory_moves_tmp

    def __set_past_interaction_moves(self, moves_tmp: [] = None):
        self.__past_interaction_moves = moves_tmp

    def __get_past_interaction_moves(self) -> []:
        return self.__past_interaction_moves

    new_turn = property(__get_new_turn, __set_new_turn, None)
    speakers = property(__get_speakers, __set_speakers, None)
    current_speaker = property(__get_current_speaker, __set_current_speaker, None)
    available_moves = property(__get_current_speaker_moves, __set_current_speaker_moves, None)
    initial_turn = property(__get_initial_turn, __set_initial_turn, None)
    all_players_did_move = property(__get_all_players_did_move, __set_all_players_did_move, None)
    turns_counter = property(__get_turns_counter, __set_turns_counter)
    last_interaction_move = property(__get_last_interaction_move, __set_last_interaction_move, None)
    last_move = property(__get_last_move, __set_last_move, None)
    status = property(__get_status, __set_status, None)
    mandatory_moves = property(__get_mandatory_moves, __set_mandatory_moves, None)
    past_moves = property(__get_past_interaction_moves, __set_past_interaction_moves, None)

    def get_speakers(self) -> []:
        speakers = []
        for player in self.players.list:
            if Role.SPEAKER.name.title() in player.roles:
                speakers.append(player.name)
        return speakers

    def set_did_move_flag(self, current_speaker: str = None):
        for player in self.players.list:
            if player.name == current_speaker:
                player.did_move_flag = True
        self.all_players_did_move = self.__update_all_players_did_move_flag()

    def __update_all_players_did_move_flag(self):
        flag = True
        for player in self.players.list:
            if player.did_move_flag is False:
                flag = False
                break
        if flag:
            self.__turns_counter += 1
            # clear flag for all
            for player in self.players.list:
                player.did_move_flag = False
            if DEBUG:
                print("New turn: " + str(self.turns_counter))
        return flag

    def set_last_move_by_name(self, move_name: str = None):
        if move_name is not None:
            for move in self.moves:
                if move_name == move.name:
                    self.last_move = move
        elif DEBUG:
            print("Could not set last_move in GameStatus")

    def __is_max_turns(self) -> bool:
        value = False
        if hasattr(self.turns, 'max'):
            if self.turns.max is not None and self.turns.max > 0:
                value = True if (
                    self.turns.max - self.turns_counter <= 0) else False
        return value

    def evaluate_game_status(self):
        if self.__is_max_turns():
            self.__status = Status.TERMINATE

    def is_player_in_game(self, player_name: str = EMPTY):
        match = False
        for player in self.players.list:
            if player.name == player_name:
                match = True
        return match

    def clear_init_moves_dicts(self):
        self.available_moves.pop(NEXT, None)
        self.available_moves.pop(NOT_NEXT, None)
        self.mandatory_moves.pop(NEXT, None)
        self.mandatory_moves.pop(NOT_NEXT, None)
        self.available_moves = {NEXT: [], NOT_NEXT: [], FUTURE: [], NOT_FUTURE: []}
        self.mandatory_moves = {NEXT: [], NOT_NEXT: [], FUTURE: [], NOT_FUTURE: []}

    def get_next_player_name_from_the_list(self, player_name: str = EMPTY):
        value = None
        length = len(self.players.list)
        if length > 0:
            for player in self.players.list:
                if player.name == player_name:
                    index = self.players.list.index(player)
                    if index < length - 1:
                        value = self.players.list[index + 1].name
                    elif index == length - 1:
                        value = self.players.list[0].name
        return value

    def get_interaction_move__by_id(self, move_id: int = None):
        interaction_move = None
        if move_id is not None:
            found = False
            for key in self.mandatory_moves:
                for move in self.mandatory_moves[key]:
                    if int(move.move_id) == int(move_id):
                        interaction_move = move
                        found = True
                        break
                if found:
                    break
            if interaction_move is None:
                for key in self.available_moves:
                    for move in self.available_moves[key]:
                        if int(move.move_id) == int(move_id):
                            interaction_move = move
                            found = True
                            break
                    if found:
                        break
        return interaction_move

    def remove_interaction_move_from_moves(self, interaction_move: InteractionMove):
        for key in self.mandatory_moves:
            if interaction_move in self.mandatory_moves[key]:
                self.mandatory_moves[key].remove(interaction_move)
        for key in self.available_moves:
            if interaction_move in self.available_moves[key]:
                self.available_moves[key].remove(interaction_move)

    def assign_speaker_assign_listener(self):
        if self.last_interaction_move is None:
            return self
        next_player = self.get_next_player_name_from_the_list(self.last_interaction_move.playerName)
        if next_player is None:
            return self
        for player in self.players.list:
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
        return self

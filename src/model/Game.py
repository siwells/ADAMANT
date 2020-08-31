from model.Store import Store
from model.Turns import Turns
from model.Player import Player
from model.Players import Players
from model.Principle import Principle
from model.Move import Move


class Game:
    def __init__(self):
        self.__name = None
        self.__store = []
        self.__turns = Turns()
        self.__players = Players()
        self.__roles = []
        self.__principles = []
        self.__moves = []
        self.__max_moves = None

    def __set_name(self, name_tmp: str = None):
        self.__name = name_tmp

    def __get_name(self) -> str:
        return self.__name

    def __set_store(self, store_tmp: [] = None):
        self.__store = store_tmp

    def __get_store(self) -> []:
        return self.__store

    def __set_turns(self, turns_tmp: Turns = None):
        self.__turns = turns_tmp

    def __get_turns(self) -> Turns:
        return self.__turns

    def __set_players(self, players_tmp: Players = None):
        self.__players = players_tmp

    def __get_players(self) -> Players:
        return self.__players

    def __get_roles(self) -> []:
        return self.__roles

    def __set_roles(self, roles_tmp: [] = None):
        self.__roles = roles_tmp

    def __get_principles(self) -> []:
        return self.__principles

    def __set_principles(self, principles_tmp: [] = None):
        self.__principles = principles_tmp

    def __set_moves(self, moves_tmp: [] = None):
        self.__moves = moves_tmp

    def __get_moves(self) -> []:
        return self.__moves

    def __set_max_moves(self, max_tmp: int = None):
        self.__max_moves = max_tmp

    def __get_max_moves(self) -> int:
        return self.__max_moves

    name = property(__get_name, __set_name, None)
    stores = property(__get_store, __set_store, None)
    turns = property(__get_turns, __set_turns, None)
    players = property(__get_players, __set_players, None)
    roles = property(__get_roles, __set_roles, None)
    principles = property(__get_principles, __set_principles, None)
    moves = property(__get_moves, __set_moves, None)
    max_moves_per_turn = property(__get_max_moves, __set_max_moves, None)

    def print_self(self):
        print("Game started: " + self.name)

        print("Turns")
        print("\t" + str(self.turns.ordering))
        print("\t" + str(self.turns.magnitude))
        if hasattr(self.turns, 'max'):
            print("\t" + "Max: " + str(self.turns.max))

        print("Players min: " + str(self.players.min))
        print("Players max: " + str(self.players.max))
        print("Players: ")
        for player in self.players.list:
            print("\t" + player.name)
            print("\t" + str(player.roles))

        print("Stores")
        for store in self.stores:
            print("\t" + store.name)
            print("\t" + "Owners: " + str(store.owner))
            print("\t" + str(store.visibility))
            print("\t" + str(store.structure))

        print("Roles:")
        for role in self.roles:
            print("\t" + str(role))

        print("Principles:")
        for principle in self.principles:
            print("\t" + principle.name)
            print("\t" + str(principle.scope))
            for condition in principle.conditions:
                print("\t" + "\t" + condition.name)
                print("\t" + "\t" + str(condition.list))
            for effect in principle.effects:
                print("\t" + "\t" + effect.name)
                print("\t" + "\t" + str(effect.list))

        print("Moves:")
        for move in self.moves:
            print("\t" + move.name)
            print("\t" + "\t" + "Content: " + str(move.content.list))
            for condition in move.conditions:
                print("\t" + "\t" + condition.name)
                print("\t" + "\t" + str(condition.list))
            for effect in move.effects:
                print("\t" + "\t" + effect.name)
                print("\t" + "\t" + str(effect.list))
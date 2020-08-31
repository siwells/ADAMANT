from enums.Structure import Structure
from enums.Visibility import Visibility
from collections import deque


class Store:
    def __init__(self):
        self.__structure = None
        self.__visibility = None
        self.__name = None
        self.__owner = []
        self.__store = []

    def __set_structure(self, structure_tmp: Structure = None):
        if structure_tmp == str.lower(Structure.SET.name):
            self.__structure = Structure.SET
        elif structure_tmp == str.lower(Structure.QUEUE.name):
            self.__structure = Structure.QUEUE
        elif structure_tmp == str.lower(Structure.STACK.name):
            self.__structure = Structure.STACK

    def __get_structure(self) -> Structure:
        return self.__structure

    def __set_visibility(self, visibility_tmp: Visibility = None):
        if visibility_tmp == str.lower(Visibility.PRIVATE.name):
            self.__visibility = Visibility.PRIVATE
        elif visibility_tmp == str.lower(Visibility.PUBLIC.name):
            self.__visibility = Visibility.PUBLIC

    def __get_visibility(self) -> Visibility:
        return self.__visibility

    def __set_name(self, name_tmp: str = None):
        self.__name = name_tmp

    def __get_name(self) -> str:
        return self.__name

    def __set_owner(self, owner_tmp: [] = None):
        self.__owner = owner_tmp

    def __get_owner(self) -> []:
        return self.__owner

    def __set_store(self, store_tmp: [] = None):
        if self.__structure == Structure.QUEUE:
            self.__store = deque(store_tmp)
        else:
            self.__store = store_tmp

    def __get_store(self) -> []:
        return self.__store

    structure = property(__get_structure, __set_structure)
    visibility = property(__get_visibility, __set_visibility)
    name = property(__get_name, __set_name)
    owner = property(__get_owner, __set_owner)
    store = property(__get_store, __set_store)

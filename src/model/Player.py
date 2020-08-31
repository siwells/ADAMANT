from interface.IGameObserver import *
from enums.Role import Role


class Player(IGameObserver):
    def update(self, obj: object = None):
        pass

    def __init__(self):
        super().__init__()
        self._name = None
        self._roles = []
        self.__did_move_flag = False

    def _set_name(self, name_tmp: str = None):
        self._name = name_tmp

    def _get_name(self) -> str:
        return self._name

    def _set_roles(self, roles_tmp: [] = None):
        self._roles = roles_tmp

    def _get_roles(self) -> []:
        return self._roles

    def __get_did_move_flag(self) -> bool:
        return self.__did_move_flag

    def __set_did_move_flag(self, flag_tmp: bool = None):
        self.__did_move_flag = flag_tmp

    name = property(_get_name, _set_name, None)
    roles = property(_get_roles, _set_roles, None)
    did_move_flag = property(__get_did_move_flag, __set_did_move_flag, None)

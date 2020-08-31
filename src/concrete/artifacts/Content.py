from helpers.Constants import EMPTY
from interface.IArtifact import IArtifact


class Content(IArtifact):
    def identify(self):
        pass

    def get_id(self) -> int:
        pass

    def __init__(self, data_tmp: str = EMPTY):
        super().__init__(data_tmp)
        self._list = []

    def _get_list(self) -> []:
        return self._list

    def _set_list(self, list_tmp: [] = None):
        self._list = list_tmp

    list = property(_get_list, _set_list, None)

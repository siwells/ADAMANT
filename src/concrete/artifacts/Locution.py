from helpers.Constants import EMPTY
from interface.IArtifact import IArtifact


class Locution(IArtifact):
    def __init__(self, data_tmp: str = EMPTY):
        super().__init__(data_tmp)

    def identify(self):
        pass

    def get_id(self) -> int:
        pass


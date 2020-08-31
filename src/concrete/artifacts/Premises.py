from helpers.Constants import EMPTY
from interface.IArtifact import IArtifact


class Premises(IArtifact):
    def identify(self):
        pass

    def get_id(self) -> int:
        pass

    def __init__(self, data_tmp: str = EMPTY):
        super().__init__(data_tmp)

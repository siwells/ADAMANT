from helpers.Constants import EMPTY


class Artifact:
    def __init__(self, data: str = EMPTY, artifactKey: str = EMPTY):
        self.data = data
        self.artifactKey = artifactKey

    def identify(self):
        pass

    def get_id(self) -> int:
        pass

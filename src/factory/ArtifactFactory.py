import json

from concrete.artifacts.Argument import Argument
from concrete.artifacts.Conclusion import Conclusion
from concrete.artifacts.Content import Content
from concrete.artifacts.Locution import Locution
from concrete.artifacts.Premises import Premises
from helpers.Constants import *
from helpers.StringParser import StringParser


class ArtifactFactory:
    @staticmethod
    def create_artifact(data_str: str = EMPTY):
        artifact = None
        if StringParser.is_json(data_str):
            artifact_json = json.loads(StringParser.dict_to_string(data_str))
            if artifact_json[ARTIFACT_KEY] in ArtifactFactory.__options:
                artifact = ArtifactFactory.__options[artifact_json[ARTIFACT_KEY]].__func__(data_str)
        elif data_str in ArtifactFactory.__options:
            artifact = ArtifactFactory.__options[data_str].__func__(data_str)
        return artifact

    @staticmethod
    def __content(data_tmp: str = EMPTY):
        artifact = Content(data_tmp)
        return artifact

    @staticmethod
    def __argument(data_tmp: str = EMPTY):
        artifact = Argument(data_tmp)
        return artifact

    @staticmethod
    def __locution(data_tmp: str = EMPTY):
        artifact = Locution(data_tmp)
        return artifact

    @staticmethod
    def __conclusion(data_tmp: str = EMPTY):
        artifact = Conclusion(data_tmp)
        return artifact

    @staticmethod
    def __premises(data_tmp: str = EMPTY):
        artifact = Premises(data_tmp)
        return artifact

    __options = {
        "Argument": __argument,
        "Conclusion": __conclusion,
        "Content": __content,
        "Locution": __locution,
        "Premises": __premises
    }
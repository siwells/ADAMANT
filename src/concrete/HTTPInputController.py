from flask import request

from helpers.Constants import UTTERANCE
from interface.IInputController import IInputController


class HTTPInputController(IInputController):
    def __init__(self):
        super().__init__()

    def get_input(self):
        return request.get_json()[UTTERANCE]

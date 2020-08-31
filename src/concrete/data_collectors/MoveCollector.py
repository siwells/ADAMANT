from concrete.HTTPInputController import HTTPInputController
from interface.IGameDataCollector import IGameDataCollector


# TODO pass in controller in constructor
class MoveCollector(IGameDataCollector):
    def collect(self):
        return self.__input_controller.get_input()

    def __init__(self):
        super().__init__()
        self.__input_controller = HTTPInputController()

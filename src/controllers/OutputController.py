from concrete.ConsoleOutputController import ConsoleOutputController
from interface.IHandler import IHandler
from model.GameStatus import GameStatus


# TODO pass in controller in constructor
class OutputController(IHandler):
    def __init__(self):
        super().__init__()

    def handle(self, game_status_tmp: GameStatus = None):
        output = ConsoleOutputController()
        # TODO serialisation
        output.send_output(game_status_tmp.last_interaction_move.__dict__)
        return game_status_tmp, None

    def update_collector(self):
        pass

    def type(self):
        pass

    def update_flag(self):
        pass

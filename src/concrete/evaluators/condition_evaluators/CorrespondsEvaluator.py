from interface.IEvaluator import IEvaluator
from model.Condition import Condition
from model.GameStatus import GameStatus


class CorrespondsEvaluator(IEvaluator):
    @staticmethod
    def evaluate(condition_tmp: Condition = None, game_status_tmp: GameStatus = None):
        evaluated = False
        # TODO implementation
        return evaluated

    def __init__(self):
        super().__init__()
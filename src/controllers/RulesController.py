from enums.Scope import Scope
from interface.IHandler import IHandler
from enums.HandlerType import HandlerType
from model.Principle import Principle
from model.GameStatus import GameStatus
from concrete.evaluators.ConditionsEvaluator import ConditionsEvaluator
from concrete.evaluators.EffectsEvaluator import EffectsEvaluator


class RulesController(IHandler):
    def update_collector(self, game_status_tmp: GameStatus = None):
        return game_status_tmp

    def update_flag(self):
        pass

    def type(self):
        return HandlerType.PRE_MOVE_CHECK

    def __init__(self):
        super().__init__()

    def handle(self, game_status_tmp: GameStatus = None):
        if game_status_tmp is None:
            return game_status_tmp
        principles = self.__get_principles_to_update(game_status_tmp)
        game_status_tmp = self.__evaluate_principles(principles,game_status_tmp)
        game_status_tmp = self.update_collector(game_status_tmp)
        self.update_flag()
        return game_status_tmp, None

    @staticmethod
    def __get_principles_to_update(game_status_tmp: GameStatus) -> []:
        values = []
        for principle in game_status_tmp.principles:
            if principle.scope == Scope.MOVEWISE:
                values.append(principle)
            elif principle.scope == Scope.TURNWISE and game_status_tmp.new_turn:
                values.append(principle)
            elif principle.scope == Scope.INITIAL and game_status_tmp.initial_turn:
                values.append(principle)
        return values

    def __evaluate_principles(self, principles_tmp: [], game_status_tmp: GameStatus) -> GameStatus:
        for principle in principles_tmp:
            if len(principle.conditions) > 0:
                self.__evaluate_condition(principle, game_status_tmp)
            else:
                # just effects so evaluate them
                if len(principle.effects) > 0:
                    game_status_tmp = self.__evaluate_effect(principle, game_status_tmp)
        return game_status_tmp

    def __evaluate_condition(self, principle: Principle, game_status_tmp: GameStatus) -> GameStatus:
        all_conditions_satisfied = True
        for condition in principle.conditions:
            # check condition setting all_conditions_satisfied to false if one of them fails
            all_conditions_satisfied = ConditionsEvaluator.evaluate(condition, game_status_tmp)
            if not all_conditions_satisfied:
                # one of the conditions has not been met - break out
                # TODO gather conditions that have not been satisfied and send them back
                break
        if all_conditions_satisfied:
            game_status_tmp = self.__evaluate_effect(principle, game_status_tmp)
        return game_status_tmp

    @staticmethod
    def __evaluate_effect(principle: Principle, game_status_tmp: GameStatus) -> GameStatus:
        if len(principle.effects) > 0:
            for effect in principle.effects:
                game_status_tmp = EffectsEvaluator.evaluate(effect, game_status_tmp)
        return game_status_tmp


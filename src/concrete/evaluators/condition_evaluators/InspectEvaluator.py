import inspect

from controllers.LoggingController import LoggingController
from helpers.Helpers import Helpers
from interface.IEvaluator import IEvaluator
from model.Condition import Condition
from model.GameStatus import GameStatus


# TODO implementation!!!
class InspectEvaluator(IEvaluator):
    @staticmethod
    def evaluate(condition_tmp: Condition = None, game_status_tmp: GameStatus = None):
        evaluated = InspectEvaluator.__evaluate_inspect(condition_tmp, game_status_tmp)
        return evaluated

    def __init__(self):
        super().__init__()

    # TODO implementation
    @staticmethod
    def __in(data: {} = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        if data['commitment_timing'] is not None:
            evaluated_tmp = InspectEvaluator.__options[data['commitment_timing']].__func__(data, evaluated_tmp,
                                                                                           game_status_tmp)
        else:
            inspect_type = data['inspect_type']
            artifact_id = data['artifact_id']
            store_name = data['store_name']
            player = data['player']
            role = ['role']

        return evaluated_tmp

    @staticmethod
    def __not_in(data: {} = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __on(data: {} = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __not_on(data: {} = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __top(data: {} = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __not_top(data: {} = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __initial(data: {} = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __past(data: {} = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __current(data: {} = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    # TODO what is on/!on
    __options = {
        "In": __in,
        "!In": __not_in,
        "On": __on,
        "!On": __not_on,
        "Top": __top,
        "!Top": __not_top,
        "Initial": __initial,
        "Past": __past,
        "Current": __current
    }

    @staticmethod
    def __evaluate_inspect(condition_tmp: Condition = None, game_status_tmp: GameStatus = None):
        evaluated = False
        LoggingController.logger.debug("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        # verify size of elements in the condition
        if len(condition_tmp.list) >= 2:
            inspect_type = condition_tmp.list[0]
            artifact_id = condition_tmp.list[1]
            store_name = condition_tmp.list[2]
            fourth_element = condition_tmp.list[3] if (len(condition_tmp.list) == 3) else None
            fifth_element = condition_tmp.list[4] if (len(condition_tmp.list) == 4) else None
            player = fourth_element if (
                fifth_element is not None and Helpers.is_player(game_status_tmp, fourth_element)) else None
            role = fifth_element if (player is None and Helpers.is_role(game_status_tmp, fourth_element)) else None
            commitment_timing = fifth_element if (fifth_element is not None) else None
            data = {'inspect_type': inspect_type, 'artifact_id': artifact_id, 'store_name': store_name,
                    'player': player,
                    'role': role, 'commitment_timing': commitment_timing}
            if inspect_type in InspectEvaluator.__options:
                evaluated = InspectEvaluator.__options[inspect_type].__func__(data, evaluated, game_status_tmp)
        return evaluated

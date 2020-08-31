from enums.Scope import Scope
from model.Condition import Condition
from model.Effect import Effect


class Principle:
    def __init__(self):
        self._name = None
        self._scope = Scope
        self._effects = []
        self._condition = []

    def _get_name(self) -> str:
        return self._name

    def _set_name(self, name_tmp: str = None):
        self._name = name_tmp

    def _set_scope(self, scope_tmp: Scope = None):
        if scope_tmp == str.lower(Scope.MOVEWISE.name):
            self._scope = Scope.MOVEWISE
        elif scope_tmp == str.lower(Scope.INITIAL.name):
            self._scope = Scope.INITIAL
        elif scope_tmp == str.lower(Scope.TURNWISE.name):
            self._scope = Scope.TURNWISE

    def _get_scope(self) -> Scope:
        return self._scope

    def _set_effect(self, effects_tmp: [] = None):
        self._effects = effects_tmp

    def _get_effect(self) -> []:
        return self._effects

    def _set_condition(self, condition_tmp: [] = None):
        self._condition = condition_tmp

    def _get_condition(self) -> []:
        return self._condition

    name = property(_get_name, _set_name, None)
    scope = property(_get_scope, _set_scope, None)
    effects = property(_get_effect, _set_effect, None)
    conditions = property(_get_condition, _set_condition, None)
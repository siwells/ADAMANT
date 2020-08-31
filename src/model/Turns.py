from enums.Magnitude import *
from enums.Ordering import *


class Turns:
    def __init__(self):
        self.__magnitude = None
        self.__ordering = None
        self.__max = None

    def __set_magnitude(self, magnitude_tmp: Magnitude = None):
        if magnitude_tmp == str.lower(Magnitude.SINGLE.name):
            self.__magnitude = Magnitude.SINGLE
        elif magnitude_tmp == str.lower(Magnitude.MULTIPLE.name):
            self.__magnitude = Magnitude.MULTIPLE

    def __set_ordering(self, ordering_tmp: Ordering = None):
        if ordering_tmp == str.lower(Ordering.LIBERAL.name):
            self.__ordering = Ordering.LIBERAL
        elif ordering_tmp == str.lower(Ordering.STRICT.name):
            self.__ordering = Ordering.STRICT

    def __set_max(self, max_tmp: int = None):
        self.__max = max_tmp

    def __get_magnitude(self) -> Magnitude:
        return self.__magnitude

    def __get_ordering(self) -> Ordering:
        return self.__ordering

    def __get_max(self):
        return self.__max

    ordering = property(__get_ordering, __set_ordering, None)
    magnitude = property(__get_magnitude, __set_magnitude, None)
    max = property(__get_max, __set_max, None)

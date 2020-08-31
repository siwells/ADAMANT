class Condition:
    def __init__(self):
        self.__name = None
        self.__list = []

    def __get_name(self) -> str:
        return self.__name

    def __set_name(self, name_tmp: str = None):
        self.__name = name_tmp

    def __get_list(self) -> []:
        return self.__list

    def __set_list(self, list_tmp: [] = None):
        self.__list = list_tmp

    name = property(__get_name, __set_name, None)
    list = property(__get_list, __set_list, None)
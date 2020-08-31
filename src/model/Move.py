from concrete.artifacts.Content import Content


class Move:
    def __init__(self, name: str = None, content: Content = None, effects: [] = [], condition: [] = [],
                 final: bool = False):
        self.__name = name
        self.__content = content
        self.__effects = effects
        self.__condition = condition
        self.__final = final

    def __get_name(self) -> str:
        return self.__name

    def __set_name(self, name_tmp: str = None):
        self.__name = name_tmp

    def __set_content(self, content_tmp: Content = None):
        self.__content = content_tmp

    def __get_content(self) -> Content:
        return self.__content

    def __set_effect(self, effects_tmp: [] = None):
        self.__effects = effects_tmp

    def __get_effect(self) -> []:
        return self.__effects

    def __set_condition(self, condition_tmp: [] = None):
        self.__condition = condition_tmp

    def __get_condition(self) -> []:
        return self.__condition

    def __get_final(self) -> bool:
        return self.__final

    def __set_final(self, final_tmp: bool = False):
        self.__final = final_tmp

    name = property(__get_name, __set_name, None)
    effects = property(__get_effect, __set_effect, None)
    conditions = property(__get_condition, __set_condition, None)
    content = property(__get_content, __set_content, None)
    final = property(__get_final, __set_final, None)

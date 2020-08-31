from interface.IInputController import IInputController


class ConsoleInputController(IInputController):
    def __init__(self):
        super().__init__()

    def get_input(self):
        return input("Enter: ")

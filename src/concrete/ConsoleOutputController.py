from interface.IOutputController import IOutputController


class ConsoleOutputController(IOutputController):
    def __init__(self):
        super().__init__()

    def send_output(self, data: str = None):
        print(data)

from abc import ABC

class CommandExecutor(ABC):
    name = ""

    def execute(self, app, args):
        ...

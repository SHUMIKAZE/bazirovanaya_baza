from .base import CommandExecutor

class ErrorCommand(CommandExecutor):
    name = "error"

    def execute(self, app, args):
        print(args["msg"])

from .base import CommandExecutor

class QuitCommand(CommandExecutor):
    name = "quit"

    def execute(self, app, args):
        app.db.close(app.media)
        print(args["msg"])
        raise SystemExit

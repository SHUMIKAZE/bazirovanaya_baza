from .base import CommandExecutor

class QuitCommand(CommandExecutor):
    name = "quit"

    def execute(self, app, args):
        app.db.media.conn.close()
        print(args["msg"])
        raise SystemExit

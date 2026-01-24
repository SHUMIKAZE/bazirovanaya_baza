from .base import CommandExecutor

class ListCommand(CommandExecutor):
    name = "list"

    def execute(self, app, args):
        data = app.db.get_data(app.media, args["target"])
        for r in data:
            print(dict(r))

from typing import List


from .base import CommandHandlerBase

class ListCommandHandler(CommandHandlerBase):

    def __init__(self):
        self.args_handlers = {
            "works": self.handle_works,
            "genres": self.handle_genres,
        }

    def handle_args(self, args: List):
        if not args:
            return {
                "type": "error",
                "msg": "What to list, works or genres?"
            }

        if args[0] not in self.args_handlers.keys():
            return {
                "type": "error",
                "msg": f"Unknown argument {args[0]}"
            }
        
        return self.args_handlers[args[0]]()
    
    def handle_works(self):
        return {
            "type": "list",
            "target": "works"
        }

    def handle_genres(self):
        return {
            "type": "list",
            "target": "genres"
        }
    

from typing import List

from .base import CommandHandlerBase

class QuitCommandHandler(CommandHandlerBase):

    def __init__(self):
        pass

    def handle_args(self, args: List):
        if args:
            return {
                "type": "error",
                "msg": f"Unknown argument {args[0]}"
            }
        else:
            return {
                "type": "quit",
                "msg": "Quitting..."
            }

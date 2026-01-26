from typing import List

from .base import CommandHandlerBase
from ..comand_routing import CmdRouter, Command

def create_quit_router():
    router = CmdRouter()

    @router.handler(command="quit")
    def handle_quit(command: Command):
        raise SystemExit
    
    return router


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

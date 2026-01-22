from typing import Dict

from .handlers import (
    CommandHandlerBase,
    ListCommandHandler,
    QuitCommandHandler
)

class MainCommandHandler:

    handlers: Dict[str,CommandHandlerBase] = {
        "list": ListCommandHandler(),
        "quit": QuitCommandHandler()
    }

    def __init__(self):
        pass

    def handle(self, cmd_str: str):
        parts = self.to_parts(cmd_str)
        if not parts:
            return None

        cmd = parts[0]
        args = parts[1:]

        cmd_handler = MainCommandHandler.handlers.get(cmd)
        if not cmd_handler:
            return {
                "type": "error",
                "msg": f"Unknown command: {cmd}"
            }

        return cmd_handler.handle_args(args)
    
    def to_parts(self, cmd_str: str):
        if not cmd_str:
            return None

        parts = cmd_str.split()
        if not parts:
            return None
        
        return parts







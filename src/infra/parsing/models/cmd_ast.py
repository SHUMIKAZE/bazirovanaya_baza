from typing import List, Optional

from .command import Command

class ComandAST:
    cmd_sequence: List[Command]

    def __init__(self, cmd_sequence: Optional[List[Command]] = None) -> None:
        if cmd_sequence is None:
            cmd_sequence = []
        self.cmd_sequence = cmd_sequence


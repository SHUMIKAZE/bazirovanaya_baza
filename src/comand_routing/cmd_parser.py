from .command import Command


class CommandParser:

    def __init__(self):
        pass

    def __call__(self, command: str):

        if not isinstance(command, str):
            raise TypeError(f"Command need to be a string, not {type(command)}")

        try:
            parts = command.strip().split()
        except Exception as e:
            raise ValueError(f"Unknown error while parsing command: {e}")
        
        return Command(parts)
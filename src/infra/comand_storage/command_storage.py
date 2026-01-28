from typing import Dict, List, Optional

from .command_node import CommandNode
from .value_objects.command_name import CommandName


class CommandStorage:
    def __init__(self):
        self._roots: Dict[str, CommandNode] = {}

    def add_root_command(self, command: CommandNode) -> None:
        if command.parent is not None:
            raise ValueError("В хранилище можно добавлять только корневые узлы (без родителя).")

        key = str(command.name)
        if key in self._roots:
            raise ValueError(f"Команда '{key}' уже существует в хранилище.")
        
        self._roots[key] = command

    def find_command(self, path_parts: List[str]) -> Optional[CommandNode]:
        if not path_parts:
            return None

        current_command = self._roots.get(path_parts[0])
        if not current_command:
            return None

        for part in path_parts[1:]:
            current_command = current_command.children.get(part)
            if not current_command:
                return None
        
        return current_command

    def _parse_path(self, command_path: str) -> List[str]:
        return command_path.strip().split()

    def _ensure_root(self, root_name: str) -> CommandNode:
        if root_name not in self._roots:
            self.add_root_command(CommandNode(CommandName(root_name)))
        return self._roots[root_name]

    def add_command(self, command_path: str) -> CommandNode:
        parts = self._parse_path(command_path)
        if not parts:
            raise ValueError("Путь команды не может быть пустым.")

        current_command = self._ensure_root(parts[0])

        for part_name in parts[1:]:
            current_command = current_command.get_or_create_child(part_name)
        
        return current_command

    def get_command(self, command_path: str) -> Optional[CommandNode]:
        parts = self._parse_path(command_path)
        return self.find_command(parts)

    def contains(self, command_path: str) -> bool:
        return self.get_command(command_path) is not None
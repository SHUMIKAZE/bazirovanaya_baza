from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .value_objects.command_name import CommandName
from .value_objects.flag import Flag


@dataclass
class CommandNode:
    name: CommandName
    parent: Optional[CommandNode] = None
    children: Dict[str, CommandNode] = field(default_factory=dict)
    flags: List[Flag] = field(default_factory=list)

    @property
    def full_path(self) -> str:
        if self.parent:
            return f"{self.parent.full_path} {self.name}"
        return str(self.name)

    def add_child(self, child: CommandNode) -> None:
        if str(child.name) in self.children:
            raise ValueError(f"Подкоманда '{child.name}' уже существует в '{self.name}'.")
        
        child.parent = self
        self.children[str(child.name)] = child

    def get_or_create_child(self, name: str) -> CommandNode:
        if name in self.children:
            return self.children[name]
        
        child = CommandNode(CommandName(name))
        self.add_child(child)
        return child

    def add_flag(self, flag: Flag) -> None:
        self.flags.append(flag)

    def has_flag(self, flag_value: str) -> bool:
        return any(flag.value == flag_value for flag in self.flags)

    def __str__(self) -> str:
        return self.full_path
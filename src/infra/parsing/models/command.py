from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List

from ..exeptions.parser import ASTError
from .argument import Argument
from .flag import Flag

@dataclass
class Command:
    flags: Optional[List[Flag]] = None
    arguments: Optional[List[Argument]] = None
    subcomand: Optional[Command] = None
 
    def __post_init__(self):
        if self.subcomand and self.arguments:
            raise ASTError("Команда не может иметь одновременно и аргументы и подкоманды.")
        
    def add_flag(self, flag: Flag):

        if not isinstance(flag, Flag):
            raise TypeError("Аргумент должен быть типа Flag.")
        
        if self.flags is None:
            self.flags = []

        self.flags.append(flag)

    def add_subcomand(self, subcomand: Command):
        if not isinstance(subcomand, Command):
            raise TypeError("Аргумент должен быть типа Command.")

        if self.has_arguments:
            raise ASTError("Команда не может иметь одновременно и аргументы и подкоманды.")
        
        self.subcomand = subcomand

    def add_argument(self, argument: Argument):
        if not isinstance(argument, Argument):
            raise TypeError("Аргумент должен быть типа Argument.")
        
        if self.has_subcomand:
            raise ASTError("Команда не может иметь одновременно и аргументы и подкоманды.")


        
    @property
    def has_flags(self) -> bool:
        return self.flags is not None
    
    @property
    def has_arguments(self) -> bool:
        return self.arguments is not None
    
    @property
    def has_subcomand(self) -> bool:
        return self.subcomand is not None
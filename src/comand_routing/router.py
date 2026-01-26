from __future__ import annotations
from functools import wraps
from typing import Dict, List, Any, Optional, Union

from .handler import Handler
from .cmd_parser import CommandParser
from .command import Command


class CmdRouter:

    def __init__(
        self, 
        cmd_parser: CommandParser = CommandParser(),
        default_handler: Optional[Handler] = None,
    ):
        self._cmd_parser = cmd_parser
        self._default_handler: Optional[Handler] = default_handler
        self._handlers: Dict[Command, Handler]= {}
        self.subrouters: List[CmdRouter] = []
        self._root_router: Optional[CmdRouter] = None
        self.context: Dict[str, Any] = {}
    
    def handler(
        self,
        *,
        command: str,
    ):
        def decorator(func):
            handler_obj = Handler(func)
            parsed_command = self._cmd_parser(command)
            self._handlers[parsed_command] = handler_obj

            return func
        return decorator
    
    def handle(self, command: str) -> None:
        command: Command = self._cmd_parser(command)
        handler: Optional[Handler] = self.find_handler(command, None)

        if handler is None:
            raise ValueError(f"Unknown command: {command}")
        
        handler(command=command, context=self.context)
    
    def add_subrouter(self, subrouter: CmdRouter):

        if not isinstance(subrouter, CmdRouter):
            raise TypeError(f"Subrouter must be a Router, not {type(subrouter)}")
        
        self.subrouters.append(subrouter)
    
    def find_handler(self, command: Command, default: Optional[Handler] = None) -> Handler:
        if default is None:
            default = self._default_handler
        
        found_handler: Optional[Handler] = self._handlers.get(command, None)

        if found_handler is not None:
            return found_handler
        
        for subrouter in self.subrouters:
            found_handler = subrouter.find_handler(command, None)
            if found_handler is not None:
                return found_handler
        
        return default
    
    def _set_root_router(self, router: CmdRouter):
        self._root_router = router

    @property
    def commands(self) -> list[Command]:
        comms = list(self._handlers.keys())
        for subrouter in self.subrouters:
            comms.extend(subrouter.commands)
        return comms

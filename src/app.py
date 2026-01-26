from typing import Dict
from .command_handler import MainCommandHandler
from .command_executor import COMMANDS, CommandExecutor
from .config import DB_PATH, SCHEMA_PATH
from .user import User
from .comand_routing import CmdRouter

from .handlers.list_command_handler import create_list_router
from .handlers.quit_comand_handler import create_quit_router
from .handlers.help_command_handler import create_help_router


from .utils import get_user_input

class App:
    def __init__(self, version: int = 1) -> None:
        self.user = User(DB_PATH, SCHEMA_PATH)
        self.running: bool = True
        self.commands: Dict[str, CommandExecutor] = {c.name: c for c in COMMANDS}
        self.version = version
        self.prepare_app()
    
    def prepare_app(self):
        
        if self.version == 2:
            self.root_router = CmdRouter()
            self.root_router.context = {
                "user": self.user,
                "root_router": self.root_router
            }

            self.root_router.add_subrouter(create_list_router())
            self.root_router.add_subrouter(create_quit_router())
            self.root_router.add_subrouter(create_help_router())

    def run(self) -> None:
        print("App started.")
        if self.version == 1:
            self.run_v1()
        else:
            self.run_v2()


    def run_v1(self) -> None:

        main_handler = MainCommandHandler()

        while self.running:
            try:
                user_input: str = input(">>> ")
            except KeyboardInterrupt:
                user_input: str = "quit"
            except EOFError:
                user_input: str = "quit"

            action = main_handler.handle(user_input)


            if action is None:
                continue

            if action["type"] == "error":
                print(action["msg"])
                continue

            handler = self.commands.get(action["type"])

            if not handler:
                print("Unknown action type:", action["type"])
                continue

            try:
                handler.execute(self.user, action)
            except SystemExit:
                break
    
    def run_v2(self):

        while self.running:
            
            try:
                self.root_router.handle(get_user_input())
            except ValueError as e:
                print(e)
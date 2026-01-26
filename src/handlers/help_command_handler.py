from pprint import pprint

from ..comand_routing import CmdRouter, Command

def create_help_router() -> CmdRouter:
    router = CmdRouter()

    @router.handler(command="help")
    def handle_help(command: Command, context):
        root_router: CmdRouter = context["root_router"]
        pprint(root_router.commands)
    
    return router
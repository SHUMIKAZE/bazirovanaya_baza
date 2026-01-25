from .commands import CommandExecutor, ListCommand, QuitCommand





COMMANDS: set[CommandExecutor] = {
    ListCommand(),
    QuitCommand()
}

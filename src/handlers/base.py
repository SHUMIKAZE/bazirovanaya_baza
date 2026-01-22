from abc import ABC, abstractmethod


class CommandHandlerBase(ABC):

    @abstractmethod
    def handle_args(self) -> dict:
        ...
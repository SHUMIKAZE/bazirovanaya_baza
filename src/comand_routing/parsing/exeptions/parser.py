from .base import ComandParserError

class ParserError(ComandParserError):
    
    def __init__(
        self, 
        message: str, 
        source: str,
    ) -> None:
        self.raw_message = message
        self.source = source

        formatted_message = f"{message}\ncmd: {source}"
        super().__init__(formatted_message)
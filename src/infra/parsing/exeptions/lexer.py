from .base import ComandParserError

class LexerError(ComandParserError):
    def __init__(self, message: str, source: str, position: int, unparsed_suffix: str):
        self.raw_message = message
        self.source = source
        self.position = position
        self.unparsed_suffix = unparsed_suffix

        # Вычисляем номер строки и колонки (полезно для IDE или логов)
        self.line = source.count('\n', 0, position) + 1
        last_newline = source.rfind('\n', 0, position)
        self.column = position - last_newline

        # Подготовка визуального контекста
        lines = source.split('\n')
        error_line = lines[self.line - 1] if self.line <= len(lines) else ""
        
        # Указатель на ошибку (column - 1, т.к. колонка 1-based)
        pointer = " " * (self.column - 1) + "^"
        formatted_message = f"{message}\nAt line {self.line}, column {self.column}:\n{error_line}\n{pointer}"
        
        super().__init__(formatted_message)

from src.comand_routing.parsing.lexer.lexer import Lexer

from pprint import pprint

lexer = Lexer()

tokens = lexer.tockenize(
    cmd='git -fr --code --code-complete="fdf" status "with probels"'
)

pprint(tokens)
from src.infra.parsing.lexical_analysis.lexer import Lexer

from pprint import pprint

parser = Lexer()

tokens = parser.tokenize(
    cmd='git -fr --code --code-complete="fdf" status "with probels"'
)

pprint(tokens)


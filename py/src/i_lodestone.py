from .lexer import Lexer
from .parser import Parser
from .builtins import Builtins

import click


@click.command()
@click.option('--input_file', help='input of iLodestone file')
def main(input_file):
    with open(input_file) as f:
        text_input = f.read()

    lexer = Lexer().get_new_lexer()
    tokens = lexer.lex(text_input)

    pg = Parser(Builtins)
    pg.parse()
    parser = pg.get_parser()
    parser.parse(tokens).eval()


if __name__ == '__main__':
    main()

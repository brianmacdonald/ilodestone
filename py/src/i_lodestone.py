from interpreter.lexer import Lexer
from interpreter.parser import Parser
from interpreter.builtins import Builtins

import click


@click.command()
@click.option('--input_file', help='input of iLodestone file')
def main(input_file):
    with open(input_file) as f:
        text_input = f.read()

    lexer = Lexer(text_input)

    pg = Parser(lexer, Builtins)
    pg.parse()
    parser = pg.get_parser()
    parser.parse().eval()


if __name__ == '__main__':
    main()

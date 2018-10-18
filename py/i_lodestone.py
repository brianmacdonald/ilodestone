from lib.lexer import Lexer
from lib.parser import Parser

import click

from lib.evaluator import node_eval


class State:

    def __init__(self, fn):
        self.fn = fn
        with open(fn) as f:
            self.src = f.read()
        self.lines = self.src.splitlines()

    def pos(self, t):
        """Reprocess location information (see parse() for more details)."""
        ln = t.source_pos.lineno - 1
        if t.value and t.value[0] == '\n':
            ln -= 1

        col = t.source_pos.colno - 1
        line = self.lines[ln] if ln < len(self.lines) else ''
        return (ln, col), (ln, col + len(t.value)), line, self.fn


@click.command()
@click.option('--input_file', help='input of iLodestone file')
def main(input_file):
    state = State(input_file)

    lexer = Lexer().get_lexer()
    tokens = lexer.lex(state.src)

    pg = Parser()
    pg.parse()
    parser = pg.get_parser()
    print(node_eval(parser.parse(tokens, state=state), {}))
    #parser.parse(tokens).eval()


if __name__ == '__main__':
    main()

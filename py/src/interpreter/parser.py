from interpreter.ast import Boolean, IdentifierExpression, IntegerLiteral, PrefixExpression, ExpressionStatement
from interpreter.token import Token


def start_parse(lex, builtins):
    parser = Parser(lex, builtins)
    parser.next_token()
    parser.next_token()
    return parser


LOWEST = 0
EQUALS = 1
LESSGREATER = 2
SUM = 3
PRODUCT = 4
MODULUS = 5
PREFIX = 6
CALL = 7
INDEX = 8


class Parser:

    def __init__(self, lex, builtins):
        self.lexer = lex
        self.builtins = builtins
        self.errors = []
        self.cur_token = Token.create_start_token()
        self._peek_token = Token.create_start_token()

    def parse(self):
        pass

    def get_parser(self):
        pass

    def peek_token(self):
        pass

    def next_token(self):
        self.cur_token = self.peek_token
        self._peek_token = self.lexer

    def prefix_parse_call(self, token):
        token_parse = {
            Token.BANG: self.parse_prefix_expression,
            Token.MINUS: self.parse_prefix_expression,
            Token.INT: self.parse_integer_literal,
            Token.IDENT: self.parse_identifier,
            Token.TRUE: self.parse_boolean,
            Token.FALSE: self.parse_boolean,
            Token.LPAREN: self.parse_grouped_expression(),
            Token.IF: self.parse_if_expression,
            Token.FUNCTION: self.parse_function_literal,
            Token.STRING: self.parse_string_literal,
        }
        return token_parse.get(token)()

    def parse_prefix_expression(self):
        token = self.cur_token
        operator = self.cur_token.literal
        self.next_token()
        right = self.parse_expression(PREFIX)
        return PrefixExpression(token, operator, right)

    def parse_integer_literal(self):
        return IntegerLiteral(self.cur_token, self.cur_token.literal)

    def parse_identifier(self):
        return IdentifierExpression(self.cur_token, self.cur_token.literal)

    def parse_boolean(self):
        return Boolean(self.cur_token, self.cur_token_is(Token.TRUE))

    def cur_token_is(self, token):
        return self.cur_token is token

    def parse_expression_statement(self):
        token = self.cur_token
        expression = self.parse_expression(LOWEST)
        if self.peek_token_is(Token.SEMICOLON):
            self.next_token()
        return ExpressionStatement(token, expression)

    def peek_token_is(self, token):
        return self.peek_token() is token

    def parse_grouped_expression(self):
        self.next_token()
        exp = self.parse_expression(LOWEST)
        if not self.expect_peek(Token.RPAREN):
            return None
        return exp

    def expect_peek(self, token):
        if self.peek_token_is(token):
            self.next_token()
            return True
        else:
            self.peek_error(token)
            return False

    def peek_error(self, token):
        peek_token = self._peek_token
        self.errors.append(f"Peek Error: expected next token to be {token}, found {peek_token} instead")

    def parse_expression(self, precedence):
        cur_token = self.cur_token
        prefix = self.prefix_parse_call(self.cur_token)
        if prefix is not None:
            left_exp = prefix
            while self.peek_token_is(Token.SEMICOLON) is False and precedence < self.peek_precedence():
                peek = self._peek_token
                if self.has_infix(peek):
                    return left_exp
                self.next_token()
                left_exp = self.infix_parse_call(peek, left_exp)
            return left_exp
        else:
            self.no_prefix_parse_fn_error(cur_token.t_type)
            return None

    def peek_precedence(self):
        peek_token = self._peek_token
        prec = self.precedences(peek_token)
        return prec if prec is not None else None

    def precedences(self, peek_token):
        precedences = {
            Token.EQ: EQUALS,
            Token.NOT_EQ: EQUALS,
            Token.LT: LESSGREATER,
            Token.GT: SUM,
            Token.PLUS: SUM,
            Token.MINUS: SUM,
            Token.MODULO: MODULUS,
            Token.SLASH: PRODUCT,
            Token.ASTERISK: PRODUCT,
            Token.LPAREN: CALL,
            Token.LBRACKET: INDEX,
        }
        return precedences.get(peek_token)

    def has_infix(self, token):
        return False

from dataclasses import dataclass


@dataclass
class TokenType:
    name: str


@dataclass
class Token:

    t_type: TokenType
    literal: str

    ILLEGAL = TokenType("ILLEGAL")
    EOF = TokenType("EOF")
    IDENT = TokenType("IDENT")
    UNDERSCORE = TokenType("UNDERSCORE")
    FUNCTION = TokenType("FUNCTION")
    OBJECT = TokenType("OBJECT")
    IMPORT = TokenType("IMPORT")
    LET = TokenType("LET")
    WHILE = TokenType("WHILE")
    TRUE = TokenType("TRUE")
    FALSE = TokenType("FALSE")
    IF = TokenType("IF")
    ELSE = TokenType("ELSE")
    RETURN = TokenType("RETURN")
    CLONE = TokenType(":=.")
    CLONE_IMMUTABLE = TokenType("::=.")
    ASSIGN_IMMUTABLE = TokenType("::=")
    ASSIGN = TokenType(":=")
    REASSIGN = TokenType("=")
    COLON = TokenType(":")
    PLUS = TokenType("+")
    MINUS = TokenType("-")
    BANG = TokenType("!")
    ASTERISK = TokenType("*")
    SLASH = TokenType("/")
    MODULO = TokenType("%")
    LT = TokenType("<")
    GT = TokenType(">")
    EQ = TokenType("==")
    NOT_EQ = TokenType("!=")
    WITH_PROTOTYPE = TokenType("=>")
    COMMA = TokenType(",")
    SEMICOLON = TokenType(";")
    LPAREN = TokenType("(")
    RPAREN = TokenType(")")
    LBRACE = TokenType("{")
    RBRACE = TokenType("}")
    LBRACKET = TokenType("[")
    RBRACKET = TokenType("]")
    SLOT = TokenType(".")
    STRING = TokenType("STRING")
    INT = TokenType("INT")


def create_start_token():
    return Token(Token.EOF, Token.EOF.name)


KEYWORDS = {
    "Object": Token.OBJECT,
    "fun": Token.FUNCTION,
    "let": Token.LET,
    "while": Token.WHILE,
    "true": Token.TRUE,
    "false": Token.FALSE,
    "if": Token.IF,
    "else": Token.ELSE,
    "return": Token.RETURN,
    "import": Token.IMPORT
}


def lookup_ident(ident):
    found = KEYWORDS.get(ident)
    return Token.IDENT if found is None else found

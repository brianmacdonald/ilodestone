from interpreter.token import lookup_ident, Token


def test_lookup_ident():
    assert Token.LET is lookup_ident("let")


def test_lookup_ident_not_found():
    assert None is lookup_ident("foobar")

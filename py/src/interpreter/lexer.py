
class Lexer:

    position = 0
    read_position = 0
    ch = None

    def __init__(self, lex_input):
        self.input = lex_input

    def lex(self):
        self.read_char()

    def read_char(self):
        if self.read_position >= len(self.input):
            self.ch = chr(0)
        else:
            self.ch = chr(self.input[self.read_position])
        self.position = self.read_position
        self.read_position += 1

    def skip_whitespace(self):
        done = False
        while done is False:
            if self.ch in ('', '\t', '\n', '\r'):
                self.read_char()
            else:
                done = True

    def peek_char(self):
        if self.read_position >= len(self.input):
            return chr(0)
        else:
            return chr(self.input[self.read_position])

    def read_string(self):
        position = self.position + 1
        done = False
        while done is False:
            self.read_char()
            if self.ch in ('"', chr(0)):
                done = True
        take_size = self.position - position
        return self.input[position:take_size]

    def read_number(self):
        position = self.position
        done = False
        while done is False:
            if self.ch.isdigit():
                self.read_char()
            else:
                done = True
        take_size = self.position - position
        return self.input[position:take_size]


                

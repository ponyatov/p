import sys

## lexer

import ply.lex as lex

tokens = ['INT', 'ID']
t_ignore = '[ \t\r\n]+'
t_ignore_comment = '\#.*'

def t_error(t): raise SyntaxError(t)

lexer = lex.lex()

## Read-Eval-Print-Loop
def REPL(): pass

## command line processing

if __name__ == '__main__':
    for src in sys.argv[1:]:
        with open(src) as script:
            lexer.input(script.read())
    REPL()

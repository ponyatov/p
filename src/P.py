import sys

## Virtual FORTH Machine

## data stack
D = []

## `( -- )` stop system
def bye(): sys.exit(0)

## lexer

import ply.lex as lex

tokens = ['INT', 'ID', 'CHAR']
t_ignore = '[ \t\r\n]+'
t_ignore_comment = '\#.*'

def t_INT(t):
    r'[+\-]?[0-9]+'
    t.value = int(t.value); return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

t_CHAR = '.'

def t_error(t): raise SyntaxError(t)

lexer = lex.lex()

## parser

import ply.yacc as yacc

def p_syntax_none(p):
    r' syntax : '
    pass
def p_syntax_ex(p):
    r' syntax : syntax ex'
    print(p[2])

def p_ex_char(p):
    r' ex : CHAR '
    p[0] = f'char: {p[1]}'
def p_ex_id(p):
    r' ex : ID '
    p[0] = f'id: {p[1]}'
def p_ex_int(p):
    r' ex : INT '
    p[0] = f'int: {p[1]}'

def p_error(p): raise SyntaxError(p)

parser = yacc.yacc(debug=False, write_tables=False)


## Read-Eval-Print-Loop

import readline

def REPL():
    print(D)
    try: parser.parse(input('> '))
    except EOFError: bye()

## command line processing

if __name__ == '__main__':
    for src in sys.argv[1:]:
        with open(src) as script:
            parser.parse(script.read())

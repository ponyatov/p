import sys

## Virtual FORTH Machine

## logging
log = True

## data stack
D = []

## `( -- o )` push element
def push(o): D.append(o)

## `( o -- )` pop element
def pop(): ret = D[-1]; D.pop(); return ret

## VM commands

## `( -- )` do nothing
def nop():
    if log: print(nop)

## `( -- )` stop system
def halt():
    if log: print(halt); sys.exit(0)

## `( ... -- )` clean stack
def dot():
    if log: print(dot); D = []

## `( -- )` print stack
def quest(): print(D)

## vocabulary

W = {'nop': nop, 'halt': halt, '.': dot, '?': quest}


## lexer

import ply.lex as lex

tokens = ['INT', 'ID']
t_ignore = '[ \t\r\n]+'
t_ignore_comment = '\#.*'

def t_INT(t):
    r'[+\-]?[0-9]+'
    t.value = int(t.value); return t

def t_ID(t):
    r'[^# \t\r\n]+'
    return t

def t_error(t): raise SyntaxError(t)

lexer = lex.lex()

## parser

import ply.yacc as yacc

def p_syntax_none(p):
    r' syntax : '
    pass
def p_syntax_ex(p):
    r' syntax : syntax ex'
    pass

def p_ex_int(p):
    r' ex : INT '
    push(p[1])
def p_ex_id(p):
    r' ex : ID '
    W[p[1]]()

def p_error(p): raise SyntaxError(p)

parser = yacc.yacc(debug=False, write_tables=False)


## Read-Eval-Print-Loop

import readline
from threading import Thread

def REPL():
    while True:
        quest()
        try: cmd = input('> ')
        except EOFError: halt()
        t = Thread(target=parser.parse, args=[cmd]); t.start(); t.join()
W['REPL'] = REPL

## command line processing

if __name__ == '__main__':
    for src in sys.argv[1:]:
        with open(src) as script:
            parser.parse(script.read())

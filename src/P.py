import sys

## custom types

class Object: pass
class Primitive(Object):
    def __init__(self, V, base=0x0A):
        match V:
            case int(V): self.value = V
            case str(V): self.value = int(V, base)
            case _: raise TypeError(V)

class Int(Primitive):
    def __init__(self, V): super().__init__(V, 0x0A)
    def __repr__(self): return f'{self.value}'

class Hex(Primitive):
    def __init__(self, V): super().__init__(V, 0x10)
    def __repr__(self): return f'0x{self.value:x}'

class Oct(Primitive):
    def __init__(self, V): super().__init__(V, 0x08)
    def __repr__(self): return f'0o{self.value:o}'

class Bin(Primitive):
    def __init__(self, V): super().__init__(V, 0x02)
    def __repr__(self): return f'0b{self.value:b}'

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
    if log: print(dot); D.clear()

## `( -- )` print stack
def quest(): print(D)

## `( hex -- dec )` convert to decimal int
def int_(): push(Int(pop().value))
def hex_(): push(Hex(pop().value))
def oct_(): push(Oct(pop().value))
def bin_(): push(Bin(pop().value))

## vocabulary

W = {'nop': nop, 'halt': halt, '.': dot, '?': quest,
     'int': int_, 'hex': hex_, 'oct': oct_, 'bin': bin_, }


## lexer

import ply.lex as lex

tokens = ['INT', 'HEX', 'OCT', 'BIN', 'ID']
t_ignore = '[ \t\r\n]+'
t_ignore_comment = '\#.*'

def t_HEX(t):
    r'0x[0-9a-fA-F]+'
    t.value = Hex(t.value); return t
def t_OCT(t):
    r'0o[0-7]+'
    t.value = Oct(t.value); return t
def t_BIN(t):
    r'0b[01]+'
    t.value = Bin(t.value); return t
def t_INT(t):
    r'[+\-]?[0-9]+'
    t.value = Int(t.value); return t

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
    r' ex : int '
    push(p[1])
def p_int_dec(p):
    r' int : INT '
    p[0] = p[1]
def p_int_hex(p):
    r' int : HEX '
    p[0] = p[1]
def p_int_oct(p):
    r' int : OCT '
    p[0] = p[1]
def p_int_bin(p):
    r' int : BIN '
    p[0] = p[1]

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
        Thread(target=parser.parse, args=[cmd]).start() # ignore errors
W['REPL'] = REPL

## command line processing

if __name__ == '__main__':
    for src in sys.argv[1:]:
        with open(src) as script:
            parser.parse(script.read())

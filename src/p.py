import ply.lex as lex

tokens = ['INT', 'ID']
t_ignore = '[ \t\r\n]+'
t_ignore_comment = '\#.*'

def t_error(msg): raise SyntaxError(t)

lexer = lex.lex()

with open('lib/p.ini') as src:
    lexer.input(src.read())

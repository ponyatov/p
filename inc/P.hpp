#pragma once

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

extern int main(int argc, char *argv[]);
extern void arg(int argc, char *argv);

extern int yylex();
extern int yylineno;
extern char *yytext;
extern FILE *yyin;
extern char *yyfile;
extern int yyparse();
extern void yyerror(const char *msg);
#include "P.yacc.hpp"

#define Dsz 0x10
extern int D[Dsz];  ///< data stack
extern size_t Dp;   ///< data stack pointer

extern void push(int n);  ///< `( -- )` push to @ref D
extern int pop();         ///< `( -- )` pop from @ref D
extern void quest();      ///< `( -- )` print @ref D

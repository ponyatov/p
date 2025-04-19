#pragma once

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

extern int main(int argc, char *argv[]);
extern void arg(int argc, char *argv);

extern int yylex();
extern int yylineno;
extern char *yytext;
extern FILE* yyin;
extern char *yyfile;
extern int yyparse();
extern void yyerror(const char* msg);
#include "P.yacc.hpp"

#pragma once

#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <map>

using namespace std;

extern int main(int argc, char *argv[]);
extern void arg(int argc, char *argv);

class Object {
    string value;

    size_t ref;           ///< gc ref.counter
    static Object *pool;  ///< global object's pool
    Object *next;         ///< linked list

   public:
    Object();
    Object(string V);
    virtual ~Object();
    virtual string dump() { return value; }
};

class Sym : public Object {
   public:
    Sym(string V);
};

class Int : public Object {
    int value;

   public:
    Int(string V);
    string dump();
};

#define Dsz 0x10
extern Object *D[Dsz];  ///< data stack
extern size_t Dp;       ///< data stack pointer

extern void push(Object *o);  ///< `( -- o )` push to @ref D
extern Object *pop();         ///< `( o -- )` pop from @ref D
extern void quest();          ///< `( -- )` print @ref D

extern map<string, Object *> W;  ///< vocabulary

extern int yylex();
extern int yylineno;
extern char *yytext;
extern FILE *yyin;
extern char *yyfile;
extern int yyparse();
extern void yyerror(const char *msg);
#include "P.yacc.hpp"
#define TOKEN(C, X)               \
    {                             \
        yylval.o = new C(yytext); \
        return X;                 \
    }

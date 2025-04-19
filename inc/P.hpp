#pragma once

#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <map>

using namespace std;

/// @defgroup main main
/// @brief POSIX entry point
/// @{

extern int main(int argc, char *argv[]);
extern void arg(int argc, char *argv);

/// @}

/// @defgroup core core
/// @brief EDS: Executable Data Sturucture (object graph)

/// @defgroup gc gc
/// @ingroup core
/// @brief garbage collector

/// @brief root object class
/// @details common behaviour for any item in a system
/// @ingroup core
class Object {
    string value;  ///< object name / scalar value

    /// @ingroup gc
    /// @{
    size_t ref;           ///< ref.counter
    static Object *pool;  ///< global object's pool
    Object *next;         ///< linked list
   public:
    /// @brief returns `this` with @ref ref `++`
    Object *incref();
    /// @brief returns `this` with @ref ref `--`
    Object *decref();
    /// @}

   public:
    /// @name (de)constructors
    /// @{
    Object();           ///< for inherited with overriden @ref value
    Object(string V);   ///< for inherited with string @ref value
    virtual ~Object();  ///< clean up
    /// @}

    /// @name dump/stringify
    /// @{
    string tag();                           ///< `<T:`
    virtual string val() { return value; }  ///< `:V>`
    string dump();                          ///< `<T:V>`
                                            /// @}

    /// @name compile/execute
    /// @{
    virtual void exec();  ///< execute object
    /// @}
};

/// @brief symbol (function/variable name etc)
/// @ingroup core
class Sym : public Object {
   public:
    Sym(string V);
};

/// @brief integer number
/// @ingroup core
class Int : public Object {
    int value;

   public:
    Int(string V);
    string val();
};

/// @brief @ref vm command (`void function()` wrapper)
/// @ingroup core
class Cmd : public Object {
    void (*fn)();

   public:
    Cmd(string V, void (*F)());  ///< `new Cmd("some",some)`
    void exec();                 ///< run @ref fn
};

/// @defgroup vm vm
/// @brief Virtual stack Machine
/// @{

/// @defgroup stack stack
/// @brief @ref D
/// @{

/// @ref D size
#define Dsz 0x10
extern Object *D[Dsz];  ///< data stack
extern size_t Dp;       ///< data stack pointer

extern void push(Object *o);  ///< `( -- o )` push to @ref D
extern Object *pop();         ///< `( o -- )` pop from @ref D
extern void quest();          ///< `( -- )` print @ref D

/// @}

/// @defgroup vocabulary vocabulary
/// @brief @ref W
/// @{
extern map<string, Object *> W;  ///< vocabulary
/// @}

/// @defgroup flow flow
/// @brief control flow
/// @{

extern void nop();   ///< `( -- )` empty command
extern void halt();  ///< `( -- )` halt system

/// @}
/// @}

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

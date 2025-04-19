%{
    #include "P.hpp"
    char *yyfile = nullptr;
%}

%option yylineno noyywrap

s [+\-]
d [0-9]

%%
#[^\n]*     {}                  // line comment
[ \t\r\n]+  {}                  // drop spaces

{s}?{d}+    TOKEN(Int,INT)
[^ \t\r\n]+ TOKEN(Sym,ID )

.           { yyerror(""); }    // any undetected char

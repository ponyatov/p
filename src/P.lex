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

{s}?{d}+    { yylval.n = atoi(yytext); return INT; }
[^ \t\r\n]+ { yylval.s =      yytext;  return  ID; }

.           { yyerror(""); }    // any undetected char

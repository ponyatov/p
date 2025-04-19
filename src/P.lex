%{
    #include "P.hpp"
    char *yyfile = nullptr;
%}

%option yylineno noyywrap

%%
.       {yyerror("");}

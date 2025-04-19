%{
    #include "P.hpp"
%}

%defines %union { int n; char c; char *s; }

%token<n> INT
%token<s> ID

%%
syntax: | syntax ex

ex  : INT   { fprintf(stderr,"int:%i\n",$1); }
    | ID    { fprintf(stderr, "id:%s\n",$1); }

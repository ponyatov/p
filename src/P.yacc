%{
    #include "P.hpp"
%}

%defines %union { Object *o; }

%token<o> INT
%token<o> ID

%%
syntax: | syntax ex

ex  : INT   { $1->dump(); push($1); quest(); }
    | ID    { $1->dump();           quest(); }

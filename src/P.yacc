%{
    #include "P.hpp"
%}

%defines %union { Object *o; }

%token<o> INT
%token<o> ID

%%
syntax: | syntax ex { quest(); }

ex  : INT   { $1->exec(); }
    | ID    { Object *o = W[$1->val()];     // lookup
              if (!o) yyerror("not found");
              else    o->exec();            }

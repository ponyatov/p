#include "P.hpp"

int main(int argc, char *argv[]) {  //
    arg(0, argv[0]);
    for (int i = 1; i < argc; i++) {  //
        arg(i, argv[i]);
        yyfile = argv[i];
        assert(yyin = fopen(yyfile, "r"));
        yyparse();
        fclose(yyin);
        yyfile = nullptr;
    }
}

void arg(int argc, char *argv) {  //
    cerr << "arg[" << argc << "] = <" << argv << ">\n";
}

void yyerror(const char *msg) {
    cerr << "\n\n" << yyfile << ':' << yylineno << ' ' << msg;
    cerr << " [" << yytext << "]\n\n";
    exit(-1);
}

Object *Object::pool = nullptr;

Object::Object() {
    ref = 0;
    next = pool;
    pool = this;
}

Object::~Object() {}

Object::Object(string V) : Object() { value = V; }

Int::Int(string V) : Object() { value = atoi(V.c_str()); }
string Int::dump() { return to_string(value); }

Sym::Sym(string V) : Object(V) {}

Object *D[Dsz];
size_t Dp = 0;

void push(Object *o) {
    assert(Dp < Dsz);
    D[Dp++] = o;
}

Object *pop() {
    assert(Dp > 0);
    return D[--Dp];
}

void quest() {
    ostringstream os;
    os << "\n[ ";
    printf("\n[ ");
    for (int i = 0; i < Dp; i++) printf("%s ", D[i]->dump().c_str());
    os << "]\n";
    cout << os.str();
}

map<string, Object *> W;

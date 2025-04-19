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

#include <cxxabi.h>

string Object::tag() {
    string ret = abi::__cxa_demangle(typeid(*this).name(), NULL, NULL, nullptr);
    for (char &c : ret) c = tolower(c);
    return ret;
}

string Object::dump() {
    ostringstream os;
    os << tag() << ':' << val();
    return os.str();
}

Int::Int(string V) : Object() { value = atoi(V.c_str()); }
string Int::val() { return to_string(value); }

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
    for (int i = 0; i < Dp; i++) os << D[i]->dump() << ' ';
    os << "]\n";
    cout << os.str();
}

map<string, Object *> W;

MODULE = $(notdir $(CURDIR))

C += $(wildcard src/*.c*)
H += $(wildcard inc/*.h*)

CP += tmp/$(MODULE).yacc.cpp tmp/$(MODULE).lex.cpp
HP += tmp/$(MODULE).yacc.hpp

CFLAGS += -Iinc -Itmp -std=c++17

.PHONY: all run
all: bin/$(MODULE) lib/$(MODULE).ini
run: bin/$(MODULE) lib/$(MODULE).ini
	$^

bin/$(MODULE): $(C) $(H) $(CP) $(HP)
	$(CXX) $(CFLAGS) -o $@ $(C) $(CP)

tmp/%.yacc.cpp: src/%.yacc
	bison -o $@ $<
tmp/%.lex.cpp: src/%.lex
	flex -o $@ $<

.PHONY: doxy
doxy: .doxygen doc/DoxygenLayout.xml doc/logo.png
	rm -rf doc/html ; doxygen $< 1>/dev/null

.PHONY: install update
install:
	$(MAKE) update
update:
	sudo apt update
	sudo apt install `cat apt.$(shell lsb_release -si)`

MODULE = $(notdir $(CURDIR))

C += $(wildcard src/*.c*)
H += $(wildcard inc/*.h*)

CFLAGS += -Iinc -Itmp

.PHONY: all run
all: bin/$(MODULE) lib/$(MODULE).ini
run: bin/$(MODULE) lib/$(MODULE).ini
	$^

bin/$(MODULE): $(C) $(H) $(CP) $(HP)
	$(CXX) $(CFLAGS) -o $@ $(C) $(CP)

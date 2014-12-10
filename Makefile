o:
	gcc -c -Wall -Werror -fpic $(CFLAGS) guava.c

so: o
	gcc -shared -o libguava.so guava.o

main: so
	gcc -L. -Wl,-rpath=. -Wall -o test main.c -lguava
	
javatest: so
	javac guava.java && java guava > testdata

all: main

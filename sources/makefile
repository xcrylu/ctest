CC = gcc
CFLAGS = -Wall -g 
LDFLAGS = -lm  

TARGETS = 1 2 3 4 5 6 7 8 9 10

all: $(TARGETS)

%: %.c
	$(CC) $(CFLAGS) -o $@ $<  $(LDFLAGS)
	mv $@ ../bin/
	
clean:
	rm -f $(TARGETS)
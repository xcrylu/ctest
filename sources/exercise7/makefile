CC = gcc
CFLAGS = -Wall -g 
LDFLAGS = -lm  

TARGETS = 1 2 3 4 5 6 7 8 9 10 11 12 12 14 15


all: $(TARGETS)

%: %.c
	$(CC) $(CFLAGS) -o $@ $<  $(LDFLAGS)
	mv $@ ../../bin/exercise7/
	
clean:
	rm -f $(TARGETS)
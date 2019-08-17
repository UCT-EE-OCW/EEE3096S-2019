.RECIPEPREFIX +=
CC = g++
CFLAGS = -Wall -lm -lrt -lwiringPi -lpthread

PROG = bin/*
OBJS = obj/*

default:
    mkdir -p bin obj
    $(CC) $(CFLAGS) -c src/Prac4.cpp -o obj/Prac4
    $(CC) $(CFLAGS) obj/Prac4 -o bin/Prac4

run:
    sudo ./bin/Prac4

clean:
    rm $(PROG) $(OBJS)

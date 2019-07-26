.RECIPEPREFIX +=
CC = arm-linux-gnueabihf-g++
CFLAGS = -lm -lrt
INCLUDE = -ITools

PROG = bin/*
OBJS = obj/*


default:
    $(CC) $(INCLUDE) $(CFLAGS) -c src/Prac2.c -o obj/Prac2.o
    $(CC) $(INCLUDE) $(CFLAGS) -c Tools/Timer.cpp -o obj/Timer.o
    $(CC) -o bin/Prac2 obj/Prac2.o obj/Timer.o $(CFLAGS)

threaded:
    $(CC) $(INCLUDE) $(CFLAGS) -c src/Prac2_threaded.c -o obj/Prac2_threaded.o
    $(CC) $(INCLUDE) $(CFLAGS) -c Tools/Timer.cpp -o obj/Timer.o
    $(CC) -o bin/Prac2_threaded obj/Prac2_threaded.o obj/Timer.o $(CFLAGS) -pthread

run:
    bin/Prac2

run_threaded:
    bin/Prac2_threaded

clean: 
    rm -rf $(PROG) $(OBJ) 

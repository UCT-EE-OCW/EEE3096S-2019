.RECIPEPREFIX +=
cc = arm-linux-gnueabihf-g++
ccflags = -lm
sources = test.c Timer.cpp

default: $(obj)
    make clean
    $(cc) $(ccflags) $(sources) -o compiled_program

clean: 
    rm -f *.o
    rm -f compiled_program

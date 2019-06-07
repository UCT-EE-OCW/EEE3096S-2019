cc = arm-linux-gnueabihf-g++
ccflags = -lm
obj = adder.o

default: 

heterodyne: $(obj)
    $(cc) $(ccflags) -o $(outputfile) $(obj)

clean: 
    rm -f *.o
    rm -f heterodyne

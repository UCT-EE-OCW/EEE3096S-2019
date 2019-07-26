# Prac 2 
Working with benchmarking and architecture specific optimisations.
Special thanks to [KaliumPuceon](https://github.com/KaliumPuceon) for their contributions to the Threaded C implementation.

## Folder Contents
#### Python
- Prac2.py  - Source code for python
- Timing.py - Module that handles timing of the critical section
- data.py - Contains source data
- olddata.py - Original source data. Not relevant for the practical

#### C
- Tools/ - Contains the Timing library used
- bin/ - Contains the compiled files
- obj/ - Contains object files
- src/ - The source code (header files, etc)
  - globals.h - The source data
  - Prac2.c and Prac2.h are source for non-parallel version
  - Prac2_threaded.c and Prac2_threaded.h are source for the threaded version
- makefile

## Running the Prac
#### Python
To run the Python benchamrk, enter into the Python directory, and run
```./Prac2.py```
You may need to give it permission to execute. To do so, you can run
```chmod +x Prac2.py```

#### C
All running of the C code is done through ```make``` commands. 
- ```make``` will compile Prac2.c
- ```make run``` will run Prac2
- ```make threaded``` will compile the threaded version of Prac 2
- ```make run_threaded``` will run the threaded version
- ```make clean``` will clean the object and binary files that have been compiled

## Editing configurations
To run some experiments for C, you need to make edits to certain files and then recompile the relevant practical (threaded/unthreaded).
#### Editing bit widths
To edit bit withs, you need to make edits to
- globals.h
  - This is a large file, so editing it will be laggy. Just be patient :)
- Prac2.c (if you're working on the unthreaded version)
- Prac2_threaded.c (if you're working on the threaded version)
- makefile (if you need to run at 16 bits)
Possible bit widths include:
- ```double``` - 64 bit floating point
- ```float``` - 32 bit floating point
- ```__fp16``` - 16 bit floating point
  - You need to add ```-mfp16-format=ieee``` to ```$(CFLAGS)``` to use 16 bit floating point
#### Editing compiler flags
To edit compiler flags, changes need to be made in the makefile. Read the practical for further instruction.
#### Making use of hardware acceleration
You need to instruct the compiler to make use of specifc instruction sets. To do so, you need the 
```-mfpu=<floating_point_unit>``` 
flag. This is added as a part of ```$(CFLAGS)```

#!/usr/bin/python3
"""
Python Practical 2 Code for heterodyning and performance testing
Keegan Crankshaw
EEE3096S Prac 2 2019
Date: 7 June 2019

This isn't exactly performant code, but it is Pythonic
This is done to stress the differences between Python and C/C++

"""

# import Relevant Librares
import Timing
from data import carrier, data

# Define values.
c = carrier *30
d = data *30
result = []

# Main function
def main():
    print("using type {}".format(type(data[0])))
    Timing.startlog()
    for i in range(len(c)):
        result.append(c[i] * d[i])
    Timing.endlog()

# Only run the functions if this module is run
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
    except Exception as e:
        print("Error: {}".format(e))

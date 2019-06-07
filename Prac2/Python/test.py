#!/usr/bin/python3
"""
Python Practical 2 Code for heterodyning and performance testing
Keegan Crankshaw
EEE3096S Prac 2 2019
Date: 7 June 2019
"""

# import Relevant Librares
import Timing
import time
from array import array
from data import carrier, data

# Define values. See below for array initilisation 
# https://www.geeksforgeeks.org/array-python-set-1-introduction-functions/
c = array('f', carrier)
d = array('f',data)

# We're going to use the "pythonic" way of creating an array
# Even though pre-allocating memory might be faster
result = array('f' ,[])

# Logic that you write
def main():
    print("Starting test code")
    print("using type {}".format(type(data[0])))
    print("Starting timer")
    Timing.start()
    for i in range(len(c)):
        result.append(c[i] * d[i])
    print(result)
    print("End test code")

# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
    except Exception as e:
        print("Error: {}".format(e.message()))

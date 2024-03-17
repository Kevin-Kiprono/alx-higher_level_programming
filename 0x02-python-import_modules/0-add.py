#!/usr/bin/python3
if  __name__    ==  "__main__":

    """print the sum of 1 and 2."""

    #imports the add function from the module add_0

from add_0 import add
 
     #assigning values of variables a and b
a = 1
b = 2

     #calling the add function and storing the result      

result = add(a, b)

     #printing the results in the required format
print("{} + {} = {}".format(a, b, result))


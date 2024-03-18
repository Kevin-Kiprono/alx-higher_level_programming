#!/usr/bin/python3

def print_list_integer(my_list=None):
    """"print integers function

    one integer per line
    dont't import any modelu or cast integers to the strings
    assume the list only contains integers
    use str.format() to print
    """
    if my_list is not None:
        for integer in my_list:
            print("{:d}".format(integer))
